import sys
import numpy as np
import tables as tb
import matplotlib.pyplot as plt
import ast
import shutil
import os

"""Python script to rotate the data for vertical configuration"""
 
# Print all arguments
print ('Argument List:', str(sys.argv))
 
# Print arguments one by one
print ('Scan (s):',  sys.argv[2])
print ('Data dir:',  sys.argv[1])

folder = sys.argv[1]

# transform string of list into python list object
if sys.argv[2].startswith("["):
    scans = ast.literal_eval(sys.argv[2])
    
elif sys.argv[2]=="all":
    subdirnames = [x[1] for x in os.walk(f"{folder}/")][0]
    scans = [s.replace("S", "") for s in sorted(subdirnames) if s.startswith("S")]
    print(scans)
    
else:
    scans = [int(sys.argv[2])]

# root_folder = "/data/id01/inhouse/david/SIXS_Jan/Pt_Al2O3/" +"testflip" + "/"  # folder of the experiment, where all scans are stored
root_folder = "/users/simonne/Documents/id01_david/SIXS_Jan/Pt_Al2O3/" + folder + "/"  # folder of the experiment, where all scans are stored
sample_name = "S"  # str or list of str of sample names (string in front of the scan number in the folder name).

# Load data
for scan in scans:
    print(scan)
    
    filename = root_folder + sample_name + str(scan) + "/data/Pt_Al2O3_ascan_mu_0" + str(scan) + ".nxs"
    f_copy = root_folder + sample_name + str(scan) + "/data/Pt_Al2O3_ascan_mu_0" + str(scan) + "_R.nxs"
    
    shutil.copy2(filename, f_copy)
    print("Saved a copy of the data as ", f_copy)

    print(f"Opening scan {scan} data ...")
    with tb.open_file(f_copy, "a") as f:
        # print(f)

        # Get data
        try:
            data_og = f.root.com.scan_data.data_02[:]
            print("Trying to climb eiger ...")
        except:
            try:
                data_og = f.root.com.scan_data.merlin_image[:]
                print("Calling merlin the enchanter ...")
            except:
                print("This data does not result from Eiger nor Merlin :/")

        # Just an index for plotting schemes
        half = int(data_og.shape[0]/2)

        # Rotate data
        data = np.transpose(data_og, axes=(0, 2, 1))
        for idx in range(data.shape[0]):
            tmp = data[idx, :, :]
            data[idx, :, :] = np.fliplr(tmp)
        print("Data well rotated by 90°.")  

        print("Saving example figures...", end="\n\n")
        plt.figure(figsize = (16, 9))
        plt.imshow(data_og[half, :, :], vmax = 10)
        plt.xlabel('Delta')
        plt.ylabel('Gamma')
        plt.tight_layout()
        plt.savefig(root_folder + sample_name + str(scan) + "/data/data_before_rotation.png")

        plt.figure(figsize = (16, 9))        
        plt.imshow(data[half, :, :], vmax = 10)
        plt.xlabel('Gamma')
        plt.ylabel('Delta')
        plt.tight_layout()
        plt.savefig(root_folder + sample_name + str(scan) + "/data/data_after_rotation.png")
        plt.close()

        # Overwrite data
        try:
            f.root.com.scan_data.data_02[:] = data
        except:
            try:
                f.root.com.scan_data.merlin_image[:] = data
            except:
                print("Could not overwrite data ><")