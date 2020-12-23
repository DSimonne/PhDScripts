# BCDI run, on linux laptop

```bash
(BCDI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2$ python 50_Ar/S1403/preprocess_bcdi.py 

Scan 1403
Setup:  SIXS_2019
Detector:  Maxipix
Pixel number (VxH):  516 516
Detector ROI: [0, 303, 0, 296]
Horizontal pixel size with binning:  5.5e-05 m
Vertical pixel size with binning:  5.5e-05 m
Specfile:  /home/david/Documents/PhD/PhDScripts/Pt_p2/50_Ar/S1403/analysis/alias_dict.txt
Scan type:  inplane
Output will be non orthogonal, in the detector frame
Detector ROI loaded (VxH): 303 296
Detector physical size without binning (VxH): 516 516
Detector size with binning (VxH): 516 516
Loading frame 203
check_pixels(): initial number of masked pixels = 3966 on a total of 89688
check_pixels(): var_mean=59.87, 1/var_threshold=208.15
check_pixels(): number of zero variance hotpixels = 0
check_pixels(): number of pixels with too low variance = 0

0  negative data points masked
Intensity normalization using monitor
Monitor min, max, mean: 0.0, 0.0, 0.0
Data normalization by monitor.min()/monitor


Input data shape: 203 303 296
Max at (qx, qz, qy):  0 176 131
Data peak value =  11810.0
Max symmetrical box (qx, qz, qy):  0 254 262
Empty images or presence of hotpixel at the border, defaulting fft_option to "skip"!

Pad width: [0 0 0 0 0 0]

Data size after cropping / padding: 203 303 296

Skipping median filtering

Data size after masking: 203 303 296

Data size after binning the stacking dimension: (203, 303, 296)

Saving directory: /home/david/Documents/PhD/PhDScripts/Pt_p2/50_Ar/S1403/pynxraw/

End of script
```

# PyNX run

On slurm, navigate to pynxraw folder, activate pynx environment

