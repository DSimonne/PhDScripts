# Preprocessing

```bash
(linux.BCDI_MI) david@pc-momonne:~/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3$ python Scripts/preprocess_bcdi_local_merlin.py NoGas 1337
Total number of arguments: 3
Argument List: ['Scripts/preprocess_bcdi_local_merlin.py', 'NoGas', '1337']
Scan (s): 1337
Data dir: NoGas
Output will be non orthogonal, in the detector frame

##############
Setup instance
##############
Setup(beamline='SIXS_2019', beam_direction=[1. 0. 0.], energy=8500, distance=1.18, outofplane_angle=None,
inplane_angle=None, tilt_angle=None, rocking_angle='inplane', grazing_angle=None, pixel_x=5.5e-05,
pixel_y=5.5e-05, direct_beam=None, sample_offsets=(0, 0, 0), filtered_data=False, custom_scan=False,
custom_images=None,
custom_monitor=None,
custom_motors=None,
sample_inplane=(1, 0, 0), sample_outofplane=(0, 0, 1), offset_inplane=0)

#################
Detector instance
#################
Detector(name='Merlin', unbinned_pixel=(5.5e-05, 5.5e-05), nb_pixel_x=515, nb_pixel_y=515, binning=(1, 1, 1),
roi=[0, 515, 0, 515], sum_roi=[0, 515, 0, 515], preprocessing_binning=(1, 1, 1), is_series=False
rootdir = None,
datadir = None,
scandir = None,
savedir = None,
sample_name = None, template_file = None, template_imagefile = Pt_Al2O3_ascan_mu_%05d_R.nxs, specfile = None,


###############
Scan 1/1: S1337
###############
datadir = '/home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/data/'
savedir = '/home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/pynxraw/'
template_imagefile = 'Pt_Al2O3_ascan_mu_%05d_R.nxs'

### ReadNxs3 ###
### End of ReadNxs3 ###

User-defined ROI size (VxH): 515 515
Detector physical size without binning (VxH): 515 515
Detector size with binning (VxH): 515 515
Loading frame 201
check_pixels(): number of masked pixels due to detector gaps = 21471 on a total of 265225
check_pixels(): var_mean=100.91, 1/var_threshold=206.11
check_pixels(): number of zero variance hotpixels = 0
check_pixels(): number of pixels with too low variance = 0

0  negative data points masked
Skip intensity normalization

Input data shape: 201 515 515
Max at pixel (Z, Y, X):  100 372 188
Data peak value = 85801.0
Max symmetrical box (qx, qz, qy):  200 286 376
FFT box (qx, qz, qy):  (200, 280, 360)

Pad width: [0 0 0 0 0 0]

Data size after cropping / padding: 200 280 360

Skipping median filtering

Data size after masking: 200 280 360

Data size after binning the stacking dimension: (200, 280, 360)

Saving directory: /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/pynxraw/
Data type before saving: float64
Mask type before saving: int64

End of script
```


# Phase retrieval

```bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/SIXS_Jan/Pt_Al2O3/Ar/S1373/pynxraw$ pynx-id01cdi.py pynx-run-no-support.txt 
Using parameters file:  pynx-run-no-support.txt
data S1373_pynx_norm_192_288_392_1_1_1.npz
mask S1373_maskpynx_norm_192_288_392_1_1_1.npz
data2cxi True
auto_center_resize False
support_threshold 0.23, 0.3
support_only_shrink False
support_update_period 20
support_smooth_width_begin 2
support_smooth_width_end 1
support_post_expand 1,-2,1
psf True
nb_raar 1000
nb_hio 400
nb_er 300
nb_ml 0
nb_run 50
nb_run_keep 10
zero_mask auto
crop_output 0
positivity False
beta 0.9
detwin False
rebin 1,1,1
detector_distance 1.18
pixel_size_detector 55e-6
wavelength 0.14586e-9
verbose 100
output_format cxi
live_plot False

Loading data:  S1373_pynx_norm_192_288_392_1_1_1.npz
Finished loading iobs data, with size: 21676032
Data CXI file already exists, not overwriting:  S1373_pynx_norm_192_288_392_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                         GeForce GTX TITAN X:   11 Gb,   242 Gbytes/s
Using CUDA GPU: GeForce GTX TITAN X
Loading mask from:  S1373_maskpynx_norm_192_288_392_1_1_1.npz
Initialized mask, with 1471642 pixels masked ( 6.789%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (192, 288, 392) -> (192, 288, 392)

 #################################################################################################### 
# 
#  CDI Run: 1/50
#
 ####################################################################################################
Finished initializing object 
Using auto-correlation to estimate initial support, relative threshold = 0.100
Initialized free mask with 1066933 pixels ( 4.922%)
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
              support_threshold =  0.24708077651450847
       support_threshold_method =  rms
            support_post_expand =  (1, -2, 1)
 confidence_interval_factor_mask_min =  0.5
 confidence_interval_factor_mask_max =  1.2
                      zero_mask =  auto
                        verbose =  100
Switching from zero_mask=1 to 0 after 840 cycles
Algorithm chain:  (Sup*ER**20)**2 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*ER**20 * Sup*ER**20 * Sup*ER**10 * PSF**100*ER**10 * (Sup*ER**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**2 * PSF**100*Sup*RAAR**20 * Sup*RAAR**20 * Sup*RAAR**10 * PSF**100*RAAR**10 * (Sup*RAAR**20)**32 * (Sup*HIO**20)**20
 HIO #  0 LLK=   18.161[   1.379](p)    1.437[   0.161](g)    5.829[   0.718](e), nb photons=1.495578e+05, support:nb=100637 ( 0.464%) average=      1.22 max=      0.00, dt/cycle=0.3010s 
 HIO #100 LLK=    1.560[   0.139](p)   27.882[   0.055](g)    3.565[   0.160](e), nb photons=4.066202e+07, support:nb=1131364 ( 5.219%) average=      6.00 max=     68.69, dt/cycle=0.0171s 
 HIO #200 LLK=    1.027[   0.113](p)    7.891[   0.057](g)    2.488[   0.168](e), nb photons=3.644780e+07, support:nb=2003450 ( 9.243%) average=      4.27 max=     80.22, dt/cycle=0.0171s 
 HIO #300 LLK=    0.932[   0.111](p)    5.885[   0.063](g)    2.433[   0.189](e), nb photons=3.569414e+07, support:nb=3407850 (15.722%) average=      3.24 max=     76.33, dt/cycle=0.0171s 
RAAR #400 LLK=    1.126[   0.118](p)    8.459[   0.058](g)    2.915[   0.172](e), nb photons=3.846718e+07, support:nb=1860761 ( 8.584%) average=      4.55 max=     78.17, dt/cycle=0.0185s 
RAAR #500 LLK=    0.751[   0.146](p)   24.254[   0.040](g)    1.529[   0.136](e), nb photons=3.162668e+07, support:nb= 84536 ( 0.390%) average=     19.34 max=     79.67, dt/cycle=0.0171s 
RAAR #600 LLK=    0.794[   0.155](p)   25.101[   0.047](g)    1.641[   0.149](e), nb photons=3.189804e+07, support:nb= 75943 ( 0.350%) average=     20.49 max=     60.39, dt/cycle=0.0172s 
RAAR #700 LLK=    0.793[   0.153](p)   24.720[   0.043](g)    1.639[   0.143](e), nb photons=3.190171e+07, support:nb= 74796 ( 0.345%) average=     20.65 max=     64.15, dt/cycle=0.0172s 
RAAR #800 LLK=    0.791[   0.155](p)   21.581[   0.044](g)    1.632[   0.147](e), nb photons=3.183849e+07, support:nb= 74221 ( 0.342%) average=     20.71 max=     63.33, dt/cycle=0.0172s 
RAAR #900 LLK=    0.809[   0.155](p)   25.787[   0.046](g)    1.685[   0.149](e), nb photons=3.201324e+07, support:nb= 72949 ( 0.337%) average=     20.95 max=     62.10, dt/cycle=0.0172s 
RAAR #1000 LLK=    0.800[   0.148](p)   23.963[   0.043](g)    1.668[   0.144](e), nb photons=3.199610e+07, support:nb= 73919 ( 0.341%) average=     20.81 max=     64.39, dt/cycle=0.0172s 
RAAR #1100 LLK=    0.214[   0.100](p)    0.607[   0.094](g)    0.613[   0.278](e), nb photons=3.377888e+07, support:nb= 88662 ( 0.409%) average=     19.52 max=     52.80, dt/cycle=0.0479s [PSF]
RAAR #1200 LLK=    0.150[   0.085](p)    0.311[   0.059](g)    0.416[   0.202](e), nb photons=2.933089e+07, support:nb= 77312 ( 0.357%) average=     19.48 max=     47.34, dt/cycle=0.0416s [PSF]
RAAR #1300 LLK=    0.153[   0.086](p)    0.309[   0.059](g)    0.424[   0.203](e), nb photons=2.913921e+07, support:nb= 74145 ( 0.342%) average=     19.82 max=     46.22, dt/cycle=0.0416s [PSF]
  ER #1400 LLK=    0.158[   0.087](p)    0.322[   0.061](g)    0.439[   0.207](e), nb photons=2.917516e+07, support:nb= 72686 ( 0.335%) average=     20.03 max=     46.80, dt/cycle=0.0430s [PSF]
  ER #1500 LLK=    0.103[   0.076](p)    0.090[   0.045](g)    0.170[   0.122](e), nb photons=2.778543e+07, support:nb= 59263 ( 0.273%) average=     21.65 max=     51.79, dt/cycle=0.0395s [PSF]
  ER #1600 LLK=    0.107[   0.077](p)    0.103[   0.049](g)    0.183[   0.128](e), nb photons=2.768222e+07, support:nb= 53992 ( 0.249%) average=     22.64 max=     52.58, dt/cycle=0.0395s [PSF]

Total elapsed time for algorithms:    46.09s
Estimated memory throughput of algorithms (not counting PSF update):
          HIO**400 [dt=  7.0s  <dt/cycle>=0.0174s]:  171.4 Gbytes/s
         RAAR**601 [dt= 10.3s  <dt/cycle>=0.0171s]:  174.6 Gbytes/s
     RAAR[PSF]**399 [dt= 17.4s  <dt/cycle>=0.0436s]:  103.6 Gbytes/s
      ER[PSF]**201 [dt=  7.9s  <dt/cycle>=0.0393s]:  106.9 Gbytes/s
           ER** 99 [dt=  3.2s  <dt/cycle>=0.0325s]:   81.9 Gbytes/s
Saving result to: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T15-46-21_Run0001_LLKf000.0782_LLK000.1113_SupportThreshold0.24708.cxi
To view the result file (HDF5/CXI or npz), use: silx view S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T15-46-21_Run0001_LLKf000.0782_LLK000.1113_SupportThreshold0.24708.cxi
```

