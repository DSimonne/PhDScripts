# Run pynx

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

# Run modes on all

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
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-17-25_Run0001_LLKf000.1501_LLK000.1807_SupportThreshold0.29580.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-46-22_Run0035_LLKf000.1502_LLK000.1809_SupportThreshold0.28934.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-48-06_Run0037_LLKf000.1502_LLK000.1813_SupportThreshold0.28400.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-52-29_Run0042_LLKf000.1501_LLK000.1810_SupportThreshold0.28866.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-53-20_Run0043_LLKf000.1502_LLK000.1813_SupportThreshold0.28236.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-17-13_Run0061_LLKf000.1501_LLK000.1809_SupportThreshold0.29184.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-28-21_Run0065_LLKf000.1501_LLK000.1818_SupportThreshold0.26875.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-31-07_Run0066_LLKf000.1501_LLK000.1816_SupportThreshold0.27192.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-39-25_Run0069_LLKf000.1500_LLK000.1810_SupportThreshold0.28998.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T23-37-12_Run0090_LLKf000.1502_LLK000.1814_SupportThreshold0.27712.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-39-25_Run0069_LLKf000.1500_LLK000.1810_SupportThreshold0.28998.cxi] - this may take a while
R_match(0, 1) = 29.815% [8 arrays remaining]
R_match(0, 2) = 27.579% [7 arrays remaining]
R_match(0, 3) = 29.963% [6 arrays remaining]
R_match(0, 4) = 16.493% [5 arrays remaining]
R_match(0, 5) = 24.092% [4 arrays remaining]
R_match(0, 6) = 24.666% [3 arrays remaining]
R_match(0, 7) = 32.369% [2 arrays remaining]
R_match(0, 8) = 24.227% [1 arrays remaining]
R_match(0, 9) = 27.184% [0 arrays remaining]
Elapsed time:  296.8s
Analysing modes
First mode represents 96.132%
Saving modes analysis to: modes.h5
````

# Run modes on good ones

````bash
(devel.p9) p9-07:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py S1400_pynx_norm_128_300_294_1_1_1-* modes=1--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-52-29_Run0042_LLKf000.1501_LLK000.1810_SupportThreshold0.28866.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-53-20_Run0043_LLKf000.1502_LLK000.1813_SupportThreshold0.28236.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-17-13_Run0061_LLKf000.1501_LLK000.1809_SupportThreshold0.29184.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-28-21_Run0065_LLKf000.1501_LLK000.1818_SupportThreshold0.26875.cxi
Loading: S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-31-07_Run0066_LLKf000.1501_LLK000.1816_SupportThreshold0.27192.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-52-29_Run0042_LLKf000.1501_LLK000.1810_SupportThreshold0.28866.cxi] - this may take a while
R_match(0, 1) = 25.215% [3 arrays remaining]
R_match(0, 2) = 23.976% [2 arrays remaining]
R_match(0, 3) = 29.112% [1 arrays remaining]
R_match(0, 4) = 24.441% [0 arrays remaining]
Elapsed time:   36.0s
Analysing modes
First mode represents 96.641%
Saving modes analysis to: modes.h5
````

# Run modes on flipped ones

````bash
(devel.p9) p9-07:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py flipped/S1400_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-17-25_Run0001_LLKf000.1501_LLK000.1807_SupportThreshold0.29580.cxi
Loading: flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-46-22_Run0035_LLKf000.1502_LLK000.1809_SupportThreshold0.28934.cxi
Loading: flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T21-48-06_Run0037_LLKf000.1502_LLK000.1813_SupportThreshold0.28400.cxi
Loading: flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-39-25_Run0069_LLKf000.1500_LLK000.1810_SupportThreshold0.28998.cxi
Loading: flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T23-37-12_Run0090_LLKf000.1502_LLK000.1814_SupportThreshold0.27712.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1400_pynx_norm_128_300_294_1_1_1-2021-01-12T22-39-25_Run0069_LLKf000.1500_LLK000.1810_SupportThreshold0.28998.cxi] - this may take a while
R_match(0, 1) = 29.815% [3 arrays remaining]
R_match(0, 2) = 27.579% [2 arrays remaining]
R_match(0, 3) = 29.963% [1 arrays remaining]
R_match(0, 4) = 27.184% [0 arrays remaining]
Elapsed time:   35.5s
Analysing modes
First mode represents 96.330%
Saving modes analysis to: modes.h5
````