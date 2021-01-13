# Pynx run, no support

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1400/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
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
data S1400_pynx_norm_128_300_294_1_1_1.npz
mask S1400_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1400_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1400_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 883688 pixels masked ( 7.827%)
Saving data to CXI file:  S1400_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   722 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   722 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Modes on all

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
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-31-47_Run0013_LLKf000.1557_LLK000.1790_SupportThreshold0.29710.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-45-03_Run0028_LLKf000.1561_LLK000.1790_SupportThreshold0.29572.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-46-46_Run0030_LLKf000.1558_LLK000.1789_SupportThreshold0.29811.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-55-32_Run0040_LLKf000.1562_LLK000.1794_SupportThreshold0.29442.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-56-26_Run0041_LLKf000.1561_LLK000.1793_SupportThreshold0.29026.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-16-29_Run0055_LLKf000.1563_LLK000.1793_SupportThreshold0.29372.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-19-15_Run0056_LLKf000.1561_LLK000.1790_SupportThreshold0.29622.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-30-12_Run0060_LLKf000.1561_LLK000.1793_SupportThreshold0.29511.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-31_Run0084_LLKf000.1560_LLK000.1793_SupportThreshold0.29221.cxi
Loading: S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T23-49-16_Run0089_LLKf000.1558_LLK000.1788_SupportThreshold0.29908.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-31-47_Run0013_LLKf000.1557_LLK000.1790_SupportThreshold0.29710.cxi] - this may take a while
R_match(0, 1) = 26.670% [8 arrays remaining]
R_match(0, 2) = 22.489% [7 arrays remaining]
R_match(0, 3) = 21.433% [6 arrays remaining]
R_match(0, 4) = 23.349% [5 arrays remaining]
R_match(0, 5) = 22.912% [4 arrays remaining]
R_match(0, 6) = 25.541% [3 arrays remaining]
R_match(0, 7) = 27.169% [2 arrays remaining]
R_match(0, 8) = 22.319% [1 arrays remaining]
R_match(0, 9) = 20.918% [0 arrays remaining]
Elapsed time:  240.0s
Analysing modes
First mode represents 97.012%
Saving modes analysis to: modes.h5
````

# Modes on good
````bash
(devel.p9) p9-07:40_Ar_10_O2/S1401/pynxraw % python pynx-cdi-analysis.py good/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: good/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-46-46_Run0030_LLKf000.1558_LLK000.1789_SupportThreshold0.29811.cxi
Loading: good/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-55-32_Run0040_LLKf000.1562_LLK000.1794_SupportThreshold0.29442.cxi
Calculating modes from the imported objects
Matching arrays against the first one [good/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-46-46_Run0030_LLKf000.1558_LLK000.1789_SupportThreshold0.29811.cxi] - this may take a while
R_match(0, 1) = 24.778% [0 arrays remaining]
Elapsed time:   10.0s
Analysing modes
First mode represents 98.465%
Saving modes analysis to: modes.h5
````

# Modes on flipped

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1401/pynxraw % python pynx-cdi-analysis.py flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T2* modes=1
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-31-47_Run0013_LLKf000.1557_LLK000.1790_SupportThreshold0.29710.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-45-03_Run0028_LLKf000.1561_LLK000.1790_SupportThreshold0.29572.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-56-26_Run0041_LLKf000.1561_LLK000.1793_SupportThreshold0.29026.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-16-29_Run0055_LLKf000.1563_LLK000.1793_SupportThreshold0.29372.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-19-15_Run0056_LLKf000.1561_LLK000.1790_SupportThreshold0.29622.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T22-30-12_Run0060_LLKf000.1561_LLK000.1793_SupportThreshold0.29511.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T23-35-31_Run0084_LLKf000.1560_LLK000.1793_SupportThreshold0.29221.cxi
Loading: flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T23-49-16_Run0089_LLKf000.1558_LLK000.1788_SupportThreshold0.29908.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1401_pynx_norm_128_300_294_1_1_1-2021-01-12T21-31-47_Run0013_LLKf000.1557_LLK000.1790_SupportThreshold0.29710.cxi] - this may take a while
R_match(0, 1) = 26.670% [6 arrays remaining]
R_match(0, 2) = 23.349% [5 arrays remaining]
R_match(0, 3) = 22.912% [4 arrays remaining]
R_match(0, 4) = 25.541% [3 arrays remaining]
R_match(0, 5) = 27.169% [2 arrays remaining]
R_match(0, 6) = 22.319% [1 arrays remaining]
R_match(0, 7) = 20.918% [0 arrays remaining]
Elapsed time:   65.8s
Analysing modes
First mode represents 96.971%
Saving modes analysis to: modes.h5
````