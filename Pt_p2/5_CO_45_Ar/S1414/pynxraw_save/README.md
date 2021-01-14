# Run pynx

````bash
(devel.p9) p9-02:5_CO_45_Ar/S1414/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
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
data S1414_pynx_norm_128_300_294_1_1_1.npz
mask S1414_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1414_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1414_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 858948 pixels masked ( 7.608%)
Saving data to CXI file:  S1414_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   699 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   608 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Running modes analysis on all

````bash
(devel.p9) p9-07:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py S1414_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-23-38_Run0003_LLKf000.1858_LLK000.1722_SupportThreshold0.29151.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-38-18_Run0013_LLKf000.1858_LLK000.1720_SupportThreshold0.28913.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-54-23_Run0024_LLKf000.1872_LLK000.1729_SupportThreshold0.27408.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-00-22_Run0028_LLKf000.1875_LLK000.1729_SupportThreshold0.27689.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-19-49_Run0041_LLKf000.1860_LLK000.1724_SupportThreshold0.28887.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-35-59_Run0052_LLKf000.1857_LLK000.1718_SupportThreshold0.29256.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-41-56_Run0056_LLKf000.1864_LLK000.1722_SupportThreshold0.28526.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-07-20_Run0073_LLKf000.1859_LLK000.1717_SupportThreshold0.29464.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-14-55_Run0078_LLKf000.1874_LLK000.1733_SupportThreshold0.27221.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-39-37_Run0095_LLKf000.1863_LLK000.1721_SupportThreshold0.29030.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-35-59_Run0052_LLKf000.1857_LLK000.1718_SupportThreshold0.29256.cxi] - this may take a while
R_match(0, 1) = 24.376% [8 arrays remaining]
R_match(0, 2) = 24.992% [7 arrays remaining]
R_match(0, 3) = 24.455% [6 arrays remaining]
R_match(0, 4) = 25.560% [5 arrays remaining]
R_match(0, 5) = 26.585% [4 arrays remaining]
R_match(0, 6) = 27.010% [3 arrays remaining]
R_match(0, 7) = 25.750% [2 arrays remaining]
R_match(0, 8) = 25.701% [1 arrays remaining]
R_match(0, 9) = 26.649% [0 arrays remaining]
Elapsed time:   90.2s
Analysing modes
First mode represents 96.446%
Saving modes analysis to: modes.h5
````

# Running modes on only the good ones

````bash
(devel.p9) p9-07:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py S1414_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-23-38_Run0003_LLKf000.1858_LLK000.1722_SupportThreshold0.29151.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-19-49_Run0041_LLKf000.1860_LLK000.1724_SupportThreshold0.28887.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-41-56_Run0056_LLKf000.1864_LLK000.1722_SupportThreshold0.28526.cxi
Loading: S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-39-37_Run0095_LLKf000.1863_LLK000.1721_SupportThreshold0.29030.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-23-38_Run0003_LLKf000.1858_LLK000.1722_SupportThreshold0.29151.cxi] - this may take a while
R_match(0, 1) = 26.779% [2 arrays remaining]
R_match(0, 2) = 23.966% [1 arrays remaining]
R_match(0, 3) = 26.030% [0 arrays remaining]
Elapsed time:   30.3s
Analysing modes
First mode represents 97.157%
Saving modes analysis to: modes.h5
````

# Running modes on the flipped ones

````bash
(devel.p9) p9-07:5_CO_45_Ar/S1414/pynxraw % python pynx-cdi-analysis.py flipped/S1414_pynx_norm_128_300_294_1_1_1-* modes=1
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
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-38-18_Run0013_LLKf000.1858_LLK000.1720_SupportThreshold0.28913.cxi
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T09-54-23_Run0024_LLKf000.1872_LLK000.1729_SupportThreshold0.27408.cxi
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-00-22_Run0028_LLKf000.1875_LLK000.1729_SupportThreshold0.27689.cxi
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-35-59_Run0052_LLKf000.1857_LLK000.1718_SupportThreshold0.29256.cxi
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-07-20_Run0073_LLKf000.1859_LLK000.1717_SupportThreshold0.29464.cxi
Loading: flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T11-14-55_Run0078_LLKf000.1874_LLK000.1733_SupportThreshold0.27221.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1414_pynx_norm_128_300_294_1_1_1-2021-01-13T10-35-59_Run0052_LLKf000.1857_LLK000.1718_SupportThreshold0.29256.cxi] - this may take a while
R_match(0, 1) = 24.992% [4 arrays remaining]
R_match(0, 2) = 24.455% [3 arrays remaining]
R_match(0, 3) = 25.560% [2 arrays remaining]
R_match(0, 4) = 25.750% [1 arrays remaining]
R_match(0, 5) = 25.701% [0 arrays remaining]
Elapsed time:   44.2s
Analysing modes
First mode represents 96.803%
Saving modes analysis to: modes.h5
````