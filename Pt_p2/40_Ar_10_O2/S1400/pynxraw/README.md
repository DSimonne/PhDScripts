# A 100 PynX run, with no initial support

````bash
(pynx-gap.p9) p9-02:40_Ar_10_O2/S1400/pynxraw % python pynx-id01cdi.py pynx-cdi-input_100.txt
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Using parameters file:  pynx-cdi-input_100.txt
data S1400_pynx_norm_128_300_294_1_1_1.npz
mask S1400_maskpynx_norm_128_300_294_1_1_1.npz
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
wavelength 1.3775e-10
verbose 100
output_format cxi
live_plot False

Loading data:  S1400_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1400_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 848840 pixels masked ( 7.519%)
Saving data to CXI file:  S1400_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1600.64 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1607.74 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# To activate the good environment fpr pynx analysis script

`source /sware/exp/pynx/devel.p9/bin/activate`

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1400/pynxraw % python pynx-cdi-analysis.py S1400_pynx_norm_128_300_294_1_1_1-* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T12-41-22_Run0009_LLKf000.2577_LLK182345523834.2285_SupportThreshold0.13295.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T12-59-12_Run0025_LLKf000.2850_LLK10706841945.6482_SupportThreshold0.12667.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-10-38_Run0034_LLKf000.2864_LLK257202587127.6855_SupportThreshold0.11729.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-25-07_Run0046_LLKf000.2894_LLK1064471435546.8750_SupportThreshold0.13469.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-25-57_Run0047_LLKf000.2420_LLK10034444332.1228_SupportThreshold0.12915.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-32-40_Run0052_LLKf000.2457_LLK10376600027.0844_SupportThreshold0.13170.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-39-58_Run0058_LLKf000.2570_LLK10007194280.6244_SupportThreshold0.12457.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-49-52_Run0067_LLKf000.2488_LLK527687072753.9062_SupportThreshold0.13461.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T13-53-34_Run0070_LLKf000.2743_LLK10025887489.3188_SupportThreshold0.12977.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T14-20-17_Run0096_LLKf000.2404_LLK10247404575.3479_SupportThreshold0.12287.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T14-20-17_Run0096_LLKf000.2404_LLK10247404575.3479_SupportThreshold0.12287.cxi] - this may take a while
R_match(0, 1) = 73.247% [8 arrays remaining]
R_match(0, 2) = 72.760% [7 arrays remaining]
R_match(0, 3) = 74.415% [6 arrays remaining]
R_match(0, 4) = 67.476% [5 arrays remaining]
R_match(0, 5) = 73.483% [4 arrays remaining]
R_match(0, 6) = 65.469% [3 arrays remaining]
R_match(0, 7) = 69.651% [2 arrays remaining]
R_match(0, 8) = 78.107% [1 arrays remaining]
R_match(0, 9) = 78.247% [0 arrays remaining]
Elapsed time:   86.3s
Analysing modes
First mode represents 74.511%
Saving modes analysis to: modes.h5
````

# After new support determination, 50 runs

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1400/pynxraw % python pynx-id01cdi.py pynx-cdi-input_50.txt
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-cdi-input_50.txt
data S1400_pynx_norm_128_300_294_1_1_1.npz
mask S1400_maskpynx_norm_128_300_294_1_1_1.npz
data2cxi True
auto_center_resize False
support filter_sig5_t20_mask_0.2.npz
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
nb_run 50
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
live_plot False

Loading data:  S1400_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1400_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1534.66 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1542.00 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1400_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 848840 pixels masked ( 7.519%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
Loading support from:  filter_sig5_t20_mask_0.2.npz
Initialized support  (128, 300, 294) , with 78005 pixels ( 0.691%)
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Analysis after new support determination

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1400/pynxraw % python pynx-cdi-analysis.py S1400_pynx_norm_128_300_294_1_1_1-* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-25-47_Run0008_LLKf000.2758_LLK9899786710.7391_SupportThreshold0.12889.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-26-49_Run0010_LLKf000.1637_LLK000.1820_SupportThreshold0.19946.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-28-27_Run0012_LLKf000.2699_LLK135357656478.8818_SupportThreshold0.13025.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-37-16_Run0022_LLKf000.1657_LLK000.1863_SupportThreshold0.19917.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-52-31_Run0040_LLKf000.2385_LLK9631733894.3481_SupportThreshold0.12736.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1400_pynx_norm_128_300_294_1_1_1-2021-01-06T15-26-49_Run0010_LLKf000.1637_LLK000.1820_SupportThreshold0.19946.cxi] - this may take a while
R_match(0, 1) = 60.682% [3 arrays remaining]
R_match(0, 2) = 77.516% [2 arrays remaining]
R_match(0, 3) = 50.740% [1 arrays remaining]
R_match(0, 4) = 70.303% [0 arrays remaining]
Elapsed time:   38.1s
Analysing modes
First mode represents 79.791%
Saving modes analysis to: modes.h5
````
# Launching strain
````bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400/pynxraw$ python strain_old.py 
/home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 182 , 180 , 188 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  47 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.002 0.608 -0.352 ) rad
Max FFT= 2104527.2890778566
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 2104527.2890778566

Shape before orthogonalization (182, 180, 188)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0077 deg, 91.67 um, 86.01 um)
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
center of mass at (z, y, x): ( 88.11 , 96.58 , 94.40 )
center of mass offset: ( 3 , -7 , 0 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.001 -0.004 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 7.666306313040858 2.1748795602022852
phase.max() =  1.0978312984432255 , at coordinates  10 120 133
End of script
````