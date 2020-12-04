# Logbook for Pt_p2

# Preprocessing the data

`preprocess_bcdi.py` was run to define a mask for the data. The environment was LAPTOP-David, I copied the variable values from `preprocess_bcdi_sisx2019_crystalD.py`, file that lead to errors, and created a new preprocess file.

Almost work on id01, but I cannot mask (no mask created when I press m, all other letters binded to commands work).

````bash
PS D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2> python .\preprocess_bcdi.py
homedir : ./
root_folder : ./
File has time stamps issues
File has time stamps issues

Scan 1398
Setup:  SIXS_2019
Detector:  Maxipix
Pixel number (VxH):  516 516
Detector ROI: [0, 303, 0, 296]
Horizontal pixel size with binning:  5.5e-05 m
Vertical pixel size with binning:  5.5e-05 m
Specfile:  ./analysis/alias_dict.txt
Scan type:  inplane
Output will be non orthogonal, in the detector frame
Detector ROI loaded (VxH): 303 296
Detector physical size without binning (VxH): 516 516
Detector size with binning (VxH): 516 516
Loading frame 129
check_pixels(): initial number of masked pixels = 3966 on a total of 89688
check_pixels(): var_mean=57.05, 1/var_threshold=132.65
check_pixels(): number of zero variance hotpixels = 0
check_pixels(): number of pixels with too low variance = 0

0  negative data points masked
Intensity normalization using monitor
Monitor min, max, mean: 0.0, 0.0, 0.0
Data normalization by monitor.min()/monitor


Input data shape: 129 303 296
Max at (qx, qz, qy):  64 178 132
Data peak value =  40088.21768417889
Max symmetrical box (qx, qz, qy):  128 250 264
FFT box (qx, qz, qy):  (128, 300, 294)

Pad width: [0 0 0 0 0 0]

Data size after cropping / padding: 128 300 294

Skipping median filtering

Data size after masking: 128 300 294

Data size after binning the stacking dimension: (128, 300, 294)

Saving directory: ./pynxraw/

End of script
PS D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2>
````

# Phase retrieval

## Running pynx

* lid01 environment
* Input energy (from MU preprocess file) = 8300 eV, changing lambda to 1.24 Angström in `pynx-cdi-input_try0.txt`.
* Garder 10 de 100, creer support avec threshold 25% -> fichier .npz

````bash
>>> he
4.141249999999999e-15
>>> c
300000000
>>> l = he*c/10000
>>> l
1.2423749999999998e-10
>>>
````

````bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python pynx-id01cdi.py pynx-cdi-input_try0.txt
Using parameters file:  pynx-cdi-input_try0.txt
data S1398_pynx_norm_128_300_294_1_1_1.npz
mask S1398_maskpynx_norm_128_300_294_1_1_1.npz
data2cxi True
auto_center_resize False
support_threshold 0.1,0.2
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

Loading data:  S1398_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1398_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
^C                                         GeForce GTX TITAN X: 12212Mb ,   0.00 Gflop/s
Searching available OpenCL GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                           GeForce GTX TITAN X [NVIDIA CUDA]: 12212Mb [max alloc.: 3053Mb], 237.92 Gflop/s
Ignoring Portable Computing Language (POCL) platform by default
Using OpenCL GPU: GeForce GTX TITAN X
Loading mask from:  S1398_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 927808 pixels masked ( 8.218%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
#################################################################################################### 
# 
#  CDI Run: 100/100
#
 ####################################################################################################
Finished initializing object 
Using auto-correlation to estimate initial support, relative threshold = 0.100
Set free mask with 543201 pixels ( 4.812%)
Interpolating masked pixels with InterpIobsMask(8, 2)
No algorithm chain supplied. Proceeding with the following parameters:
                         nb_hio =  400
                        nb_raar =  1000
                          nb_er =  300
                          nb_ml =  0
                     positivity =  False
            support_only_shrink =  False
                           beta =  0.9
                         detwin =  False
                      live_plot =  0
          support_update_period =  20
     support_smooth_width_begin =  2.0
       support_smooth_width_end =  1.0
              support_threshold =  0.10201561015908664
       support_threshold_method =  rms
            support_post_expand =  (1, -2, 1)
 confidence_interval_factor_mask_min =  0.5
 confidence_interval_factor_mask_max =  1.2
                      zero_mask =  False
                        verbose =  100
Algorithm chain:  (Sup*ER**20)**2 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**32 * (Sup*HIO**20)**20
````
## Create modes.h5

````bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
Importing data files
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-44-11_Run0019_LLKf000.1524_LLK4828897416.5916_SupportThreshold0.14254.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-44-45_Run0020_LLKf000.1371_LLK5106613636.0168_SupportThreshold0.10094.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-45-51_Run0022_LLKf000.1473_LLK4969885945.3201_SupportThreshold0.14390.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-54-34_Run0037_LLKf000.1530_LLK4964432716.3696_SupportThreshold0.10306.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-56-16_Run0040_LLKf000.1437_LLK4936279356.4796_SupportThreshold0.13960.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-59-36_Run0046_LLKf000.1456_LLK4796542525.2914_SupportThreshold0.14391.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T11-01-14_Run0049_LLKf000.1443_LLK5064797401.4282_SupportThreshold0.14046.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T11-05-30_Run0057_LLKf000.1454_LLK5000520944.5953_SupportThreshold0.10299.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T11-08-14_Run0062_LLKf000.1495_LLK5079728960.9909_SupportThreshold0.14758.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T11-13-50_Run0073_LLKf000.1539_LLK4811616539.9551_SupportThreshold0.10281.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1398_pynx_norm_128_300_294_1_1_1-2020-12-03T10-44-45_Run0020_LLKf000.1371_LLK5106613636.0168_SupportThreshold0.10094.cxi] - this may take a while
R_match(0, 1) = 73.178% [8 arrays remaining]
R_match(0, 2) = 80.152% [7 arrays remaining]
R_match(0, 3) = 75.265% [6 arrays remaining]
R_match(0, 4) = 66.872% [5 arrays remaining]
R_match(0, 5) = 76.427% [4 arrays remaining]
R_match(0, 6) = 79.603% [3 arrays remaining]
R_match(0, 7) = 82.065% [2 arrays remaining]
R_match(0, 8) = 79.596% [1 arrays remaining]
R_match(0, 9) = 76.035% [0 arrays remaining]
Elapsed time:  107.3s
Analysing modes
First mode represents 70.847%
Saving modes analysis to: modes.h5
````
Not so good

