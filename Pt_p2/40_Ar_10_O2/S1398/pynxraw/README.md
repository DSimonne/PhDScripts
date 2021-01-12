# A new beginning
````bash
(devel.p9) p9-01:40_Ar_10_O2/S1398/pynxraw_2020 % python  pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-34-08_Run0008_LLKf000.1203_LLK000.1331_SupportThreshold0.29902.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-35-30_Run0010_LLKf000.1202_LLK000.1333_SupportThreshold0.29495.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-37-31_Run0013_LLKf000.1203_LLK000.1332_SupportThreshold0.29415.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-44-23_Run0023_LLKf000.1206_LLK000.1333_SupportThreshold0.29070.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-47-49_Run0028_LLKf000.1205_LLK000.1332_SupportThreshold0.29519.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-09-29_Run0060_LLKf000.1203_LLK000.1330_SupportThreshold0.29976.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-10-52_Run0062_LLKf000.1208_LLK000.1333_SupportThreshold0.29019.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-14-58_Run0068_LLKf000.1205_LLK000.1333_SupportThreshold0.29837.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-34-31_Run0097_LLKf000.1204_LLK000.1333_SupportThreshold0.29290.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-35-12_Run0098_LLKf000.1200_LLK000.1331_SupportThreshold0.29585.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-35-12_Run0098_LLKf000.1200_LLK000.1331_SupportThreshold0.29585.cxi] - this may take a while
R_match(0, 1) = 40.194% [8 arrays remaining]
R_match(0, 2) = 41.378% [7 arrays remaining]
R_match(0, 3) = 42.364% [6 arrays remaining]
R_match(0, 4) = 39.477% [5 arrays remaining]
R_match(0, 5) = 36.243% [4 arrays remaining]
R_match(0, 6) = 38.052% [3 arrays remaining]
R_match(0, 7) = 36.166% [2 arrays remaining]
R_match(0, 8) = 35.615% [1 arrays remaining]
R_match(0, 9) = 37.106% [0 arrays remaining]
Elapsed time:   89.7s
Analysing modes
First mode represents 92.841%
Saving modes analysis to: modes.h5
````

These cxi files came without even a support input

````bash
(linux.BCDI_MI) david@ord00003:~/Documents/PhD_local/PhDScripts/Pt_p2/40_Ar_10_O2/S1398/pynxraw_2020$ python strain_2020.py
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 210 , 172 , 184 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD_local/PhDScripts/Pt_p2/40_Ar_10_O2/S1398/pynxraw_2020/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  42 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.006 0.562 -0.307 ) rad
Max FFT= 2313582.8395902053
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 2313582.839590206

