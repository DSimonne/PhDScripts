import sys
import numpy as np
import tables as tb
import ast
import shutil
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from mpl_toolkits.mplot3d import Axes3D

import glob
import cmath

# Annoying warnings bc of .cxi files
import warnings
warnings.filterwarnings("ignore")

# Edit overall plot parameters
# Font parameters
# mpl.rcParams['font.family'] = 'Verdana'
mpl.rcParams['font.size'] = 18

# Edit axes parameters
mpl.rcParams['axes.linewidth'] = 2

# Tick properties
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['ytick.direction'] = 'out'

"""Python script to show slices of cxi files"""
 
# Print all arguments
print ('Argument List:', str(sys.argv))
 
# Print arguments one by one
cwd = os.getcwd()
scan_dir = os.getcwd() + "/" + sys.argv[1]

print("Scan directory", scan_dir)
print ('Type of plot:',  sys.argv[2])
print ('Axes for projection:',  sys.argv[3])
print ('Plotting options:',  sys.argv[4])
print("Index for slice:", sys.argv[5])

ComplexNumber = sys.argv[2]
axplot = sys.argv[3]
PlottingOptions = sys.argv[4] # options = [("2D plot", "2D"), ("2D contour plot", "2DC"),("3D surface plot", "3D")],

def Plotting(axplot, datapath, ComplexNumber):
	"""Interactive function to plot the cxi files, only open in read mode"""

	# Open the file
	try:
		with tb.open_file(datapath, "r") as f:
			# Since .cxi files follow a specific architectture, we know where our data is.
			data = f.root.entry_1.data_1.data[:]

	except Exception as E:
		raise NameError("Wrong path")

	# Save run name
	run = "Run" + datapath.split("Run")[1].split("_LLK")[0]
	print(run)

	# Decide what we want to plot
	if ComplexNumber == "Real":
		PlottedArrayType = np.real(data)
	elif ComplexNumber == "Imaginary":
		PlottedArrayType = np.imag(data)
	elif ComplexNumber == "Module":
		PlottedArrayType = np.abs(data)
	else:
		PlottedArrayType = np.angle(data)

	# Print the shape of that array along 2 axis, use the last dimension for plotting and Project along two axes
	if axplot == "xy":
		print(f"The shape of this projection is {np.shape(data[:, :, 0])}")

		r = np.shape(data[0, 0, :])
		print(f"Length of last axis: {r[0]}")

	elif axplot == "yz":
		print(f"The shape of this projection is {np.shape(data[0, :, :])}")

		r = np.shape(data[:, 0, 0])
		print(f"Length of last axis: {r[0]}")

	else:
		print(f"The shape of this projection is {np.shape(data[:, 0, :])}")

		r = np.shape(data[0, :, 0])
		print(f"Length of last axis: {r[0]}")

	# Create a new figure
	plt.close()
	if sys.argv[5] == "mid":
		i = r[0]//2 # min=0, max=r[0]-1, step=1,
	else:
		i = int(sys.argv[5])

	# Print the shape of that array along 2 axis, use the last dimension for plotting and Project along two axes
	if axplot == "xy":
	    TwoDPlottedArray = PlottedArrayType[:, :, i]

	elif axplot == "yz":
	    TwoDPlottedArray = PlottedArrayType[i, :, :]

	else:
	    TwoDPlottedArray = PlottedArrayType[:, i, :]

	# Find max and min
	dmax = TwoDPlottedArray.max()
	dmin = TwoDPlottedArray.min()

	# print(f"Current index: {i}")
	# print(np.mean(TwoDPlottedArray))

	# Create figure and add axis
	# fig = plt.figure(figsize=(20,10))
	# ax = fig.add_subplot(111)

	# Remove x and y ticks
	# ax.xaxis.set_tick_params(size=0)
	# ax.yaxis.set_tick_params(size=0)
	# ax.set_xticks([])
	# ax.set_yticks([])

	# Show image
	if PlottingOptions == "2D":
	    plt.close()
	    fig, ax = plt.subplots(figsize = (15,15))
	    img = ax.imshow(TwoDPlottedArray,
	                origin='lower',
	                cmap='YlGnBu_r',
	                #extent=(0, 2, 0, 2),
	                vmin = dmin,
	                vmax = dmax)

	    # # Create scale bar (only if we know the  image size)
	    # ax.fill_between(x=[1.4, 1.9], y1=[0.1, 0.1], y2=[0.2, 0.2], color='white')

	    # ax.text(x=1.65, y=0.25, s='500 nm', va='bottom', ha='center', color='white', size=20)

	    # Create axis for colorbar
	    cbar_ax = make_axes_locatable(ax).append_axes(position='right', size='5%', pad=0.1)

	    # Create colorbar
	    cbar = fig.colorbar(mappable=img, cax=cbar_ax)

	    # Edit colorbar ticks and labels
	    ticks = [dmin + n * (dmax-dmin)/10 for n in range(0, 11)]
	    tickslabel = [f"{t}" for t in ticks]

	    cbar.set_ticks(ticks)
	    cbar.set_ticklabels(tickslabel)
	    plt.savefig(f"{scan_dir}/images/{run}_{axplot}_{i}_2D.png")
	    print(f"Saved as {scan_dir}/images/{run}_{axplot}_{i}_2D.png")
	    #plt.show()

	elif PlottingOptions == "2DC" :
	    plt.close()
	    # Show contour plot instead
	    try:
	        fig, ax = plt.subplots(figsize = (15,15))
	        ticks = [dmin + n * (dmax-dmin)/10 for n in range(0, 11)]

	        img = ax.contour(TwoDPlottedArray,
	                        ticks,
	                    #extent=(0, 2, 0, 2),
	                    cmap='YlGnBu_r',
	                    vmin=dmin,
	                    vmax=dmax)

	        # Create axis for colorbar
	        cbar_ax = make_axes_locatable(ax).append_axes(position='right', size='5%', pad=0.1)

	        # Create colorbar
	        cbar = fig.colorbar(mappable=img, cax=cbar_ax)

	        # Edit colorbar ticks and labels
	        tickslabel = [f"{t}" for t in ticks]

	        cbar.set_ticks(ticks)
	        cbar.set_ticklabels(tickslabel)
	        plt.savefig(f"{scan_dir}/images/{run}_{axplot}_{i}_2DC.png")
	        print(f"Saved as {scan_dir}/images/{run}_{axplot}_{i}_2DC.png")
	        #plt.show()

	    except IndexError:
	        plt.close()
	        print("No contour levels were found within the data range. Meaning there is very little variation in the dat, change index")# 


try:
	os.mkdir(f"{scan_dir}/images")
except FileExistsError:
    pass
filenames = glob.glob(f"{scan_dir}/*LLK*.cxi")
# Load data
for f in filenames:	    
    # Plot
    Plotting(axplot, f, ComplexNumber)