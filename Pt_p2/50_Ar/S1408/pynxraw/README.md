# Run pynx

````bash
(devel.p9) p9-02:50_Ar/S1408/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
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
data S1408_pynx_norm_128_300_294_1_1_1.npz
mask S1408_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1408_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Loading mask from:  S1408_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 885745 pixels masked ( 7.846%)
Saving data to CXI file:  S1408_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   609 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   683 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Run modes on all

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-36-06_Run0015_LLKf000.1482_LLK000.1761_SupportThreshold0.29619.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-37-39_Run0016_LLKf000.1485_LLK000.1760_SupportThreshold0.29157.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-52-25_Run0026_LLKf000.1488_LLK000.1768_SupportThreshold0.28666.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-58-22_Run0030_LLKf000.1478_LLK000.1759_SupportThreshold0.29790.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-16-07_Run0042_LLKf000.1491_LLK000.1762_SupportThreshold0.29104.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-20-33_Run0045_LLKf000.1489_LLK000.1770_SupportThreshold0.28445.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-25-03_Run0048_LLKf000.1482_LLK000.1760_SupportThreshold0.29647.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-29-38_Run0051_LLKf000.1484_LLK000.1761_SupportThreshold0.29009.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T11-29-31_Run0091_LLKf000.1479_LLK000.1761_SupportThreshold0.29972.cxi
Loading: S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T11-39-24_Run0098_LLKf000.1484_LLK000.1771_SupportThreshold0.29768.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-58-22_Run0030_LLKf000.1478_LLK000.1759_SupportThreshold0.29790.cxi] - this may take a while
R_match(0, 1) = 26.659% [8 arrays remaining]
R_match(0, 2) = 28.332% [7 arrays remaining]
R_match(0, 3) = 31.439% [6 arrays remaining]
R_match(0, 4) = 28.845% [5 arrays remaining]
R_match(0, 5) = 32.988% [4 arrays remaining]
R_match(0, 6) = 28.578% [3 arrays remaining]
R_match(0, 7) = 25.813% [2 arrays remaining]
R_match(0, 8) = 28.246% [1 arrays remaining]
R_match(0, 9) = 30.956% [0 arrays remaining]
Elapsed time:   86.9s
Analysing modes
First mode represents 95.245%
Saving modes analysis to: modes.h5
````

# running modes on flipped

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-36-06_Run0015_LLKf000.1482_LLK000.1761_SupportThreshold0.29619.cxi
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-37-39_Run0016_LLKf000.1485_LLK000.1760_SupportThreshold0.29157.cxi
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-16-07_Run0042_LLKf000.1491_LLK000.1762_SupportThreshold0.29104.cxi
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-20-33_Run0045_LLKf000.1489_LLK000.1770_SupportThreshold0.28445.cxi
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-29-38_Run0051_LLKf000.1484_LLK000.1761_SupportThreshold0.29009.cxi
Loading: flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T11-29-31_Run0091_LLKf000.1479_LLK000.1761_SupportThreshold0.29972.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T11-29-31_Run0091_LLKf000.1479_LLK000.1761_SupportThreshold0.29972.cxi] - this may take a while
R_match(0, 1) = 25.270% [4 arrays remaining]
R_match(0, 2) = 30.431% [3 arrays remaining]
R_match(0, 3) = 27.964% [2 arrays remaining]
R_match(0, 4) = 32.044% [1 arrays remaining]
R_match(0, 5) = 28.443% [0 arrays remaining]
Elapsed time:   44.3s
Analysing modes
First mode represents 95.825%
Saving modes analysis to: modes.h5
````

# Running modes on good

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-52-25_Run0026_LLKf000.1488_LLK000.1768_SupportThreshold0.28666.cxi
Loading: good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-58-22_Run0030_LLKf000.1478_LLK000.1759_SupportThreshold0.29790.cxi
Loading: good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T10-25-03_Run0048_LLKf000.1482_LLK000.1760_SupportThreshold0.29647.cxi
Loading: good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T11-39-24_Run0098_LLKf000.1484_LLK000.1771_SupportThreshold0.29768.cxi
Calculating modes from the imported objects
Matching arrays against the first one [good/S1408_pynx_norm_128_300_294_1_1_1-2021-01-13T09-58-22_Run0030_LLKf000.1478_LLK000.1759_SupportThreshold0.29790.cxi] - this may take a while
R_match(0, 1) = 31.439% [2 arrays remaining]
R_match(0, 2) = 28.578% [1 arrays remaining]
R_match(0, 3) = 30.956% [0 arrays remaining]
Elapsed time:   29.0s
Analysing modes
First mode represents 95.961%
Saving modes analysis to: modes.h5
````