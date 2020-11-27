# Logbook for Pt_p2

## Preprocessing the data

`preprocess_bcdi.py` was run to define a mask for the data. The environment was LAPTOP-David, I copied the variable values from `preprocess_bcdi_sisx2019_crystalD.py`, file that lead to errors, and created a new preprocess file.

Works on id01 but not great

## Phase retrieval

 Output in \pynxraw

### `python pynx-id01cdi.py pynx-cdi-input_try0.txt` was run:

`p9-03:~/Documents/Pt_p2/pynxraw % source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate
(pynx-gap.p9) p9-03:~ % python pynx-id01cdi.py pynx-cdi-input_try0.txt 
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
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
nb_run 20
nb_run_keep 5
zero_mask False
crop_output 0
positivity False
beta 0.9
detwin False
rebin 1,1,1
detector_distance 0.84
pixel_size_detector 55e-6
wavelength 1.3775e-10
verbose 100
output_format cxi
live_plot True
Loading data:  S1398_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1398_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 1124594 pixels masked ( 9.961%)
Saving data to CXI file:  S1398_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]: Tesla V100-SXM2-32GB: 32256Mb ,1499.26 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)`


Interesting fact : he removed by himself the *.cxi* file that he told me to read, it was the last one (nb 20), probably generic,

Cannot find the environment in which I can use silx view, so I am copying the files back on my laptop.

## Create modes.h5

`python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1`

**Errors**, I tried to work in both */home/Documents* and */id01_david*, seems that there is no influence, does not work with slurm

`(pynx-gap.p9) p9-05:id01_david/Pt_p2/pynxraw % pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Traceback (most recent call last):
  File "/data/id01/inhouse/richard/pynx-gap.p9/bin/pynx-cdi-analysis.py", line 4, in <module>
    __import__('pkg_resources').run_script('PyNX==2020.2b0', 'pynx-cdi-analysis.py')
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/pkg_resources/__init__.py", line 650, in run_script
    self.require(requires)[0].run_script(script_name, ns)
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/pkg_resources/__init__.py", line 1446, in run_script
    exec(code, namespace, namespace)
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/EGG-INFO/scripts/pynx-cdi-analysis.py", line 22, in <module>
    from pynx.cdi.cl_operator import PRTF
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/cdi/cl_operator.py", line 20, in <module>
    from ..processing_unit.cl_processing_unit import CLProcessingUnit
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/processing_unit/cl_processing_unit.py", line 38, in <module>
    class CLEvent(object):
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/processing_unit/cl_processing_unit.py", line 44, in CLEvent
    def __init__(self, event: cl.Event, nflop: int = 0, nbyte: int = 0):
NameError: name 'cl' is not defined
(pynx-gap.p9) p9-05:id01_david/Pt_p2/pynxraw %`


`p9-05:~/Documents/Pt_p2/pynxraw % source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate
(pynx-gap.p9) p9-05:~/Documents/Pt_p2/pynxraw % ls
finalmask_S1398_norm_128_300_294_1_1_1.png
finalsum_S1398_norm_128_300_294_1_1_1.png
pynx-cdi-analysis.py
pynx-cdi-input_try0.txt
pynx-id01cdi.py
S1398_maskpynx_norm_128_300_294_1_1_1.npz
S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-51-52_Run0013_LLKf000.1687_LLK4388551712.0361_SupportThreshold0.12811.cxi
S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-52-43_Run0014_LLKf000.1607_LLK4597681164.7415_SupportThreshold0.13668.cxi
S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-55-33_Run0017_LLKf000.1524_LLK4391592741.0126_SupportThreshold0.13151.cxi
S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-56-24_Run0018_LLKf000.1879_LLK4452517032.6233_SupportThreshold0.12824.cxi
S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-57-15_Run0019_LLKf000.1579_LLK4392738938.3316_SupportThreshold0.12829.cxi
S1398_pynx_norm_128_300_294_1_1_1.cxi
S1398_pynx_norm_128_300_294_1_1_1.npz
strain.py
(pynx-gap.p9) p9-05:~/Documents/Pt_p2/pynxraw % python pynx-cdi-analysis.py 
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Traceback (most recent call last):
  File "pynx-cdi-analysis.py", line 25, in <module>
    from pynx.cdi.cu_operator import PRTF
ImportError: cannot import name 'PRTF' from 'pynx.cdi.cu_operator' (/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/cdi/cu_operator.py)
(pynx-gap.p9) p9-05:~/Documents/Pt_p2/pynxraw % python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Traceback (most recent call last):
  File "pynx-cdi-analysis.py", line 25, in <module>
    from pynx.cdi.cu_operator import PRTF
ImportError: cannot import name 'PRTF' from 'pynx.cdi.cu_operator' (/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/cdi/cu_operator.py)`

