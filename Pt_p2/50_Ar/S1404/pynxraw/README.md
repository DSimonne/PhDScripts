# Run pynx

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-run-no-support.txt
data S1414_pynx_norm_128_300_294_1_1_1.npz
mask S1414_maskpynx_norm_128_300_294_1_1_1.npz
data2cxi True
auto_center_resize False
support_threshold 0.2, 0.3
support_only_shrink False
support_update_period 20
support_smooth_width_begin 2
support_smooth_width_end 1
support_post_expand 1,-2,1
mask_interp 8,2
confidence_interval_factor_mask 0.5,1.2
psf True
nb_raar 1000
nb_hio 400
nb_er 300
nb_ml 0
nb_run 100
nb_run_keep 10
zero_mask False
crop_output 0
positivity False
beta 0.9
detwin False
rebin 1,1,1
detector_distance 0.84
pixel_size_detector 55e-6
wavelength 1.2423e-10
verbose 100
output_format cxi
live_plot False

Loading data:  S1414_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1414_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 858948 pixels masked ( 7.608%)
Saving data to CXI file:  S1414_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   699 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   608 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Run modes

````bash
(devel.p9) p9-01:50_Ar/S1404/pynxraw % python pynx-cdi-analysis.py S1404_pynx_norm_128_300_294_1_1_1-* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-01
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T22-13-50_Run0006_LLKf000.1098_LLK000.1203_SupportThreshold0.29956.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T22-54-50_Run0021_LLKf000.1098_LLK000.1204_SupportThreshold0.29983.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-11-13_Run0027_LLKf000.1099_LLK000.1205_SupportThreshold0.29321.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-19-27_Run0030_LLKf000.1098_LLK000.1204_SupportThreshold0.29257.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-27-28_Run0033_LLKf000.1098_LLK000.1203_SupportThreshold0.29950.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-49_Run0036_LLKf000.1095_LLK000.1203_SupportThreshold0.29718.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-52-21_Run0042_LLKf000.1102_LLK000.1204_SupportThreshold0.29237.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-35-11_Run0061_LLKf000.1098_LLK000.1205_SupportThreshold0.29505.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-49-28_Run0079_LLKf000.1099_LLK000.1204_SupportThreshold0.29205.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-56-20_Run0089_LLKf000.1098_LLK000.1203_SupportThreshold0.29531.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-49_Run0036_LLKf000.1095_LLK000.1203_SupportThreshold0.29718.cxi] - this may take a while
R_match(0, 1) = 29.233% [8 arrays remaining]
R_match(0, 2) = 33.212% [7 arrays remaining]
R_match(0, 3) = 30.711% [6 arrays remaining]
R_match(0, 4) = 28.019% [5 arrays remaining]
R_match(0, 5) = 28.404% [4 arrays remaining]
R_match(0, 6) = 32.099% [3 arrays remaining]
R_match(0, 7) = 31.152% [2 arrays remaining]
R_match(0, 8) = 25.917% [1 arrays remaining]
R_match(0, 9) = 33.070% [0 arrays remaining]
Elapsed time:  178.3s
Analysing modes
First mode represents 95.404%
Saving modes analysis to: modes.h5
````

Weird:
S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T22-54-50_Run0021_LLKf000.1098_LLK000.1204_SupportThreshold0.29983.cxi

Flipped:
S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T22-13-50_Run0006_LLKf000.1098_LLK000.1203_SupportThreshold0.29956.cxi
S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-19-27_Run0030_LLKf000.1098_LLK000.1204_SupportThreshold0.29257.cxi
S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-27-28_Run0033_LLKf000.1098_LLK000.1203_SupportThreshold0.29950.cxi
S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-49_Run0036_LLKf000.1095_LLK000.1203_SupportThreshold0.29718.cxi
S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-35-11_Run0061_LLKf000.1098_LLK000.1205_SupportThreshold0.29505.cxi
S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-49-28_Run0079_LLKf000.1099_LLK000.1204_SupportThreshold0.29205.cxi