# Modes analysis 

```bash
(devel.debian9) simonne@lid01gpu1:/data/id01/inhouse/david/SIXS_Jan/Pt_Al2O3/Ar/S1373/pynxraw$ pynx-cdi-analysis.py *LLK* modes=1
Importing data files
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T15-47-22_Run0002_LLKf000.0720_LLK000.0937_SupportThreshold0.25035.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T15-56-19_Run0012_LLKf000.0721_LLK000.0939_SupportThreshold0.24679.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T15-59-06_Run0015_LLKf000.0720_LLK000.0936_SupportThreshold0.24380.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-03-32_Run0020_LLKf000.0719_LLK000.0935_SupportThreshold0.23925.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-06-08_Run0023_LLKf000.0721_LLK000.0941_SupportThreshold0.24992.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-11-38_Run0029_LLKf000.0718_LLK000.0935_SupportThreshold0.24235.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-12-31_Run0030_LLKf000.0720_LLK000.0936_SupportThreshold0.24164.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-14-19_Run0032_LLKf000.0718_LLK000.0946_SupportThreshold0.26414.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-19-42_Run0038_LLKf000.0718_LLK000.0933_SupportThreshold0.24021.cxi
Loading: S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-20-34_Run0039_LLKf000.0720_LLK000.0938_SupportThreshold0.25474.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1373_pynx_norm_192_288_392_1_1_1-2021-02-17T16-14-19_Run0032_LLKf000.0718_LLK000.0946_SupportThreshold0.26414.cxi] - this may take a while
R_match(0, 1) = 23.767% [8 arrays remaining]
R_match(0, 2) = 20.595% [7 arrays remaining]
R_match(0, 3) = 22.422% [6 arrays remaining]
R_match(0, 4) = 24.476% [5 arrays remaining]
R_match(0, 5) = 21.787% [4 arrays remaining]
R_match(0, 6) = 20.875% [3 arrays remaining]
R_match(0, 7) = 24.677% [2 arrays remaining]
R_match(0, 8) = 19.960% [1 arrays remaining]
R_match(0, 9) = 22.448% [0 arrays remaining]
Elapsed time:  219.4s
Analysing modes
First mode represents 97.881%
Saving modes analysis to: modes.h5
```