## Then I try to create a new support by using an average of the support determined by the program from the last run.

It worked, it is the file Mask_10_100_0_1.npz, looks a bit rough on the edges though.

````bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python pynx-id01cdi.py pynx-cdi-input_try0.txt
Using parameters file:  pynx-cdi-input_try0.txt
data S1398_pynx_norm_128_300_294_1_1_1.npz
mask S1398_maskpynx_norm_128_300_294_1_1_1.npz
data2cxi True
auto_center_resize False
support Mask_10_100_0_1.npz
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

Loading data:  S1398_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1398_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                         GeForce GTX TITAN X: 12212Mb , 453.16 Gflop/s
Searching available OpenCL GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                           GeForce GTX TITAN X [NVIDIA CUDA]: 12212Mb [max alloc.: 3053Mb], 247.08 Gflop/s
Ignoring Portable Computing Language (POCL) platform by default
Using CUDA GPU: GeForce GTX TITAN X
Loading mask from:  S1398_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 927808 pixels masked ( 8.218%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
Loading support from:  Mask_10_100_0_1.npz
Initialized support  (128, 300, 294) , with 84988 pixels ( 0.753%)
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
 #################################################################################################### 
# 
#  CDI Run: 100/100
#
 ####################################################################################################
Finished initializing object 
Set free mask with 546968 pixels ( 4.845%)
Interpolating masked pixels with InterpIobsMask(8, 2)
No algorithm chain supplied. Proceeding with the following parameters:
                         nb_hio =  400
                        nb_raar =  1000
                          nb_er =  300
                          nb_ml =  0
                     positivity =  False
            support_only_shrink =  False
                           beta =  0.9
                         detwin =  False
                      live_plot =  0
          support_update_period =  20
     support_smooth_width_begin =  2.0
       support_smooth_width_end =  1.0
              support_threshold =  0.254352891562228
       support_threshold_method =  rms
            support_post_expand =  (1, -2, 1)
 confidence_interval_factor_mask_min =  0.5
 confidence_interval_factor_mask_max =  1.2
                      zero_mask =  False
                        verbose =  100
Algorithm chain:  (Sup*ER**20)**2 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**32 * (Sup*HIO**20)**20
````

## Create modes.h5 again

````bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
Importing data files
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-25-40_Run0008_LLKf000.1159_LLK000.1328_SupportThreshold0.29541.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-26-53_Run0010_LLKf000.1158_LLK000.1330_SupportThreshold0.29706.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-37-13_Run0027_LLKf000.1157_LLK000.1329_SupportThreshold0.29221.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-39-39_Run0031_LLKf000.1158_LLK000.1330_SupportThreshold0.28916.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-41-28_Run0034_LLKf000.1158_LLK000.1332_SupportThreshold0.28754.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-44-30_Run0039_LLKf000.1158_LLK000.1330_SupportThreshold0.29166.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-47-34_Run0044_LLKf000.1158_LLK000.1329_SupportThreshold0.29538.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-59-06_Run0063_LLKf000.1155_LLK000.1329_SupportThreshold0.29807.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T20-14-50_Run0089_LLKf000.1156_LLK000.1331_SupportThreshold0.29090.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T20-18-28_Run0095_LLKf000.1159_LLK000.1332_SupportThreshold0.28434.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1398_pynx_norm_128_300_294_1_1_1-2020-12-04T19-59-06_Run0063_LLKf000.1155_LLK000.1329_SupportThreshold0.29807.cxi] - this may take a while
R_match(0, 1) = 30.332% [8 arrays remaining]
R_match(0, 2) = 28.736% [7 arrays remaining]
R_match(0, 3) = 33.285% [6 arrays remaining]
R_match(0, 4) = 37.631% [5 arrays remaining]
R_match(0, 5) = 28.119% [4 arrays remaining]
R_match(0, 6) = 37.937% [3 arrays remaining]
R_match(0, 7) = 29.123% [2 arrays remaining]
R_match(0, 8) = 28.070% [1 arrays remaining]
R_match(0, 9) = 30.672% [0 arrays remaining]
Elapsed time:  108.2s
Analysing modes
First mode represents 94.530%
Saving modes analysis to: modes.h5
````
Better I guess ?

