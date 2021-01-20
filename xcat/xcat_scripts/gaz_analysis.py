import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
from IPython.display import display
import datetime
from scipy import interpolate
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


	# load and interpolate rga data
	def load_rga(self, rga_file, rename_columns = False):
		"""Find timestamp of rga file and loads it as a DataFrame"""

		if rename_columns:
			names = ["Time(s)", "CO", "O2", "Ar", "CO2", "C", "H2"]

		else:
			names = ["Time(s)", "Channel#1", "Channel#2", "Channel#3", "Channel#4", "Channel#5", "Channel#6"]

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
			    skiprows = 28)

		except OSError:
			raise OSError

		# Interpolate the valves data
		try:
			# get bad time axis 
			x = self.rga_data["Time(s)"]

			# get duration in seconds of the experiment linked to that dataset
			self.duration = int(x.values[-1])

			print(f"Experiment duration: {self.duration} seconds.")

			# create new time column in integer seconds
			new_time_column = np.round(np.linspace(0, self.duration, self.duration + 1), 0)

			# proceed to interpolation over the new time axis
			interpolated_df = pd.DataFrame({
			    f"time" : new_time_column
			    })

			# Iterate over all the columns
			for col in self.rga_data.columns[self.rga_data.columns != "Time(s)"]:

			    y = self.rga_data[col].values

			    tck = interpolate.splrep(x, y, s = 0)
			    y_new = interpolate.splev(new_time_column, tck)
			    interpolated_df[col] = y_new

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
			raise e


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

	#### plotting functions ###

	def plot_xcat_entry(self, plot_entry_list, df = "interpolated", zoom1 = [None, None, None, None], zoom2 = [None, None, None, None], cursor_positions = [None]):
		try:
			plot_entry_list = [g.lower() for g in plot_entry_list]

			fig, ax = plt.subplots(2, 1, figsize = (16, 9))

			for entry in plot_entry_list:

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

				ax[0].set_ylabel("Flow",fontsize=16)
				ax[0].set_xlabel("Time (s)",fontsize=16)
				ax[1].set_ylabel("Valve position",fontsize=16)
				ax[1].set_xlabel("Time (s)",fontsize=16)

				ax[0].legend()
				ax[1].legend()

				plt.show()

		except KeyError as e:
			raise KeyError("Are you sure you are trying to plot a gaz?")


	def plot_rga(self, plotted_columns = ["CO", "O2", "Ar", "CO2", "C", "H2"], zoom = [None, None, None, None], cursor_positions = [None]):
		"""Plot rga data
		if plotted_columns = None, it plots all the columns
		"""

		plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')
		for element in plotted_columns:
			plt.plot(self.rga_df_interpolated.time.values, self.rga_df_interpolated[element].values, linewidth = 2, label = f"Mass {element}")
			
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

			plt.xlabel('Time (s)',fontsize=16)
			plt.ylabel('Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color='r', linestyle='--')
			plt.show()


	def plot_rga_norm_leak(self, leak_values = [1], leak_positions = [None, None], plotted_columns = ["CO", "O2", "Ar", "CO2", "C", "H2"], zoom = [None, None, None, None], cursor_positions = [None]):
		"""Plot rga data
		if plotted_columns = None, it plots all the columns
		"""

		if len(leak_values) + 1 == len(leak_positions):

			plt.figure(figsize = (18, 13), dpi = 80, facecolor = 'w', edgecolor = 'k')

			# for each column
			for element in plotted_columns:
				normalized_values = self.rga_df_interpolated[element].values.copy()

				# normalize between the leak positions
				for j, value in enumerate(leak_values):

					# print(f"We normalize between {leak_positions[j]} s and {leak_positions[j+1]} s by {value}")

					normalized_values[leak_positions[j]:leak_positions[j+1]] = (normalized_values[leak_positions[j]:leak_positions[j+1]] / value)

				plt.plot(self.rga_df_interpolated.time.values, normalized_values, linewidth = 2, label = f"Mass {element}")
				
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

				plt.xlabel('Time (s)',fontsize=16)
				plt.ylabel('Normalized Pressure (mBar)',fontsize=16)
				plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
				       ncol=5, mode="expand", borderaxespad=0.)
				plt.grid(b=True, which='major', color='b', linestyle='-')
				plt.grid(b=True, which='minor', color='r', linestyle='--')
				plt.show()

		else:
			print("Length of leak_positions should be one more than leak_values.")


	def plot_rga_norm_ptot(self, plotted_columns = ["CO", "O2", "Ar", "CO2", "C", "H2"], ref_column = "CO", zoom = [None, None, None, None], cursor_positions = [None]):
		"""Plot rga data
		if plotted_columns = None, it plots all the columns
		"""

		norm_df = self.rga_df_interpolated.copy()

		plt.figure(figsize=(18, 13), dpi=80, facecolor='w', edgecolor='k')
		for element in plotted_columns:
			if element != ref_column:
				norm_df[element] = norm_df[element] / norm_df[ref_column]

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

			plt.xlabel('Time (s)',fontsize=16)
			plt.ylabel('Partial Pressure (mBar)',fontsize=16)
			plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
			       ncol=5, mode="expand", borderaxespad=0.)
			plt.grid(b=True, which='major', color='b', linestyle='-')
			plt.grid(b=True, which='minor', color='r', linestyle='--')
			plt.show()


	# def plot_decimal(self, entry):
	# 	try:

	# 		plt.close()
	# 		fig, ax = plt.subplots(3, 1, figsize = (16, 9))

	# 		# Normal scale

	# 		ax[0].plot(plot_df[f"time_{entry}"], plot_df[f"flow_{entry}"], label = "flow_{entry}")
	# 		ax[1].plot(plot_df[f"time_{entry}"], plot_df[f"setpoint_{entry}"], label = "setpoint_{entry}")
	# 		ax[2].plot(plot_df[f"time_{entry}"], plot_df[f"valve_{entry}"], label = "valve_{entry}")

	# 		ax[0].legend()
	# 		ax[1].legend()
	# 		ax[2].legend();

	# 	except KeyError:
	# 		raise KeyError("Wrong entry name")


	# def plot_log(self, entry):
	# 	try:

	# 		plt.close()
	# 		fig, ax = plt.subplots(3, 1, figsize = (16, 9))

	# 		# logscale

	# 		ax[0].plot(np.log(plot_df[f"time_{entry}"]), np.log(plot_df[f"flow_{entry}"]), label = "flow_{entry}")
	# 		ax[1].plot(np.log(plot_df[f"time_{entry}"]), np.log(plot_df[f"setpoint_{entry}"]), label = "setpoint_{entry}")
	# 		ax[2].plot(np.log(plot_df[f"time_{entry}"]), np.log(plot_df[f"valve_{entry}"]), label = "valve_{entry}")

	# 		ax[0].legend()
	# 		ax[1].legend()
	# 		ax[2].legend();

	# 	except KeyError:
	# 		raise KeyError("Wrong entry name")
