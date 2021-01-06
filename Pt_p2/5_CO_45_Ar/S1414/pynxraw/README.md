# A 100 PynX run, with no initial support

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-id01cdi.py pynx-cdi-input_100.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-cdi-input_100.txt
data S1414_pynx_norm_128_300_294_1_1_1.npz
mask S1414_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1414_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1414_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1518.76 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1539.98 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1414_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 724877 pixels masked ( 6.421%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````	

# To activate the good environment fpr pynx analysis script

`source /sware/exp/pynx/devel.p9/bin/activate`

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T1* modes=1
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
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-12-32_Run0005_LLKf000.2251_LLK10914092063.9038_SupportThreshold0.12811.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-13-40_Run0007_LLKf000.2116_LLK18752760887.1460_SupportThreshold0.13002.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-25-45_Run0026_LLKf000.2338_LLK128257074356.0791_SupportThreshold0.13028.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-26-09_Run0027_LLKf000.2264_LLK14988203048.7061_SupportThreshold0.12806.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-45-52_Run0043_LLKf000.2538_LLK47087259292.6025_SupportThreshold0.12051.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-54-25_Run0050_LLKf000.1601_LLK000.1833_SupportThreshold0.19477.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T13-02-56_Run0056_LLKf000.2763_LLK83716192245.4834_SupportThreshold0.11442.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T13-47-40_Run0092_LLKf000.2718_LLK67956871986.3892_SupportThreshold0.11676.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T13-53-26_Run0096_LLKf000.2216_LLK11530823707.5806_SupportThreshold0.12736.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T13-53-58_Run0097_LLKf000.2393_LLK12115581035.6140_SupportThreshold0.12403.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T12-54-25_Run0050_LLKf000.1601_LLK000.1833_SupportThreshold0.19477.cxi] - this may take a while
R_match(0, 1) = 69.052% [8 arrays remaining]
R_match(0, 2) = 73.067% [7 arrays remaining]
R_match(0, 3) = 68.129% [6 arrays remaining]
R_match(0, 4) = 77.848% [5 arrays remaining]
R_match(0, 5) = 71.586% [4 arrays remaining]
R_match(0, 6) = 69.327% [3 arrays remaining]
R_match(0, 7) = 74.506% [2 arrays remaining]
R_match(0, 8) = 74.023% [1 arrays remaining]
R_match(0, 9) = 64.254% [0 arrays remaining]
Elapsed time:   84.4s
Analysing modes
First mode represents 75.288%
Saving modes analysis to: modes.h5
````

# After new support determination, 50 runs

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-id01cdi.py pynx-cdi-input_100.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-cdi-input_100.txt
data S1414_pynx_norm_128_300_294_1_1_1.npz
mask S1414_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1414_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1414_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1518.76 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1539.98 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1414_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 724877 pixels masked ( 6.421%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Analysis after new support determination

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T1* modes=1
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
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-22-31_Run0011_LLKf000.2595_LLK640360717773.4375_SupportThreshold0.13150.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-43-28_Run0033_LLKf000.2611_LLK296001110076.9043_SupportThreshold0.12987.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-45-15_Run0035_LLKf000.2579_LLK65678715705.8716_SupportThreshold0.13216.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-56-12_Run0046_LLKf000.2505_LLK11074535846.7102_SupportThreshold0.13068.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-57-47_Run0049_LLKf000.2596_LLK12211879491.8060_SupportThreshold0.12639.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1414_pynx_norm_128_300_294_1_1_1-2021-01-06T15-56-12_Run0046_LLKf000.2505_LLK11074535846.7102_SupportThreshold0.13068.cxi] - this may take a while
R_match(0, 1) = 74.282% [3 arrays remaining]
R_match(0, 2) = 73.776% [2 arrays remaining]
R_match(0, 3) = 68.861% [1 arrays remaining]
R_match(0, 4) = 68.028% [0 arrays remaining]
Elapsed time:   38.3s
Analysing modes
First mode represents 79.341%
Saving modes analysis to: modes.h5
````

# Launching strain

````bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/5_CO_45_Ar/S1414/pynxraw$ python strain_old.py 
/home/david/Documents/PhD/PhDScripts/Pt_p2/5_CO_45_Ar/S1414/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 190 , 186 , 192 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD/PhDScripts/Pt_p2/5_CO_45_Ar/S1414/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  56 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.039 0.607 -0.368 ) rad
Max FFT= 2296028.128610338
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 2296028.128610338

Shape before orthogonalization (190, 186, 192)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0074 deg, 88.71 um, 84.22 um)
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
center of mass at (z, y, x): ( 93.32 , 95.66 , 95.76 )
center of mass offset: ( 2 , -3 , 0 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.001 -0.004 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 10.529764859445244 2.6891504818042553
phase.max() =  1.6193510022531026 , at coordinates  122 174 91
End of script
````