**Works on lid01:**

`cd /data/id01/inhouse/david/Pt_p2`

`Matching arrays against the first one [S1398_pynx_norm_128_300_294_1_1_1-2020-11-26T15-55-33_Run0017_LLKf000.1524_LLK4391592741.0126_SupportThreshold0.13151.cxi] - this may take a while
R_match(0, 1) = 77.933% [3 arrays remaining]
R_match(0, 2) = 79.114% [2 arrays remaining]
R_match(0, 3) = 76.972% [1 arrays remaining]
R_match(0, 4) = 83.713% [0 arrays remaining]
Elapsed time:   47.9s
Analysing modes
First mode represents 74.860%
Saving modes analysis to: modes.h5`

### Silx view sort of works on id01

`(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ silx view modes.h5`

## Strain analysis

Did not work ar first:

`simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python strain.py 
Traceback (most recent call last):
  File "strain.py", line 201, in <module>
    root = tk.Tk()
  File "/usr/lib/python3.5/tkinter/__init__.py", line 1880, in __init__
    self.tk = _tkinter.create(screenName, baseName, className, interactive, wantobjects, useTk, sync, use)
_tkinter.TclError: no display name and no $DISPLAY environment variable
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw`

**Pareil sur rnice9, almost works on laptop environment. Just one error :**

`    Directory: D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2\pynxraw
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
Traceback (most recent call last):
  File ".\strain.py", line 316, in <module>
    phase = pu.remove_offset(array=phase, support=support, offset_method=offset_method, user_offset=phase_offset,
AttributeError: module 'bcdi.postprocessing.postprocessing_utils' has no attribute 'remove_offset'
PS D:\Documents\PythonScripts\PhDLocalScripts\Pt_p2\pynxraw>`

L'erreur pop après que les 3 premières fenêtres se soient ouvertes

### Nouvel essai le lendemain sur lid01

  *Sur lid01, il n'arrive pas à trouver le fichier, bizarre car il se lance alors que c'est exactement les mêmes commandes que hier
  *Ensuite il trouve le fichier, c'est de la magie

**Question :** Les fichiers blackman tout ça sont ils les mêmes pour chaque scan ? d'où viennent-ils ?

Seems to work but voxel size becomes zero ? What are all these figures Had toc hange directory to ./

`(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ python strain.py 
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 200 , 178 , 192 )
Averaging using 1 candidate reconstructions
Opening  /mntdirect/_data_id01_inhouse/david/Pt_p2/pynxraw/modes.h5
This reconstruction will serve as reference object.
Average performed over  1 reconstructions
Extent of the phase over an extended support (ceil(phase range))~  51 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.007 0.566 -0.345 ) rad
Max FFT= 1496427.1226652777
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 1496427.1226652777
Shape before orthogonalization (200, 178, 192)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 9.03 nm, 10.97 nm, 12.10 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0070 deg, 92.70 um, 84.22 um)
Sanity check, recalculated direct space voxel sizes: ( 9.03  nm, 10.97 nm, 12.10 nm )
using SIXS geometry
rocking angle is mu, with beta non zero
VTK spacing : 0.00 nm
Angle between q and y = 71.79132269042893 deg
Angle with y in zy plane -45.36658787319517 deg
Angle with y in xy plane -70.76682162800394 deg
Angle with z in xz plane 109.46236623829827 deg
Normalized wavevector transfer [z, y, x]: [-0.31650317  0.31247879  0.89564655]
Wavevector transfer: (angstroms) 2.7268
Atomic plane distance: (angstroms) 2.3042 angstroms
center of mass at (z, y, x): ( 99.50 , 88.50 , 95.50 )
center of mass offset: ( 1 , 1 , 1 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.000 0.000 0.000 ) rad
Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  0.00 nm
Final data shape: 200 200 200
/mntdirect/_data_id01_inhouse/richard/bcdiDevel.debian9/lib/python3.5/site-packages/vtk/util/numpy_support.py:137: FutureWarning: Conversion of the second argument of issubdtype from `complex` to `np.complexfloating` is deprecated. In future, it will be treated as `np.complex128 == np.dtype(complex).type`.
  assert not numpy.issubdtype(z.dtype, complex), \
Traceback (most recent call last):
  File "strain.py", line 689, in <module>
    pixel_spacing = tick_spacing / voxel_size
ZeroDivisionError: division by zero
(bcdiDevel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/Pt_p2/pynxraw$ `