Shape before orthogonalization (210, 172, 184)
Real space pixel size (z, y, x) based on initial FFT shape: ( 6.08 nm, 10.95 nm, 11.18 nm )
Tilt, pixel_y, pixel_x based on actual array shape: ( 0.0067 deg, 95.93 um, 87.88 um)
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
center of mass at (z, y, x): ( 80.37 , 74.20 , 73.19 )
center of mass offset: ( 25 , 12 , 19 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.014 -0.001 0.007 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 5.970903236059291 3.8169256751518486
phase.max() =  2.166524574376124 , at coordinates  19 91 126
End of script
````

Il y a des fichiers cxi vraiment moins bien que d'autres, pour certains, ils sont même tournés

S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-47-49_Run0028_LLKf000.1205_LLK000.1332_SupportThreshold0.29519.cxi is flipped
S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-09-29_Run0060_LLKf000.1203_LLK000.1330_SupportThreshold0.29976.cxi is bad
S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-10-52_Run0062_LLKf000.1208_LLK000.1333_SupportThreshold0.29019.cxi is flipped
S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-35-12_Run0098_LLKf000.1200_LLK000.1331_SupportThreshold0.29585.cxi is flipped

# Running modes on the 6 datasets that were quite good :

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1398/pynxraw_2020 % python pynx-cdi-analysis.py before_mask/*.cxi modes =1
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
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-34-08_Run0008_LLKf000.1203_LLK000.1331_SupportThreshold0.29902.cxi
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-35-30_Run0010_LLKf000.1202_LLK000.1333_SupportThreshold0.29495.cxi
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-37-31_Run0013_LLKf000.1203_LLK000.1332_SupportThreshold0.29415.cxi
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-44-23_Run0023_LLKf000.1206_LLK000.1333_SupportThreshold0.29070.cxi
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-14-58_Run0068_LLKf000.1205_LLK000.1333_SupportThreshold0.29837.cxi
Loading: before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T00-34-31_Run0097_LLKf000.1204_LLK000.1333_SupportThreshold0.29290.cxi
Calculating modes from the imported objects
Matching arrays against the first one [before_mask/S1398_pynx_norm_128_300_294_1_1_1-2021-01-11T23-35-30_Run0010_LLKf000.1202_LLK000.1333_SupportThreshold0.29495.cxi] - this may take a while
R_match(0, 1) = 36.012% [4 arrays remaining]
R_match(0, 2) = 31.657% [3 arrays remaining]
R_match(0, 3) = 41.270% [2 arrays remaining]
R_match(0, 4) = 34.133% [1 arrays remaining]
R_match(0, 5) = 35.984% [0 arrays remaining]
Elapsed time:   48.3s
Analysing modes
First mode represents 94.100%
Saving modes analysis to: modes.h5
````

# New run, this time we are sure that we used a good support

````bash
(devel.p9) p9-01:40_Ar_10_O2/S1398/pynxraw_2020 % python pynx-id01cdi.py pynx-run-2020-direct-mask.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-01
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-run-2020-direct-mask.txt
data S1398_pynx_norm_128_300_294_1_1_1.npz
mask S1398_maskpynx_norm_128_300_294_1_1_1.npz
data2cxi True
auto_center_resize False
support direct_mask.npz
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
                                        Tesla V100-SXM2-32GB: 32256Mb ,1531.74 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1483.74 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1398_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 795106 pixels masked ( 7.043%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
Loading support from:  direct_mask.npz
Initialized support  (128, 300, 294) , with 94557 pixels ( 0.838%)
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Modes

````bash
(devel.p9) p9-01:40_Ar_10_O2/S1398/pynxraw_2020 % python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-23-23_Run0006_LLKf000.1146_LLK000.1340_SupportThreshold0.29748.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-28-45_Run0012_LLKf000.1152_LLK000.1343_SupportThreshold0.29181.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-34-36_Run0019_LLKf000.1150_LLK000.1342_SupportThreshold0.29230.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-46-33_Run0033_LLKf000.1148_LLK000.1341_SupportThreshold0.29642.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-53-32_Run0041_LLKf000.1147_LLK000.1341_SupportThreshold0.29823.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T14-07-42_Run0057_LLKf000.1152_LLK000.1343_SupportThreshold0.29115.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T14-11-14_Run0061_LLKf000.1148_LLK000.1340_SupportThreshold0.29934.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T14-22-40_Run0074_LLKf000.1153_LLK000.1343_SupportThreshold0.29054.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T14-28-51_Run0081_LLKf000.1156_LLK000.1346_SupportThreshold0.28200.cxi
Loading: S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T14-33-13_Run0086_LLKf000.1153_LLK000.1342_SupportThreshold0.29618.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1398_pynx_norm_128_300_294_1_1_1-2021-01-12T13-23-23_Run0006_LLKf000.1146_LLK000.1340_SupportThreshold0.29748.cxi] - this may take a while
R_match(0, 1) = 31.488% [8 arrays remaining]
R_match(0, 2) = 36.517% [7 arrays remaining]
R_match(0, 3) = 32.922% [6 arrays remaining]
R_match(0, 4) = 35.273% [5 arrays remaining]
R_match(0, 5) = 37.892% [4 arrays remaining]
R_match(0, 6) = 33.890% [3 arrays remaining]
R_match(0, 7) = 35.288% [2 arrays remaining]
R_match(0, 8) = 35.596% [1 arrays remaining]
R_match(0, 9) = 35.337% [0 arrays remaining]
Elapsed time:   89.3s
Analysing modes
First mode represents 93.987%
Saving modes analysis to: modes.h5
````