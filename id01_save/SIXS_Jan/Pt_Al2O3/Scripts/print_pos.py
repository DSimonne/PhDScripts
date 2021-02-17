import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import ReadNxs3 as rd

def find_pos(scan_nb, verbose = False):
    print(scan_nb, end="; ")
    data = rd.DataSet(f"data/Pt_Al2O3_ascan_mu_0{scan_nb}.nxs")
    if verbose:
        print("x = ", data.x[0])
        print("y = ", data.y[0])
        print("z = ", data.z[0])
        print("mu = ", data.mu[0])
        print("delta = ", data.delta[0])
        print("omega = ", data.omega[0])
        print("gamma = ", data.gamma[0])
        print("gamma-mu = ", data.gamma[0] - data.mu[0])
        print(f"Rocking angle steps ={(data.mu[-1] - data.mu[-0]) / len(data.mu)}")

"""Part of script to allow systematic use"""

import ast
import sys

# Print total number of arguments
print ('Total number of arguments:', format(len(sys.argv)))
 
# Print all arguments
print ('Argument List:', str(sys.argv))
 
# Print arguments one by one
# print ('First argument:',  str(sys.argv[0]))
print ('Scan (s):',  sys.argv[1])

# transform string of list into python list object
if sys.argv[1].startswith("["):
    scans = ast.literal_eval(sys.argv[1])
else:
    scans = [int(sys.argv[1])]

for s in scans:
    find_pos(s, verbose = True)