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


### Silx view sort of works on id01, but better on my laptop (rnice ?)

````bash
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ silx view modes.h5
````

## Strain analysis

**Did not work at all at first on lid01 or rnice9:**

strain flip = False

````bash
simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python strain.py 
````
````python
Traceback (most recent call last):
  File "strain.py", line 201, in <module>
    root = tk.Tk()
  File "/usr/lib/python3.5/tkinter/__init__.py", line 1880, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
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

**Nouvel essai sur lid01**

* Sur lid01, il n'arrive pas à trouver le fichier, bizarre car il se lance alors que c'est exactement les mêmes commandes que hier
* (EDIT) Ensuite il trouve le fichier, c'est de la magie, je crois qu'il faut avoir executé strain et analysis dans la meme session.

**Question :** Les fichiers blackman tout ça sont ils les mêmes pour chaque scan (surement car juste filtre) ? D'où viennent-ils ?

Seems to work now (no idea why) but voxel size becomes zero ? What are all these figures ?
(erreur humaine a l'origine ><)

````bash
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python strain.py 
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 194 , 178 , 196 )

Averaging using 1 candidate reconstructions

Opening  /mntdirect/_data_id01_inhouse/david/Pt_p2/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  47 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.014 0.577 -0.346 ) rad
Max FFT= 1446641.0422051493
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 1446641.0422051493

Shape before orthogonalization (194, 178, 196)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 9.03 nm, 10.97 nm, 12.10 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0073 deg, 92.70 um, 82.50 um)
Sanity check, recalculated direct space voxel sizes: ( 9.03  nm, 10.97 nm, 12.10 nm )
using SIXS geometry
rocking angle is mu, with beta non zero
VTK spacing : 5.00 nm
Angle between q and y = 71.79132269042893 deg
Angle with y in zy plane -45.36658787319517 deg
Angle with y in xy plane -70.76682162800394 deg
Angle with z in xz plane 109.46236623829827 deg
Normalized wavevector transfer [z, y, x]: [-0.31650317  0.31247879  0.89564655]
Wavevector transfer: (angstroms) 2.7268
Atomic plane distance: (angstroms) 2.3042 angstroms
center of mass at (z, y, x): ( 94.72 , 92.12 , 104.71 )
center of mass offset: ( 2 , -3 , -7 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.002 -0.005 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
/mntdirect/_data_id01_inhouse/richard/bcdiDevel.debian9/lib/python3.5/site-packages/vtk/util/numpy_support.py:137: FutureWarning: Conversion of the second argument of issubdtype from `complex` to `np.complexfloating` is deprecated. In future, it will be treated as `np.complex128 == np.dtype(complex).type`.
  assert not numpy.issubdtype(z.dtype, complex), \
Phase extent before and after thresholding: 7.587438232427344 2.2128061129682015
phase.max() =  1.1387100144463769 , at coordinates  127 81 17
/mntdirect/_data_id01_inhouse/richard/bcdiDevel.debian9/lib/python3.5/site-packages/matplotlib/pyplot.py:514: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
  max_open_warning, RuntimeWarning)
End of script
````