## Just on the results that are in the right direction :

````bash
(devel.p9) p9-01:50_Ar/S1404/pynxraw % python pynx-cdi-analysis.py S1404_pynx_norm_128_300_294_1_1_1-* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-01
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-11-13_Run0027_LLKf000.1099_LLK000.1205_SupportThreshold0.29321.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-52-21_Run0042_LLKf000.1102_LLK000.1204_SupportThreshold0.29237.cxi
Loading: S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-56-20_Run0089_LLKf000.1098_LLK000.1203_SupportThreshold0.29531.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-56-20_Run0089_LLKf000.1098_LLK000.1203_SupportThreshold0.29531.cxi] - this may take a while
R_match(0, 1) = 29.964% [1 arrays remaining]
R_match(0, 2) = 30.123% [0 arrays remaining]
Elapsed time:   50.8s
Analysing modes
First mode represents 96.970%
Saving modes analysis to: modes.h5
````

# On the flipped ones

````bash
(devel.p9) p9-01:50_Ar/S1404/pynxraw % python pynx-cdi-analysis.py flipped/S1404_pynx_norm_128_300_294_1_1_1-* modes=1--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-01
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T22-13-50_Run0006_LLKf000.1098_LLK000.1203_SupportThreshold0.29956.cxi
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-19-27_Run0030_LLKf000.1098_LLK000.1204_SupportThreshold0.29257.cxi
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-27-28_Run0033_LLKf000.1098_LLK000.1203_SupportThreshold0.29950.cxi
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-49_Run0036_LLKf000.1095_LLK000.1203_SupportThreshold0.29718.cxi
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-35-11_Run0061_LLKf000.1098_LLK000.1205_SupportThreshold0.29505.cxi
Loading: flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-13T00-49-28_Run0079_LLKf000.1099_LLK000.1204_SupportThreshold0.29205.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1404_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-49_Run0036_LLKf000.1095_LLK000.1203_SupportThreshold0.29718.cxi] - this may take a while
R_match(0, 1) = 29.233% [4 arrays remaining]
R_match(0, 2) = 28.019% [3 arrays remaining]
R_match(0, 3) = 28.404% [2 arrays remaining]
R_match(0, 4) = 31.152% [1 arrays remaining]
R_match(0, 5) = 25.917% [0 arrays remaining]
Elapsed time:  102.0s
Analysing modes
First mode represents 96.165%
Saving modes analysis to: modes.h5
````

# Running strain

````bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD_local/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw$ python strain.py 
/home/david/Documents/PhD_local/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 196 , 190 , 216 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD_local/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  43 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.017 0.643 -0.374 ) rad
Max FFT= 1312829.2889078613
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 1312829.2889078613

Shape before orthogonalization (196, 190, 216)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0072 deg, 86.84 um, 74.86 um)
New real space pixel size (z, y, x) based on actual array shape: ( 6.08  nm, 10.95 nm, 11.18 nm )
using SIXS geometry
rocking angle is mu, with beta non zero
VTK spacing : 5.00 nm
Angle between q and y = 71.79132269042893 deg
Angle with y in zy plane -45.36658787319518 deg
Angle with y in xy plane -70.76682162800394 deg
Angle with z in xz plane 109.46236623829827 deg
Normalized wavevector transfer [z, y, x]: [-0.31650317  0.31247879  0.89564655]
Wavevector transfer: (angstroms) 2.6627
Atomic plane distance: (angstroms) 2.3597 angstroms
center of mass at (z, y, x): ( 73.30 , 66.70 , 127.66 )
center of mass offset: ( 25 , 28 , -20 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.012 -0.031 -0.006 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 6.93600270837479 3.6675278395431903
phase.max() =  2.011600576043031 , at coordinates  25 176 124
/home/david/.local/lib/python3.9/site-packages/bcdi/graph/graph_utils.py:1403: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
  fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 9))
End of script
````