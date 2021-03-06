import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from IPython.display import display
import datetime
from scipy import interpolate
from scipy import special
from scipy.optimize import curve_fit

import matplotlib.colors as mcolors

"""
To make the valves data and the rga data work together, we need to:
	Interpolate both datasets on integer seconds
	Cut the valves data depending on the timestamp of the rga data
"""


class XCAT():
	"""Transforms scat raw data to pandas.DataFrame object from path/to/data
	Then allows to compare with differnet rga datasets
	"""

	def __init__(self, log_file):
		"""init with raw valves data
		"""

		self.log_file = log_file
		self.pathtodata = self.log_file if self.log_file.endswith(".txt") else self.log_file+".txt"

		self.MRS_pos = [
						"All", "Ar", "Ar+Shu", "All", "Rea+Ar", "Closed", "All", "Closed", "Ar", "Ar+Shu", "Shu",
						"Closed", "All", "Rea", "Rea", "Rea+Ar", "Rea+Ar", "Closed", "All", "Shu", "Rea+Shu",
						"Rea+Shu", "Shu", "Closed",
						]

		self.MIX_pos = [
						"NO", "All", "Closed", "H2+CO", "H2+O2+CO", "H2+O2", "H2", "All", "Closed", "NO+O2",
						"NO+O2+CO", "O2+CO", "O2", "All", "Closed", "H2+CO", "NO+H2+CO", "NO+CO", "CO", "All",
						"Closed", "NO+O2", "NO+H2+O2", "NO+H2"
						]

		self.gaz_travel_time = 12 #time for the gaz to travel from cell to detector
		self.time_shift = 128
		# Create dataframe
		try:
			self.df = pd.read_csv(
			    self.pathtodata,
			    header = None,
			    delimiter = "\t",
			    skiprows = 1,
			    names = [
		            "time_no", "flow_no", "setpoint_no", "valve_no",
		            "time_h2", "flow_h2", "setpoint_h2", "valve_h2",
		            "time_o2", "flow_o2", "setpoint_o2", "valve_o2",
		            "time_co", "flow_co", "setpoint_co", "valve_co",
		            "time_ar", "flow_ar", "setpoint_ar", "valve_ar",
		            "time_shunt", "flow_shunt", "setpoint_shunt", "valve_shunt",
		            "time_reactor", "flow_reactor", "setpoint_reactor", "valve_reactor",
		            "time_drain", "flow_drain", "setpoint_drain", "valve_drain",
		            "time_valve", "valve_MRS", "valve_MIX"]
		            )

		except OSError:
			raise OSError
		
		# Change time to unix epoch
		for column_name in ["time_no" ,"time_h2" , "time_o2", "time_co", "time_ar" , "time_shunt", "time_reactor", "time_drain", "time_valve"]:
		    column = getattr(self.df, column_name)
		    
		    column -= 2082844800

		display(self.df.head())

		display(self.df.tail())

		# define heater parameters
		self.heater_ramp = pd.DataFrame({
								    "Current" : [0.3 , 0.4 , 0.5 , 0.6 , 0.7 , 0.8 , 0.9 , 1.1 , 1.3 , 1.5 , 1.7],
								    "Temperature" : [T + 25 for T in [72 , 96 , 134 , 170 , 217 , 245 , 300, 355 ,433, 500, 571]]
								})
		
		self.heater_poly_fit_coef = np.polyfit(self.heater_ramp["Current"], self.heater_ramp["Temperature"], 1)
		self.heater_poly_fit = np.poly1d(self.heater_poly_fit_coef)

	
	# separate XCAT data
	def separate_xcat_dataframes(self, entry_list):
		"""Create new dataframes based on the gases that were analyzed"""
		self.entry_list = [g.lower() for g in entry_list]

		try:
			for entry in self.entry_list:
				if entry == "no":
					self.no_df = self.df.iloc[:, 0:4].copy()
					print(f"New dataframe created starting  or NO.")

				if entry == "h2":
					self.h2_df = self.df.iloc[:, 4:8].copy()
					print(f"New dataframe created starting for H2.")

				if entry == "o2":
					self.o2_df = self.df.iloc[:, 8:12].copy()
					print(f"New dataframe created starting for O2.")

				if entry == "co":
					self.co_df = self.df.iloc[:, 12:16].copy()
					print(f"New dataframe created starting for CO.")

				if entry == "ar":
					self.ar_df = self.df.iloc[:, 16:20].copy()
					print(f"New dataframe created starting for Ar.")

				if entry == "shunt":
					self.shunt_df = self.df.iloc[:, 20:24].copy()
					print(f"New dataframe created starting for shunt.")

				if entry == "reactor":
					self.reactor_df = self.df.iloc[:, 24:28].copy()
					print(f"New dataframe created starting for reactor.")

				if entry == "drain":
					self.drain_df = self.df.iloc[:, 28:32].copy()
					print(f"New dataframe created starting for drain.")

				if entry == "valve":
					self.valve_df = self.df.iloc[:, 32:35].copy()
					print(f"New dataframe created starting for valve.")

		except Exception as e:
			raise e


	# load and interpolate rga data
	def load_rga(self, rga_file, skiprows = 28, names = ["time", "CO", "O2", "Ar", "CO2", "C", "H2"]):
		"""Find timestamp of rga file and loads it as a DataFrame"""

		# Find timestamp
		with open(rga_file) as f:
			for line in f:
				if "Start time, " in line:
					timeline = line.rstrip() #rstrip remove the spaces at the end of the line
					self.time_stamp = time.mktime(datetime.datetime.strptime(timeline[12:], "%b %d, %Y  %I:%M:%S  %p").timetuple())
					print(f"Timestamp: {self.time_stamp} (unix epoch).")

		# Create dataframe
		try:
			self.rga_data = pd.read_csv(
			    rga_file,
			    delimiter = ',',
			    index_col = False,
			    names = names,
			    skiprows = skiprows)

		except OSError:
			raise OSError

		# Interpolate the valves data
		try:
			# get bad time axis 
			x = self.rga_data["time"]

			# get duration in seconds of the experiment linked to that dataset
			self.duration = int(float(x.values[-1]))

			print(f"Experiment duration: {self.duration} seconds.")

			# create new time column in integer seconds
			new_time_column = np.round(np.linspace(0, self.duration, self.duration + 1), 0)

			# proceed to interpolation over the new time axis
			interpolated_df = pd.DataFrame({
			    f"time" : new_time_column
			    })

			# Iterate over all the columns
			for col in self.rga_data.columns[self.rga_data.columns != "time"]:

			    y = self.rga_data[col].values

			    # tck = interpolate.splrep(x, y, s = 0)
			    # y_new = interpolate.splev(new_time_column, tck)

			    # this way is better
			    f = interpolate.interp1d(x, y)
			    interpolated_df[col] = f(new_time_column)

			# make sure that the time is integer
			interpolated_df["time"] = interpolated_df["time"].astype(int)

			# save
			setattr(self, "rga_df_interpolated", interpolated_df)
			print(f"New interpolated dataframe created for rga.")

			display(self.rga_df_interpolated.head())
			display(self.rga_df_interpolated.tail())

		except NameError:
			print("To interpolate also thr rga data, you need to run Valves.load_rga() first")

		except Exception as e:
			print("Play with the amount of columns names and the amount of rows skipped.")
			raise e


	# truncate data based on rga file
	def truncate_xcat_df(self):
		"""Truncate entry specific df based on timestamp and duration if given (otherwise from timestamp to end)"""

		if not self.entry_list:
			raise KeyError("Create rga dataframes first")

		try:
			for entry in self.entry_list:

				# find starting time for this df
				temp_df = getattr(self, f"{entry}_df").copy()
				index_start_time = (temp_df[f"time_{entry}"] - self.time_stamp).abs().argsort()[0]

				# create truncated df based on the duration of the rga data
				if self.duration:
					# reset time
					temp_df = temp_df.iloc[index_start_time:, :].reset_index(drop=True)
					temp_df[f"time_{entry}"] -= temp_df[f"time_{entry}"].values[0]

					# truncate based on duration (take one more sec to be sure to have enough data for interpolation)
					temp_df = temp_df[temp_df[f"time_{entry}"] < self.duration + 1]

					setattr(self, f"{entry}_df_truncated", temp_df)

					print(f"New truncated dataframe created starting from timestamp for {entry} and for {self.duration} seconds.")

				else:
					pass
					# temp_df = temp_df.iloc[index_start_time:, :].reset_index(drop=True)
					# temp_df[f"time_{entry}"] -= temp_df[f"time_{entry}"][0]

					# setattr(self, f"{entry}_df_truncated", temp_df)

					# print(f"New truncated dataframe created starting from timestamp for {entry}.")

		except Exception as e:
			raise e


	# only after truncation, otherwise too big
	def interpolate_xcat_df(self):
		"""Only possible if we already ran load_rga"""

		try:
			for entry in self.entry_list:

				# get dataframe
				temp_df = getattr(self, f"{entry}_df_truncated")

				# get bad time axis 
				x = temp_df[f"time_{entry}"]

				x_0 = int(temp_df[f"time_{entry}"].values[0])
				x_1 = int(temp_df[f"time_{entry}"].values[-1])

				# # get duration in seconds of the experiment linked to that dataset from rga if exist, or just length oh dataset
				# try:
				# 	exp_duration = self.duration
				# except:
				# 	exp_duration = int(x.values[-1])

				# create new time column in integer seconds
				new_time_column = np.linspace(x_0, x_1, x_1 + 1)

				# proceed to interpolation over the new time axis
				interpolated_df = pd.DataFrame({
				    f"time_{entry}" : new_time_column
				    })

				# Iterate over all the columns
				for col in temp_df.columns[temp_df.columns != f"time_{entry}"]:

				    y = temp_df[col].values

				    tck = interpolate.splrep(x, y, s = 0)
				    y_new = interpolate.splev(new_time_column, tck)
				    interpolated_df[col] = y_new

				# make sure that the time is integer
				interpolated_df[f"time_{entry}"] = interpolated_df[f"time_{entry}"].astype(int)

				# save
				setattr(self, f"{entry}_df_interpolated", interpolated_df)
				print(f"New interpolated dataframe created for {entry}.")

		except NameError:
			print("You need to get the experiment duration first, run XCAT.load_rga()")

		except Exception as e:
			raise e

	#### plotting functions for xcat data ###

	def plot_xcat_entry(self, plot_entry_list, df = "interpolated", zoom1 = [None, None, None, None], zoom2 = [None, None, None, None], cursor_positions = [None]):
		try:
			plot_entry_list = [g.lower() for g in plot_entry_list]

			for entry in plot_entry_list:
				plt.close()
				fig, ax = plt.subplots(2, 1, figsize = (16, 9))

				if df == "interpolated":
					plot_df = getattr(self, f"{entry}_df_interpolated")

				elif df == "truncated":
					plot_df = getattr(self, f"{entry}_df_truncated")

				else:
					raise NameError("Wrong df.")

				ax[0].plot(plot_df[f"time_{entry}"], plot_df[f"flow_{entry}"], label = f"flow_{entry}")
				ax[0].plot(plot_df[f"time_{entry}"], plot_df[f"setpoint_{entry}"], "--", label = f"setpoint_{entry}")
				ax[1].plot(plot_df[f"time_{entry}"], plot_df[f"valve_{entry}"], "--", label = f"valve_{entry}")

				ax[0].set_xlim([zoom1[0], zoom1[1]])
				ax[0].set_ylim([zoom1[2], zoom1[3]])
				ax[1].set_xlim([zoom2[0], zoom2[1]])
				ax[1].set_ylim([zoom2[2], zoom2[3]])

				# cursor
				try:
					#mcolors.CSS4_COLORS["teal"]
					for cursor_pos in cursor_positions:
						ax[0].axvline(cursor_pos, linestyle = "--", color = "#bb1e10")
						ax[1].axvline(cursor_pos, linestyle = "--", color = "#bb1e10")

				except TypeError:
					print("No cursor")

				finally:
					ax[0].set_ylabel("Flow",fontsize=16)
					ax[0].set_xlabel("Time (s)",fontsize=16)
					ax[1].set_ylabel("Valve position",fontsize=16)
					ax[1].set_xlabel("Time (s)",fontsize=16)

					ax[0].legend()
					ax[1].legend()

					plt.show()

		except KeyError as e:
			raise KeyError("Plot valves with Valves.plot_valves")


	def plot_xcat_valves(self, df = "interpolated", zoom1 = [None, None, None, None], zoom2 = [None, None, None, None], cursor_positions = [None]):
		try:

			fig, ax = plt.subplots(2, 1, figsize = (16, 9))

			if df == "interpolated":
				plot_df = getattr(self, "valve_df_interpolated")

			elif df == "truncated":
				plot_df = getattr(self, "valve_df_truncated")

			else:
				raise NameError("Wrong df.")

			ax[0].plot(plot_df["time_valve"], plot_df["valve_MRS"], label = "valve_MRS")
			ax[1].plot(plot_df["time_valve"], plot_df["valve_MIX"], label = "valve_MIX")

			# cursor
			try:
				#mcolors.CSS4_COLORS["teal"]
				for cursor_pos in cursor_positions:
					plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
			except TypeError:
				print("No cursor")

			finally:

				ax[0].set_xlim([zoom1[0], zoom1[1]])
				ax[0].set_ylim([zoom1[2], zoom1[3]])
				ax[1].set_xlim([zoom2[0], zoom2[1]])
				ax[1].set_ylim([zoom2[2], zoom2[3]])

				ax[0].set_ylabel("Valve position",fontsize=16)
				ax[0].set_xlabel("Time (s)",fontsize=16)
				ax[1].set_ylabel("Valve position",fontsize=16)
				ax[1].set_xlabel("Time (s)",fontsize=16)

				ax[0].legend()
				ax[1].legend()

				plt.show()

		except KeyError as e:
			raise KeyError("Are you sure you are trying to plot a gaz?")

		except AttributeError as e:
			raise e
			print("Interpolate data first")

	#### plotting functions for rga data ###

	def plot_rga(self, interpolated_data = True, plotted_columns = None, zoom = [None, None, None, None], cursor_positions = [None]):
		"""Plot rga data
		if plotted_columns = None, it plots all the columns
		"""

		if interpolated_data==True:
			norm_df = self.rga_df_interpolated.copy()
		else:
			norm_df = self.rga_data.copy()

		plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')

		try:
			for element in plotted_columns:
				plt.plot(norm_df.time.values, norm_df[element].values, linewidth = 2, label = f"Mass {element}")
		
		# if plotted_columns is None		
		except:
			for element in norm_df.columns[1:]:
				plt.plot(norm_df.time.values, norm_df[element].values, linewidth = 2, label = f"Mass {element}")

		plt.semilogy()

		# cursor
		try:
			#mcolors.CSS4_COLORS["teal"]
			for cursor_pos in cursor_positions:
				plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
		except TypeError:
			print("No cursor")

		finally:
			plt.xlim(zoom[0], zoom[1])
			plt.ylim(zoom[2], zoom[3])
			
			plt.title(f"Pressure for each element", fontsize=16)

			plt.xlabel('Time (s)',fontsize=16)
			plt.ylabel('Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='--')
			plt.show()


	def plot_rga_norm_leak(self, interpolated_data = True, leak_values = [1], leak_positions = [None, None], plotted_columns = None, zoom = [None, None, None, None], cursor_positions = [None]):
		"""
		Plot rga data normalized by the values given in leak_values on the intervals given by leak_positions
		e.g. leak_values = [1.3, 2] and leak_positions = [100, 200, 500] will result in a division by 1.3 between indices 100 and 200
		and by a division by 2 between indices 200 and 500.
		works on rga_df_interpolated
		if plotted_columns = None, it plots all the columns
		possible to use a zoom and vertical cursors (one or multiple) 
		"""
		if interpolated_data==True:
			norm_df = self.rga_df_interpolated.copy()
		else:
			norm_df = self.rga_data.copy()

		if len(leak_values) + 1 == len(leak_positions):

			plt.figure(figsize = (18, 13), dpi = 80, facecolor = 'w', edgecolor = 'k')

			# for each column
			try:
				for element in plotted_columns:
					normalized_values = norm_df[element].values.copy()

					# normalize between the leak positions
					for j, value in enumerate(leak_values):

						# print(f"We normalize between {leak_positions[j]} s and {leak_positions[j+1]} s by {value}")

						normalized_values[leak_positions[j]:leak_positions[j+1]] = (normalized_values[leak_positions[j]:leak_positions[j+1]] / value)

					plt.plot(norm_df.time.values, normalized_values, linewidth = 2, label = f"Mass {element}")
			
			# if plotted_columns is None
			except:
				for element in norm_df.columns[1:]:
					normalized_values = norm_df[element].values.copy()

					# normalize between the leak positions
					for j, value in enumerate(leak_values):

						# print(f"We normalize between {leak_positions[j]} s and {leak_positions[j+1]} s by {value}")

						normalized_values[leak_positions[j]:leak_positions[j+1]] = (normalized_values[leak_positions[j]:leak_positions[j+1]] / value)

					plt.plot(norm_df.time.values, normalized_values, linewidth = 2, label = f"Mass {element}")
			
			plt.semilogy()

			# cursor
			try:
				#mcolors.CSS4_COLORS["teal"]
				for cursor_pos in cursor_positions:
					plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
			except TypeError:
				print("No cursor")

			finally:
				plt.xlim(zoom[0], zoom[1])
				plt.ylim(zoom[2], zoom[3])

				plt.title(f"Normalized by pressure in rga (leak valve)", fontsize=16)

				plt.xlabel('Time (s)',fontsize=16)
				plt.ylabel('Pressure (mBar)',fontsize=16)
				plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
				       ncol=5, mode="expand", borderaxespad=0.)
				plt.grid(b=True, which='major', color='b', linestyle='-')
				plt.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='--')
				plt.show()

		else:
			print("Length of leak_positions should be one more than leak_values.")


	def plot_rga_norm_carrier(self, interpolated_data = True, carrier_gaz = "Ar", plotted_columns = None, zoom = [None, None, None, None], cursor_positions = [None]):
		"""
		Plot rga data normalized by one column (carrier_gaz)
		works on rga_df_interpolated
		if plotted_columns = None, it plots all the columns
		possible to use a zoom and vertical cursors (one or multiple) 
		"""
		if interpolated_data==True:
			norm_df = self.rga_df_interpolated.copy()
		else:
			norm_df = self.rga_data.copy()

		plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')
		
		try:
			plotted_columns.remove(carrier_gaz)

		except:
			plotted_columns = list(norm_df.columns).remove(carrier_gaz)

		for element in plotted_columns:
			norm_df[element] = norm_df[element] / norm_df[carrier_gaz]

			plt.plot(norm_df.time.values, norm_df[element].values, linewidth = 2, label = f"Mass {element}")
				
		plt.semilogy()

		# cursor
		try:
			#mcolors.CSS4_COLORS["teal"]
			for cursor_pos in cursor_positions:
				plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
		except TypeError:
			print("No cursor")

		finally:
			plt.xlim(zoom[0], zoom[1])
			plt.ylim(zoom[2], zoom[3])

			plt.title(f"Normalized by carrier gaz ({carrier_gaz}) pressure", fontsize=16)

			plt.xlabel('Time (s)',fontsize=16)
			plt.ylabel('Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='-')
			plt.show()


	def plot_rga_norm_ptot(self, interpolated_data = True, plotted_columns = None, ptot = None, zoom = [None, None, None, None], cursor_positions = [None]):
		"""
		Plot rga data normalized by the total pressure in the cell
		works on rga_df_interpolated
		if plotted_columns = None, it plots all the columns
		possible to use a zoom and vertical cursors (one or multiple) 
		"""

		if interpolated_data==True:
			norm_df = self.rga_df_interpolated.copy()

		else:
			norm_df = self.rga_data.copy()

		used_arr = norm_df.values
		ptot_row = used_arr[:,1:].sum(axis = 1) / ptot

		val = np.ones(used_arr.shape)
		val[:,1:] = (val[:,1:].T * ptot_row).T

		norm_df = pd.DataFrame(used_arr / val, columns = norm_df.columns)
		display(norm_df.head())

		plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')

		try:
			for element in plotted_columns:
				plt.plot(norm_df.time.values, norm_df[element].values, linewidth = 2, label = f"Mass {element}")

		# if plotted_columns is None
		except:
			for element in norm_df.columns[1:]:	
				plt.plot(norm_df.time.values, norm_df[element].values, linewidth = 2, label = f"Mass {element}")

		plt.semilogy()

		# cursor
		try:
			for cursor_pos in cursor_positions:
				plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")

		except TypeError:
			print("No cursor")

		finally:
			plt.xlim(zoom[0], zoom[1])
			plt.ylim(zoom[2], zoom[3])

			plt.title(f"Normalized by total pressure ({ptot} bar)",fontsize=16)

			plt.xlabel('Time (s)',fontsize=16)
			plt.ylabel('Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='--')
			plt.show()


	def plot_rga_norm_temp(self, start_heating, nb_points, amp_final, save = False, interpolated_data = True, delta_time = 10, bins_nb = 1000, binning = False, plotted_columns = None, zoom = [None, None, None, None], cursor_positions = [None]):
		"""
		Plot rga data normalized by the values given in intensity_values on the intervals given by leak_positions
		e.g. intensity_values = [1.3, 2] and leak_positions = [100, 200, 500] will result in a division by 1.3 between indices 100 and 200
		and by a division by 2 between indices 200 and 500.
		works on rga_df_interpolated
		if plotted_columns = None, it plots all the columns
		possible to use a zoom and vertical cursors (one or multiple) 
		"""
		if interpolated_data==True:
			norm_df = self.rga_df_interpolated.copy()
		else:
			norm_df = self.rga_data.copy()

		# recreate points that were used during data acquisition
		# amperage = np.round(np.concatenate((np.linspace(0, amp_final, nb_points*delta_time, endpoint=False), np.linspace(amp_final, 0, nb_points*delta_time))), 2)
		amperage = np.concatenate((np.linspace(0, amp_final, nb_points*delta_time, endpoint=False), np.linspace(amp_final, 0, nb_points*delta_time)))

		# recreate temperature from heater benchmarks
		temperature = self.heater_poly_fit(amperage)
		temperature_real = np.array([t if t >25 else 25 for t in temperature])

		# find end time
		end_heating = start_heating + (2 * nb_points) * delta_time

		# timerange of heating
		time_column = norm_df["time"].values[start_heating:end_heating]

		# save in df
		self.rga_during_heating = pd.DataFrame({
			"time" : time_column,
			"amperage" : amperage,
			"temperature" : temperature_real,
			})

		print("Results saved in self.rga_during_heating DataFrame")

		plt.figure(figsize = (18, 13), dpi = 80, facecolor = 'w', edgecolor = 'k')

		# for each column
		try:
			for element in plotted_columns:
				data_column = norm_df[element].values[start_heating:end_heating]
				self.rga_during_heating[element] = data_column

				if not binning:
					plt.plot(temperature_real, data_column, linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")
		
		# if plotted_columns is None
		except:
			for element in norm_df.columns[1:]:
				data_column = norm_df[element].values[start_heating:end_heating]
				self.rga_during_heating[element] = data_column
				if not binning:
					plt.plot(self.rga_during_heating.temperature, self.rga_during_heating[element], linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")
					# plt.plot(temperature_real, data_column, linewidth = 2, label = f"Mass {element}")

		# do binning after so that the dataframe on heating timerange already exists
		if binning:
			# Bin the data frame by "time" with bins_nb bins...
			bins = np.linspace(self.rga_during_heating.time.min(), self.rga_during_heating.time.max(), bins_nb)
			groups = self.rga_during_heating.groupby(np.digitize(self.rga_during_heating.time, bins))

			# Get the mean of each bin:
			self.binned_data = groups.mean()
			for element in plotted_columns:
				plt.plot(self.binned_data.temperature, self.binned_data[element], linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")

		plt.semilogy()

		# cursor
		try:
			#mcolors.CSS4_COLORS["teal"]
			for cursor_pos in cursor_positions:
				plt.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
		except TypeError:
			print("No cursor")

		finally:
			plt.xlim(zoom[0], zoom[1])
			plt.ylim(zoom[2], zoom[3])
			if not binning:
				plt.title(f"Pressure as a function of the temperature (from input current)", fontsize=16)
			else:
				plt.title(f"Pressure as a function of the temperature (from input current), with {bins_nb} bins.", fontsize=16)

			plt.xlabel('Temperature (°C)',fontsize=16)
			plt.ylabel('Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='--')
			if save == True:
				plt.tight_layout()
				plt.savefig("plot_rga_norm_temp.png")
				print("Saved as plot_rga_norm_temp.png")
			plt.show()


	def fit_error_function(self, initial_guess, new_amper_vect, interpolated_data = True, fitted_columns = None, binning = False, zoom = [None, None, None, None], cursor_positions = [None]):
		"""fit pressure vs temperature dta with error function"""

		def error_function(z, a, b, c, d):
		    return a * (1 + special.erf((z - b) / c) ) + d

		longer_temp_vect = self.heater_poly_fit(new_amper_vect)

		if not binning:
			used_df = self.rga_during_heating.copy()
			xdata = used_df.temperature
		else:
			used_df = self.binned_data.copy()
			xdata = used_df.temperature

		fig, ax = plt.subplots(1, 1, figsize = (18, 13), dpi = 80, facecolor = 'w', edgecolor = 'k')

		try:
			for element in fitted_columns:
				ydata = used_df[element]
				popt, pcov = curve_fit(error_function, xdata, ydata, p0 = initial_guess)
				# ax.plot(xdata, func(xdata, *guessErf))
				ax.plot(xdata, ydata, linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")
				#ax.plot(xdata, func(xdata, *popt))
				ax.plot(longer_temp_vect, error_function(longer_temp_vect, *popt), linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")

		except:
			for element in used_df.columns[1:]:
				ydata = used_df[element]
				popt, pcov = curve_fit(error_function, xdata, ydata, p0 = initial_guess)
				# ax.plot(xdata, func(xdata, *guessErf))
				ax.plot(xdata, ydata, linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")
				#ax.plot(xdata, func(xdata, *popt))
				ax.plot(longer_temp_vect, error_function(longer_temp_vect, *popt), linewidth = 2, linestyle = "dashdot", label = f"Mass {element}")

		# cursor
		try:
			#mcolors.CSS4_COLORS["teal"]
			for cursor_pos in cursor_positions:
				ax.axvline(x = cursor_pos, linestyle = "--", color = "#bb1e10")
		except TypeError:
			print("No cursor")

		finally:
			ax.set_xlim(zoom[0], zoom[1])
			ax.set_ylim(zoom[2], zoom[3])

			ax.set_xlabel('Temperature (°C)',fontsize=16)
			ax.set_ylabel('Pressure (mBar)',fontsize=16)
			ax.legend(bbox_to_anchor=(0., -0.1, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			ax.grid(b=True, which='major', color='b', linestyle='-')
			ax.grid(b=True, which='minor', color=mcolors.CSS4_COLORS["teal"], linestyle='--')

			plt.title("Temperature vs pressure graphs fitted with error functions")
			plt.show()