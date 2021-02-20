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
mpl.rcParams['font.family'] = 'Verdana'
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
print ('Data dir:',  sys.argv[1])
print ('Scan (s):',  sys.argv[2])
print ('Type of plot:',  sys.argv[3])

folder = sys.argv[1]
scans = sys.argv[2]
ComplexNumber = sys.argv[3]
axplot = sys.argv[4]

# transform string of list into python list object
if scans.startswith("["):
    scans = ast.literal_eval(scans)
    
elif scans == "all":
    subdirnames = [x[1] for x in os.walk(f"{folder}/")][0]
    scans = [int(s.replace("S", "")) for s in sorted(subdirnames) if s.startswith("S")]
    print(scans)
    
else:
    scans = [int(scans)]

root_folder = "/home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/com/" + folder + "/" # folder of the experiment, where all scans are stored
# root_folder = "/users/simonne/Documents/id01_david/SIXS_Jan/Pt_Al2O3/" + folder + "/" # folder of the experiment, where all scans are stored
sample_name = "S"  # str or list of str of sample names (string in front of the scan number in the folder name).

#mkdir slices
filenames = sorted(glob.glob(root_folder + sample_name + str(scan) + "/pynxraw/*LLK*.cxi")

# Load data
for f in filenames:
    print(f)
    # Plot
    # Plotting(axplot, f, ComplexNumber)

                  
def Plotting(axplot, datapath, ComplexNumber):
	"""Interactive function to plot the cxi files, only open in read mode"""

	# Open the file
	try:
		with tb.open_file(datapath, "r") as f:
			# Since .cxi files follow a specific architectture, we know where our data is.
			data = f.root.entry_1.data_1.data[:]

	except Exception as E:
		raise NameError("Wrong path")

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

    i = r[0]//2 # min=0, max=r[0]-1, step=1,

	PlottingOptions = "2D" # options = [("2D plot", "2D"), ("2D contour plot", "2DC"),("3D surface plot", "3D")],

    # Create a new figure
    plt.close()

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
            plt.show()

        except IndexError:
            plt.close()
            print("No contour levels were found within the data range. Meaning there is very little variation in the dat, change index")# 