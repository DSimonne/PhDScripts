# Output of `preprocess_bcdi.py`

````bash
(BCDI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1397$ python preprocess_bcdi.py 
File has time stamps issues
File has time stamps issues

Scan 1397
Setup:  SIXS_2019
Detector:  Maxipix
Pixel number (VxH):  516 516
Detector ROI: [0, 303, 0, 296]
Horizontal pixel size with binning:  5.5e-05 m
Vertical pixel size with binning:  5.5e-05 m
Specfile:  /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1397/analysis/alias_dict.txt
Scan type:  inplane
Output will be non orthogonal, in the detector frame
Detector ROI loaded (VxH): 303 296
Detector physical size without binning (VxH): 516 516
Detector size with binning (VxH): 516 516
Loading frame 201
check_pixels(): initial number of masked pixels = 3966 on a total of 89688
check_pixels(): var_mean=50.84, 1/var_threshold=206.11
check_pixels(): number of zero variance hotpixels = 0
check_pixels(): number of pixels with too low variance = 0

0  negative data points masked
Intensity normalization using monitor
Monitor min, max, mean: 0.0, 0.0, 0.0
Data normalization by monitor.min()/monitor


Input data shape: 201 303 296
Max at (qx, qz, qy):  11 180 131
Data peak value =  34567.0627169585
Max symmetrical box (qx, qz, qy):  22 246 262
FFT box (qx, qz, qy):  (200, 300, 294)

Pad width: [0 0 0 0 0 0]

Data size after cropping / padding: 200 300 294
pause for pan/zoom
resume masking
pause for pan/zoom
resume masking
pause for pan/zoom
resume masking

Skipping median filtering

Data size after masking: 200 300 294

Data size after binning the stacking dimension: (200, 300, 294)

Saving directory: /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1397/pynxraw/

End of script
````