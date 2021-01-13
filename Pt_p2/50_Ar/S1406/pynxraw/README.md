# Run pynx

````bash
(devel.p9) p9-02:50_Ar/S1406/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
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
data S1406_pynx_norm_128_300_294_1_1_1.npz
mask S1406_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1406_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1406_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 932063 pixels masked ( 8.256%)
Saving data to CXI file:  S1406_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   458 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   623 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Run modes on all

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-21-34_Run0007_LLKf000.1604_LLK000.1675_SupportThreshold0.29146.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-24-28_Run0009_LLKf000.1608_LLK000.1675_SupportThreshold0.26541.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-39-05_Run0019_LLKf000.1614_LLK000.1710_SupportThreshold0.27685.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-47-45_Run0025_LLKf000.1610_LLK000.1677_SupportThreshold0.28371.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-49-11_Run0026_LLKf000.1609_LLK000.1676_SupportThreshold0.28677.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-10-52_Run0041_LLKf000.1610_LLK000.1688_SupportThreshold0.29628.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-12-20_Run0042_LLKf000.1609_LLK000.1679_SupportThreshold0.29649.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-22-23_Run0049_LLKf000.1610_LLK000.1678_SupportThreshold0.28432.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-29-42_Run0054_LLKf000.1608_LLK000.1676_SupportThreshold0.26994.cxi
Loading: S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T11-22-03_Run0090_LLKf000.1610_LLK000.1681_SupportThreshold0.29593.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-21-34_Run0007_LLKf000.1604_LLK000.1675_SupportThreshold0.29146.cxi] - this may take a while
R_match(0, 1) = 29.798% [8 arrays remaining]
R_match(0, 2) = 58.390% [7 arrays remaining]
R_match(0, 3) = 26.581% [6 arrays remaining]
R_match(0, 4) = 28.809% [5 arrays remaining]
R_match(0, 5) = 32.826% [4 arrays remaining]
R_match(0, 6) = 29.543% [3 arrays remaining]
R_match(0, 7) = 27.076% [2 arrays remaining]
R_match(0, 8) = 28.212% [1 arrays remaining]
R_match(0, 9) = 30.510% [0 arrays remaining]
Elapsed time:   79.5s
Analysing modes
First mode represents 93.399%
Saving modes analysis to: modes.h5
````

# Run modes on flipped ones

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py flipped/S1406_pynx_norm_128_300_294_1_1_1-* modes=1--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: flipped/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-21-34_Run0007_LLKf000.1604_LLK000.1675_SupportThreshold0.29146.cxi
Loading: flipped/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-47-45_Run0025_LLKf000.1610_LLK000.1677_SupportThreshold0.28371.cxi
Loading: flipped/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-10-52_Run0041_LLKf000.1610_LLK000.1688_SupportThreshold0.29628.cxi
Loading: flipped/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T11-22-03_Run0090_LLKf000.1610_LLK000.1681_SupportThreshold0.29593.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-21-34_Run0007_LLKf000.1604_LLK000.1675_SupportThreshold0.29146.cxi] - this may take a while
R_match(0, 1) = 26.581% [2 arrays remaining]
R_match(0, 2) = 32.826% [1 arrays remaining]
R_match(0, 3) = 30.510% [0 arrays remaining]
Elapsed time:   27.3s
Analysing modes
First mode represents 96.350%
Saving modes analysis to: modes.h5
````

# Run modes on good ones

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py good/S1406_pynx_norm_128_300_294_1_1_1-* modes=1--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Importing data files
Loading: good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-24-28_Run0009_LLKf000.1608_LLK000.1675_SupportThreshold0.26541.cxi
Loading: good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T09-49-11_Run0026_LLKf000.1609_LLK000.1676_SupportThreshold0.28677.cxi
Loading: good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-12-20_Run0042_LLKf000.1609_LLK000.1679_SupportThreshold0.29649.cxi
Loading: good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-22-23_Run0049_LLKf000.1610_LLK000.1678_SupportThreshold0.28432.cxi
Loading: good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-29-42_Run0054_LLKf000.1608_LLK000.1676_SupportThreshold0.26994.cxi
Calculating modes from the imported objects
Matching arrays against the first one [good/S1406_pynx_norm_128_300_294_1_1_1-2021-01-13T10-29-42_Run0054_LLKf000.1608_LLK000.1676_SupportThreshold0.26994.cxi] - this may take a while
R_match(0, 1) = 29.032% [3 arrays remaining]
R_match(0, 2) = 29.343% [2 arrays remaining]
R_match(0, 3) = 29.250% [1 arrays remaining]
R_match(0, 4) = 31.386% [0 arrays remaining]
Elapsed time:   35.0s
Analysing modes
First mode represents 96.193%
Saving modes analysis to: modes.h5
````