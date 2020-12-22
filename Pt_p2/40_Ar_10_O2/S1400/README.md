(BCDI) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400$ python preprocess_bcdi.py 
File has time stamps issues
File has time stamps issues

Scan 1400
Setup:  SIXS_2019
Detector:  Maxipix
Pixel number (VxH):  516 516
Detector ROI: [0, 303, 0, 296]
Horizontal pixel size with binning:  5.5e-05 m
Vertical pixel size with binning:  5.5e-05 m
Specfile:  /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400/analysis/alias_dict.txt
Scan type:  inplane
Output will be non orthogonal, in the detector frame
Detector ROI loaded (VxH): 303 296
Detector physical size without binning (VxH): 516 516
Detector size with binning (VxH): 516 516
Loading frame 129
check_pixels(): initial number of masked pixels = 3966 on a total of 89688
check_pixels(): var_mean=47.58, 1/var_threshold=132.65
check_pixels(): number of zero variance hotpixels = 0
check_pixels(): number of pixels with too low variance = 0

0  negative data points masked
Intensity normalization using monitor
Monitor min, max, mean: 0.0, 0.0, 0.0
Data normalization by monitor.min()/monitor


Input data shape: 129 303 296
Max at (qx, qz, qy):  64 180 131
Data peak value =  78905.14772976928
Max symmetrical box (qx, qz, qy):  128 246 262
FFT box (qx, qz, qy):  (128, 300, 294)

Pad width: [0 0 0 0 0 0]

Data size after cropping / padding: 128 300 294

Skipping median filtering

Data size after masking: 128 300 294

Data size after binning the stacking dimension: (128, 300, 294)

Saving directory: /home/david/Documents/PhD/PhDScripts/Pt_p2/40_Ar_10_O2/S1400/pynxraw/

End of script
