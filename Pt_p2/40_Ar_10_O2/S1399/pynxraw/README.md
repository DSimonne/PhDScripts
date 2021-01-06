# A 100 PynX run, with no initial support

````bash
(pynx-gap.p9) p9-02:40_Ar_10_O2/S1399/pynxraw % python pynx-id01cdi.py pynx-cdi-input_100.txt
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Using parameters file:  pynx-cdi-input_100.txt
data S1399_pynx_norm_128_300_294_1_1_1.npz
mask S1399_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1399_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1399_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 832720 pixels masked ( 7.376%)
Saving data to CXI file:  S1399_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1630.78 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1620.63 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# To activate the good environment fpr pynx analysis script

`source /sware/exp/pynx/devel.p9/bin/activate`

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py S1399_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T12-27-56_Run0001_LLKf000.2351_LLK10771352052.6886_SupportThreshold0.12055.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T12-49-52_Run0018_LLKf000.2355_LLK10387599468.2312_SupportThreshold0.12771.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T13-05-03_Run0029_LLKf000.2372_LLK10730016231.5369_SupportThreshold0.12664.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T13-05-46_Run0030_LLKf000.2515_LLK12614953517.9138_SupportThreshold0.12005.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T13-15-22_Run0037_LLKf000.2466_LLK53377161026.0010_SupportThreshold0.11996.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T13-16-02_Run0038_LLKf000.2156_LLK10353032350.5402_SupportThreshold0.12985.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T13-34-09_Run0055_LLKf000.2482_LLK11962997913.3606_SupportThreshold0.11718.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T14-12-35_Run0088_LLKf000.2136_LLK10725700855.2551_SupportThreshold0.12915.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T14-13-10_Run0089_LLKf000.2479_LLK29679756164.5508_SupportThreshold0.11962.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T14-19-41_Run0095_LLKf000.2199_LLK10506527423.8586_SupportThreshold0.12665.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T14-12-35_Run0088_LLKf000.2136_LLK10725700855.2551_SupportThreshold0.12915.cxi] - this may take a while
R_match(0, 1) = 79.172% [8 arrays remaining]
R_match(0, 2) = 70.895% [7 arrays remaining]
R_match(0, 3) = 79.733% [6 arrays remaining]
R_match(0, 4) = 74.217% [5 arrays remaining]
R_match(0, 5) = 81.757% [4 arrays remaining]
R_match(0, 6) = 67.723% [3 arrays remaining]
R_match(0, 7) = 79.156% [2 arrays remaining]
R_match(0, 8) = 75.741% [1 arrays remaining]
R_match(0, 9) = 82.590% [0 arrays remaining]
Elapsed time:   86.0s
Analysing modes
First mode represents 72.467%
Saving modes analysis to: modes.h5
````

# After new support determination, 50 runs

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1399/pynxraw % python pynx-id01cdi.py pynx-cdi-input_50.txt
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
data S1399_pynx_norm_128_300_294_1_1_1.npz
mask S1399_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1399_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1399_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1547.41 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb , 385.80 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1399_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 832720 pixels masked ( 7.376%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
Loading support from:  filter_sig5_t20_mask_0.2.npz
Initialized support  (128, 300, 294) , with 69666 pixels ( 0.617%)
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Analysis after new support determination
````bash
(devel.p9) p9-02:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py S1399_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T15-29-50_Run0013_LLKf000.2393_LLK13362524509.4299_SupportThreshold0.12361.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T15-38-34_Run0022_LLKf000.2504_LLK10428920984.2682_SupportThreshold0.10350.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T15-44-31_Run0028_LLKf000.2180_LLK10260871648.7885_SupportThreshold0.12747.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T15-45-05_Run0029_LLKf000.2353_LLK10438144207.0007_SupportThreshold0.12006.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T16-02-59_Run0049_LLKf000.2405_LLK9888525605.2017_SupportThreshold0.11941.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1399_pynx_norm_128_300_294_1_1_1-2021-01-06T15-44-31_Run0028_LLKf000.2180_LLK10260871648.7885_SupportThreshold0.12747.cxi] - this may take a while
R_match(0, 1) = 61.686% [3 arrays remaining]
R_match(0, 2) = 78.538% [2 arrays remaining]
R_match(0, 3) = 81.511% [1 arrays remaining]
R_match(0, 4) = 68.671% [0 arrays remaining]
Elapsed time:   38.1s
Analysing modes
First mode represents 76.829%
Saving modes analysis to: modes.h5
````

# Launching strain
````bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1399/pynxraw$ python strain_old.py 
/home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1399/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 186 , 176 , 190 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1399/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  49 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.004 0.622 -0.351 ) rad
Max FFT= 1945510.3598529114
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 1945510.3598529112

Shape before orthogonalization (186, 176, 190)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0076 deg, 93.75 um, 85.11 um)
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
center of mass at (z, y, x): ( 97.79 , 84.48 , 91.13 )
center of mass offset: ( -5 , 4 , 4 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.000 -0.004 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 10.345715743195019 1.8819018196436326
phase.max() =  1.0010957340630053 , at coordinates  102 111 11
End of script
````