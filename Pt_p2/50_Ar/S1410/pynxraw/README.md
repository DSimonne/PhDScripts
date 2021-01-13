# Running pynx

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-id01cdi.py pynx-run-no-support.txt 
--------------------------------------------------------------------------
No OpenFabrics connection schemes reported that they were able to be
used on a specific port.  As such, the openib BTL (OpenFabrics
support) will be disabled for this port.

  Local host:           p9-07
  Local device:         mlx5_0
  Local port:           1
  CPCs attempted:       udcm
--------------------------------------------------------------------------
Using parameters file:  pynx-run-no-support.txt
data S1410_pynx_norm_128_300_294_1_1_1.npz
mask S1410_maskpynx_norm_128_300_294_1_1_1.npz
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

Loading data:  S1410_pynx_norm_128_300_294_1_1_1.npz
Finished loading iobs data, with size: 11289600
Data CXI file already exists, not overwriting:  S1410_pynx_norm_128_300_294_1_1_1.cxi
CDI runner: preparing processing unit
Computing speed for available CUDA GPU [ranking by global memory bandwidth]:
                                        Tesla V100-SXM2-32GB:   31 Gb,   722 Gbytes/s
                                        Tesla V100-SXM2-32GB:   31 Gb,   722 Gbytes/s
Using CUDA GPU: Tesla V100-SXM2-32GB
Loading mask from:  S1410_maskpynx_norm_128_300_294_1_1_1.npz
Initialized mask, with 916043 pixels masked ( 8.114%)
Rebinning Iobs with rebin=(1,1,1)
Ignoring rebin=1
No support given. Will use autocorrelation to estimate initial support
Centering & reshaping data: (128, 300, 294) -> (128, 300, 294)
````

# Running modes on all

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-20-47_Run0003_LLKf000.1412_LLK000.1527_SupportThreshold0.29196.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-31-14_Run0010_LLKf000.1409_LLK000.1528_SupportThreshold0.28959.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-41-40_Run0017_LLKf000.1406_LLK000.1527_SupportThreshold0.29715.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-50-37_Run0023_LLKf000.1409_LLK000.1526_SupportThreshold0.29957.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-23-17_Run0045_LLKf000.1413_LLK000.1532_SupportThreshold0.28170.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-46-57_Run0061_LLKf000.1405_LLK000.1527_SupportThreshold0.29760.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-49-58_Run0063_LLKf000.1408_LLK000.1528_SupportThreshold0.29584.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-12-24_Run0078_LLKf000.1409_LLK000.1528_SupportThreshold0.29699.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-18-25_Run0082_LLKf000.1409_LLK000.1526_SupportThreshold0.29735.cxi
Loading: S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-38-40_Run0096_LLKf000.1410_LLK000.1529_SupportThreshold0.29221.cxi
Calculating modes from the imported objects
Matching arrays against the first one [S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-46-57_Run0061_LLKf000.1405_LLK000.1527_SupportThreshold0.29760.cxi] - this may take a while
R_match(0, 1) = 29.721% [8 arrays remaining]
R_match(0, 2) = 29.262% [7 arrays remaining]
R_match(0, 3) = 30.280% [6 arrays remaining]
R_match(0, 4) = 27.460% [5 arrays remaining]
R_match(0, 5) = 23.484% [4 arrays remaining]
R_match(0, 6) = 28.577% [3 arrays remaining]
R_match(0, 7) = 25.660% [2 arrays remaining]
R_match(0, 8) = 32.849% [1 arrays remaining]
R_match(0, 9) = 23.604% [0 arrays remaining]
Elapsed time:   85.4s
Analysing modes
First mode represents 95.793%
Saving modes analysis to: modes.h5
````

# Running modes on good

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-20-47_Run0003_LLKf000.1412_LLK000.1527_SupportThreshold0.29196.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-31-14_Run0010_LLKf000.1409_LLK000.1528_SupportThreshold0.28959.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-23-17_Run0045_LLKf000.1413_LLK000.1532_SupportThreshold0.28170.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-46-57_Run0061_LLKf000.1405_LLK000.1527_SupportThreshold0.29760.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-49-58_Run0063_LLKf000.1408_LLK000.1528_SupportThreshold0.29584.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-12-24_Run0078_LLKf000.1409_LLK000.1528_SupportThreshold0.29699.cxi
Loading: good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-38-40_Run0096_LLKf000.1410_LLK000.1529_SupportThreshold0.29221.cxi
Calculating modes from the imported objects
Matching arrays against the first one [good/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T10-46-57_Run0061_LLKf000.1405_LLK000.1527_SupportThreshold0.29760.cxi] - this may take a while
R_match(0, 1) = 29.721% [5 arrays remaining]
R_match(0, 2) = 29.262% [4 arrays remaining]

R_match(0, 3) = 23.484% [3 arrays remaining]
R_match(0, 4) = 28.577% [2 arrays remaining]
R_match(0, 5) = 25.660% [1 arrays remaining]
R_match(0, 6) = 23.604% [0 arrays remaining]
Elapsed time:   54.0s
Analysing modes
First mode represents 96.283%
Saving modes analysis to: modes.h5
````

# Running modes on flipped

````bash
(devel.p9) p9-07:40_Ar_10_O2/S1399/pynxraw % python pynx-cdi-analysis.py flipped/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T* modes=1
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
Loading: flipped/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-41-40_Run0017_LLKf000.1406_LLK000.1527_SupportThreshold0.29715.cxi
Loading: flipped/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-50-37_Run0023_LLKf000.1409_LLK000.1526_SupportThreshold0.29957.cxi
Loading: flipped/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T11-18-25_Run0082_LLKf000.1409_LLK000.1526_SupportThreshold0.29735.cxi
Calculating modes from the imported objects
Matching arrays against the first one [flipped/S1410_pynx_norm_128_300_294_1_1_1-2021-01-13T09-41-40_Run0017_LLKf000.1406_LLK000.1527_SupportThreshold0.29715.cxi] - this may take a while
R_match(0, 1) = 25.961% [1 arrays remaining]
R_match(0, 2) = 25.275% [0 arrays remaining]
Elapsed time:   19.7s
Analysing modes
First mode represents 97.591%
Saving modes analysis to: modes.h5
````