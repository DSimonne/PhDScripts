# A 100 PynX run, with no initial support

````bash
(pynx-gap.p9) p9-02:40_Ar_10_O2/S1401/pynxraw % python pynx-id01cdi.py pynx-cdi-input_100.txt
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Using parameters file:  pynx-cdi-input_100.txt
data S1401_pynx_norm_128_300_294_1_1_1.npz
mask S1401_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1401_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1401_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 824046 pixels masked ( 7.299%)
Saving data to CXI file:  S1401_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1613.92 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1544.35 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# To activate the good environment fpr pynx analysis script

`source /sware/exp/pynx/devel.p9/bin/activate`

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1401/pynxraw % python pynx-cdi-analysis.py S1401_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T12-35-55_Run0005_LLKf000.2752_LLK11617815494.5374_SupportThreshold0.11709.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T12-44-14_Run0011_LLKf000.2814_LLK250091323852.5391_SupportThreshold0.13391.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-00-56_Run0024_LLKf000.2397_LLK24732971191.4062_SupportThreshold0.13122.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-16-13_Run0036_LLKf000.1725_LLK000.1875_SupportThreshold0.19753.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-20-16_Run0040_LLKf000.2702_LLK102805213928.2227_SupportThreshold0.13027.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-21-03_Run0041_LLKf000.2488_LLK11161841154.0985_SupportThreshold0.13203.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-21-41_Run0042_LLKf000.2738_LLK11299086809.1583_SupportThreshold0.12577.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-47-30_Run0064_LLKf000.2763_LLK10816708803.1769_SupportThreshold0.11844.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T14-13-51_Run0089_LLKf000.2535_LLK24014744758.6060_SupportThreshold0.13191.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T14-21-31_Run0099_LLKf000.2874_LLK11242763996.1243_SupportThreshold0.12898.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T13-16-13_Run0036_LLKf000.1725_LLK000.1875_SupportThreshold0.19753.cxi] - this may take a while
R_match(0, 1) = 56.607% [8 arrays remaining]
R_match(0, 2) = 64.164% [7 arrays remaining]
R_match(0, 3) = 78.297% [6 arrays remaining]
R_match(0, 4) = 65.164% [5 arrays remaining]
R_match(0, 5) = 78.217% [4 arrays remaining]
R_match(0, 6) = 63.680% [3 arrays remaining]
R_match(0, 7) = 64.908% [2 arrays remaining]
R_match(0, 8) = 75.967% [1 arrays remaining]
R_match(0, 9) = 74.673% [0 arrays remaining]
Elapsed time:   81.8s
Analysing modes
First mode represents 74.155%
Saving modes analysis to: modes.h5
````

# After new support determination, 50 runs

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1401/pynxraw % python pynx-id01cdi.py pynx-cdi-input_50.txt
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
data S1401_pynx_norm_128_300_294_1_1_1.npz
mask S1401_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1401_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1401_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb , 904.18 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb , 336.88 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1401_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 824046 pixels masked ( 7.299%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
Loading support from:  filter_sig5_t20_mask_0.2.npz
Initialized support  (128, 300, 294) , with 87674 pixels ( 0.777%)
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Analysis after new support determination

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1401/pynxraw % python pynx-cdi-analysis.py S1401_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-19-54_Run0001_LLKf000.2324_LLK11842081546.7834_SupportThreshold0.12486.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-23-02_Run0004_LLKf000.2485_LLK000.1813_SupportThreshold0.19726.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-39-20_Run0022_LLKf000.2474_LLK11436803340.9119_SupportThreshold0.12996.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-54-39_Run0036_LLKf000.2476_LLK000.1843_SupportThreshold0.19945.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-56-09_Run0037_LLKf000.2469_LLK171665115356.4453_SupportThreshold0.13380.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1401_pynx_norm_128_300_294_1_1_1-2021-01-06T15-19-54_Run0001_LLKf000.2324_LLK11842081546.7834_SupportThreshold0.12486.cxi] - this may take a while
R_match(0, 1) = 77.355% [3 arrays remaining]
R_match(0, 2) = 73.196% [2 arrays remaining]
R_match(0, 3) = 62.541% [1 arrays remaining]
R_match(0, 4) = 72.326% [0 arrays remaining]
Elapsed time:   35.4s
Analysing modes
First mode represents 79.474%
Saving modes analysis to: modes.h5
````

# Launching strain.py

```bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1401/pynxraw$ python strain_old.py 
/home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1401/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 180 , 180 , 192 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1401/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  52 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.003 0.601 -0.355 ) rad
Max FFT= 2377291.8451157687
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 2377291.8451157687

Shape before orthogonalization (180, 180, 192)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0078 deg, 91.67 um, 84.22 um)
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
center of mass at (z, y, x): ( 88.29 , 88.30 , 102.52 )
center of mass offset: ( 2 , 2 , -7 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.002 -0.005 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 7.508056659330176 2.0085757106646365
phase.max() =  1.0712401539649883 , at coordinates  89 110 178
End of script
````