# New run, with old scripts

````bash
(devel.p9) p9-01:~ % python pynx-id01cdi.py pynx-run-no-support.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-01
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-run-no-support.txt
data S1399_pynx_norm_128_300_294_1_1_1.npz
mask S1399_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1399_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1399_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 774320 pixels masked ( 6.859%)
Saving data to CXI file:  S1399_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing FFT speed for available CUDA GPU[ranking by fft, fft_shape=(16, 400, 400)]:
                                        Tesla V100-SXM2-32GB: 32256Mb ,1538.53 Gflop/s
                                        Tesla V100-SXM2-32GB: 32256Mb ,1541.86 Gflop/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Modes analysis

````bash
(devel.p9) p9-01:~ % python pynx-cdi-analysis.py S1399_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-13-42_Run0001_LLKf000.1637_LLK000.1685_SupportThreshold0.25649.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-21-36_Run0012_LLKf000.1636_LLK000.1677_SupportThreshold0.25773.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-22-26_Run0013_LLKf000.1627_LLK000.1736_SupportThreshold0.28355.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-37-40_Run0030_LLKf000.1638_LLK000.1680_SupportThreshold0.27743.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-42-58_Run0036_LLKf000.1637_LLK000.1683_SupportThreshold0.24114.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-49-49_Run0044_LLKf000.1638_LLK000.1684_SupportThreshold0.28394.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-06-38_Run0063_LLKf000.1632_LLK000.1678_SupportThreshold0.26107.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-11-59_Run0069_LLKf000.1634_LLK000.1680_SupportThreshold0.23190.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-26-05_Run0085_LLKf000.1629_LLK000.1677_SupportThreshold0.26013.cxi
Loading: S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-33-03_Run0093_LLKf000.1634_LLK000.1678_SupportThreshold0.26080.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-22-26_Run0013_LLKf000.1627_LLK000.1736_SupportThreshold0.28355.cxi] - this may take a while
R_match(0, 1) = 45.119% [8 arrays remaining]
R_match(0, 2) = 47.356% [7 arrays remaining]
R_match(0, 3) = 45.405% [6 arrays remaining]
R_match(0, 4) = 46.770% [5 arrays remaining]
R_match(0, 5) = 47.009% [4 arrays remaining]
R_match(0, 6) = 47.759% [3 arrays remaining]
R_match(0, 7) = 48.201% [2 arrays remaining]
R_match(0, 8) = 46.942% [1 arrays remaining]
R_match(0, 9) = 47.040% [0 arrays remaining]
Elapsed time:   80.5s
Analysing modes
First mode represents 95.077%
Saving modes analysis to: modes.h5
````

# Modes before mask, check for flipped ones

````bash
(devel.p9) p9-02:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T1* modes=1                                                      --------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-02
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-13-42_Run0001_LLKf000.1637_LLK000.1685_SupportThreshold0.25649.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-21-36_Run0012_LLKf000.1636_LLK000.1677_SupportThreshold0.25773.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-37-40_Run0030_LLKf000.1638_LLK000.1680_SupportThreshold0.27743.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T13-49-49_Run0044_LLKf000.1638_LLK000.1684_SupportThreshold0.28394.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-06-38_Run0063_LLKf000.1632_LLK000.1678_SupportThreshold0.26107.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-11-59_Run0069_LLKf000.1634_LLK000.1680_SupportThreshold0.23190.cxi
Loading: before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-33-03_Run0093_LLKf000.1634_LLK000.1678_SupportThreshold0.26080.cxi
Calculating modes from the imported objects
Matching arrays against the first one [before_mask/S1399_pynx_norm_128_300_294_1_1_1-2021-01-12T14-06-38_Run0063_LLKf000.1632_LLK000.1678_SupportThreshold0.26107.cxi] - this may take a while
R_match(0, 1) = 29.070% [5 arrays remaining]
R_match(0, 2) = 24.307% [4 arrays remaining]
R_match(0, 3) = 28.132% [3 arrays remaining]
R_match(0, 4) = 27.552% [2 arrays remaining]
R_match(0, 5) = 28.110% [1 arrays remaining]
R_match(0, 6) = 22.738% [0 arrays remaining]
Elapsed time:   53.1s
Analysing modes
First mode represents 96.566%
Saving modes analysis to: modes.h5
````

# Can try to do a new reconstruction, with initial mask