# Strain plotting

```bash
(linux.BCDI_MI) david@pc-momonne:~/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3$ python Scripts/strain-SIXS_local_merlin.py Ar 1373
Scan (s): 1373
Data dir: Ar
### ReadNxs3 ###
### End of ReadNxs3 ###

#########
Scan 1373
#########

##############
Setup instance
##############
Setup(beamline='SIXS_2019', beam_direction=[1. 0. 0.], energy=8500, distance=1.18, outofplane_angle=0.326,
inplane_angle=37.938, tilt_angle=0.005, rocking_angle='inplane', grazing_angle=(0, 0), pixel_x=5.5e-05,
pixel_y=5.5e-05, direct_beam=None, sample_offsets=(0, 0, 0), filtered_data=False, custom_scan=False,
custom_images=None,
custom_monitor=None,
custom_motors=None,
sample_inplane=(1, 0, 0), sample_outofplane=(0, 0, 1), offset_inplane=0)

#################
Detector instance
#################
Detector(name='Merlin', unbinned_pixel=(5.5e-05, 5.5e-05), nb_pixel_x=515, nb_pixel_y=515, binning=(1, 1, 1),
roi=[0, 515, 0, 515], sum_roi=[0, 515, 0, 515], preprocessing_binning=(1, 1, 1), is_series=False
rootdir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/Ar/,
datadir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/Ar/S1373/data/,
scandir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/Ar/S1373/,
savedir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/Ar/S1373/result/,
sample_name = S, template_file = Pt_Al2O3_ascan_mu_%05d_R.nxs, template_imagefile = Pt_Al2O3_ascan_mu_%05d_R.nxs, specfile = /home/david/anaconda3/envs/linux.BCDI_MI/lib/python3.9/site-packages/bcdi-0.0.10a2-py3.9.egg/bcdi/preprocessing/alias_dict_2021.txt,


###############
Processing data
###############
Initial data size: ( 192 , 288 , 392 )
FFT size before accounting for phasing_binning (192, 288, 392)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (192, 288, 392)
Data shape used for orthogonalization and plotting: ( 180 , 178 , 202 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/Ar/S1373/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range)) ~  7 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.008 0.020 -0.010 ) rad
Max FFT= 3957133.9077831456
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 3957133.9077831456

Shape before orthogonalization (180, 178, 202)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 11.50 nm, 10.87 nm, 11.81 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0053 deg, 88.99 um, 106.73 um)
Sanity check, recalculated direct space voxel sizes: ( 11.50 nm, 10.87 nm, 11.81 nm )
out-of plane detector angle=0.326 deg, inplane_angle=37.938 deg
using SIXS geometry
rocking angle is mu, beta=0.000 deg
VTK spacing : (11.499383777054422, 10.866231455838511, 11.811373768490675) (nm)

Angle between q and y = 89.50 deg
Angle with y in zy plane = -88.46 deg
Angle with y in xy plane = -89.47 deg
Angle with z in xz plane = 108.97 deg

Normalized wavevector transfer [z, y, x]: [-0.32506635  0.00875166  0.94565072]
Wavevector transfer: (angstroms) 2.8006
Atomic plane distance: (angstroms) 2.2435 angstroms
center of mass at (z, y, x): ( 84.57 , 88.55 , 102.61 )
center of mass offset: ( 5 , 0 , -2 ) pixels
Support limits (start_z, stop_z, start_y, stop_y, start_x, stop_x):56, 116, 59, 116, 79, 125
Support limits (start_z, stop_z, start_y, stop_y, start_x, stop_x):56, 116, 59, 116, 79, 125
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.004 0.000 -0.007 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size: (11.50, 10.87, 11.81) (nm)
Final data shape: 180 178 202
Phase extent before and after thresholding: 3.49,3.49
phase.max() = 1.92 at voxel (98, 85, 120)
/home/david/anaconda3/envs/linux.BCDI_MI/lib/python3.9/site-packages/bcdi-0.0.10a2-py3.9.egg/bcdi/graph/graph_utils.py:1361: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
  fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2, figsize=(12, 9))
End of script
```

Fixing the voxel size just ends up zooming or not
Axis to align does not change anything