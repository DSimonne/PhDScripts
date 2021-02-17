# Strain plotting

```bash
(linux.BCDI_MI) david@pc-momonne:~/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3$ python Scripts/strain-SIXS_local_merlin.py NoGas 1337
Scan (s): 1337
Data dir: NoGas
### ReadNxs3 ###
### End of ReadNxs3 ###

#########
Scan 1337
#########

##############
Setup instance
##############
Setup(beamline='SIXS_2019', beam_direction=[1. 0. 0.], energy=8500, distance=1.18, outofplane_angle=0.326,
inplane_angle=37.938, tilt_angle=0.005, rocking_angle='inplane', grazing_angle=(0, 0), pixel_x=5.5e-05,
pixel_y=5.5e-05, direct_beam=None, sample_offsets=(0, 0, 0), filtered_data=False, custom_scan=False,
custom_images=None,
custom_monitor=None,
custom_motors=None,
sample_inplane=(1, 0, 0), sample_outofplane=(0, 0, 1), offset_inplane=0)

#################
Detector instance
#################
Detector(name='Merlin', unbinned_pixel=(5.5e-05, 5.5e-05), nb_pixel_x=515, nb_pixel_y=515, binning=(1, 1, 1),
roi=[0, 515, 0, 515], sum_roi=[0, 515, 0, 515], preprocessing_binning=(1, 1, 1), is_series=False
rootdir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/,
datadir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/data/,
scandir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/,
savedir = /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/result/,
sample_name = S, template_file = Pt_Al2O3_ascan_mu_%05d_R.nxs, template_imagefile = Pt_Al2O3_ascan_mu_%05d_R.nxs, specfile = /home/david/anaconda3/envs/linux.BCDI_MI/lib/python3.9/site-packages/bcdi-0.0.10a2-py3.9.egg/bcdi/preprocessing/alias_dict_2021.txt,


###############
Processing data
###############
Initial data size: ( 200 , 280 , 360 )
FFT size before accounting for phasing_binning (200, 280, 360)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (200, 280, 360)
Data shape used for orthogonalization and plotting: ( 176 , 178 , 188 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD_local/PhDScripts/id01_save/SIXS_Jan/Pt_Al2O3/NoGas/S1337/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range)) ~  8 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.017 0.015 0.035 ) rad
Max FFT= 4622808.042716527
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 4622808.042716527

Shape before orthogonalization (176, 178, 188)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 11.13 nm, 11.18 nm, 12.06 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0057 deg, 86.52 um, 105.32 um)
Sanity check, recalculated direct space voxel sizes: ( 11.13 nm, 11.18 nm, 12.06 nm )
out-of plane detector angle=0.326 deg, inplane_angle=37.938 deg
using SIXS geometry
rocking angle is mu, beta=0.000 deg
VTK spacing : (11.129109491392002, 11.176657010197765, 12.05818499657052) (nm)

Angle between q and y = 89.50 deg
Angle with y in zy plane = -88.46 deg
Angle with y in xy plane = -89.47 deg
Angle with z in xz plane = 108.97 deg

Normalized wavevector transfer [z, y, x]: [-0.32506635  0.00875166  0.94565072]
Wavevector transfer: (angstroms) 2.8006
Atomic plane distance: (angstroms) 2.2435 angstroms
center of mass at (z, y, x): ( 84.88 , 90.85 , 95.05 )
center of mass offset: ( 3 , -2 , -1 ) pixels
Support limits (start_z, stop_z, start_y, stop_y, start_x, stop_x):60, 120, 62, 118, 73, 118
Support limits (start_z, stop_z, start_y, stop_y, start_x, stop_x):60, 120, 62, 118, 73, 118
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.002 -0.025 0.032 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size: (11.13, 11.18, 12.06) (nm)
Final data shape: 176 178 188
Phase extent before and after thresholding: 5.90,4.02
phase.max() = 1.59 at voxel (87, 154, 53)
End of script
```