### Silx works on rnice, better on laptop

````bash
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ silx view modes.h5
````

## Strain analysis

**Did not work at all at first on lid01 or rnice9:**

strain flip = False

````bash
simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python strain.py
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 190 , 198 , 194 )

Averaging using 1 candidate reconstructions

Opening  /mntdirect/_data_id01_inhouse/david/Pt_p2/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  65 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.001 0.492 -0.312 ) rad
Max FFT= 2305565.585629071
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 2305565.5856290716

Shape before orthogonalization (190, 198, 194)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 9.25 nm, 11.24 nm, 12.39 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0074 deg, 83.33 um, 83.35 um)
Sanity check, recalculated direct space voxel sizes: ( 9.25  nm, 11.24 nm, 12.39 nm )
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
center of mass at (z, y, x): ( 88.46 , 130.85 , 82.49 )
center of mass offset: ( 7 , -32 , 15 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.016 0.030 0.002 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
/mntdirect/_data_id01_inhouse/richard/bcdiDevel.debian9/lib/python3.5/site-packages/vtk/util/numpy_support.py:137: FutureWarning: Conversion of the second argument of issubdtype from `complex` to `np.complexfloating` is deprecated. In future, it will be treated as `np.complex128 == np.dtype(complex).type`.
  assert not numpy.issubdtype(z.dtype, complex), \
Phase extent before and after thresholding: 13.222435415222712 3.7654175076326446
phase.max() =  1.6250838106795826 , at coordinates  157 136 177
End of script
````

**Almost works on laptop environment. Just one error :**
Directory: D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2\pynxraw

````bash
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        11/26/2020   3:08 PM          86034 finalmask_S1398_norm_128_300_294_1_1_1.png
-a----        11/26/2020   3:08 PM         436766 finalsum_S1398_norm_128_300_294_1_1_1.png
-a----        11/26/2020   5:17 PM       79110712 modes.h5
-a----        11/26/2020   1:44 PM          19961 pynx-cdi-analysis.py
-a----        11/26/2020   3:38 PM           1495 pynx-cdi-input_try0.txt
-a----         11/5/2020  12:05 PM            767 pynx-id01cdi.py
-a----        11/26/2020   3:08 PM         371448 S1398_maskpynx_norm_128_300_294_1_1_1.npz
-a----        11/26/2020   3:52 PM       79888171 S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-51-52_Run0013_LLKf000
                                                  .1687_LLK4388551712.0361_SupportThreshold0.12811.cxi
-a----        11/26/2020   3:53 PM       79696192 S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-52-43_Run0014_LLKf000
                                                  .1607_LLK4597681164.7415_SupportThreshold0.13668.cxi
-a----        11/26/2020   3:56 PM       79847367 S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-55-33_Run0017_LLKf000
                                                  .1524_LLK4391592741.0126_SupportThreshold0.13151.cxi
-a----        11/26/2020   3:57 PM       79910077 S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-56-24_Run0018_LLKf000
                                                  .1879_LLK4452517032.6233_SupportThreshold0.12824.cxi
-a----        11/26/2020   3:58 PM       79830294 S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-57-15_Run0019_LLKf000
                                                  .1579_LLK4392738938.3316_SupportThreshold0.12829.cxi
-a----        11/26/2020   3:41 PM        2508560 S1398_pynx_norm_128_300_294_1_1_1.cxi
-a----        11/26/2020   3:08 PM         959117 S1398_pynx_norm_128_300_294_1_1_1.npz
-a----        11/27/2020   9:57 AM          39200 strain.py
PS D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2\pynxraw> python .\strain.py
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 200 , 178 , 192 )
Averaging using 1 candidate reconstructions
Opening  D:/Documents/PythonScripts/PhDLocalScripts/Pt_p2/pynxraw/modes.h5
This reconstruction will serve as reference object.
Average performed over  1 reconstructions
Extent of the phase over an extended support (ceil(phase range))~  51 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.007 0.566 -0.345 ) rad
````
````python
Traceback (most recent call last):
  File ".\strain.py", line 316, in <module>
    phase = pu.remove_offset(array=phase, support=support, offset_method=offset_method, user_offset=phase_offset,
AttributeError: module 'bcdi.postprocessing.postprocessing_utils' has no attribute 'remove_offset'
````

L'erreur pop après que les 3 premières fenêtres se soient ouvertes, surement un pb de versions ?