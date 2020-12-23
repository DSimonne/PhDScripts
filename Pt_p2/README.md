# Experiment details
Cristal D mesuré sur SixS :

flow: 40 ml/min Ar, 10 ml/min O2
S1397, 1398, 1399, 1400, 1401

flow: 50 ml/min Ar
S1403, 1404, 1406, 1408, 1410

flow: 5 ml/min CO, 45 ml/min Ar
S1414

Les fichiers nexus sont dans :
/data/id01/inhouse/otherlightsources/2019_sixs_nobackup/Pt_p2

1) si le champ de déplacement et le strain évoluent pour une condition de gaz donnée.
2) si ils évoluent d'une condition à l'autre.

# BCDI environment
Use on rnice : 
`conda activate rnice.bcdi`

Advice for BCDI
* run once, check that the peak is well centered, if not run again after changing roi in file


# PyNX environment
## to do
* use kernel pynxenv on jupyter notebook and try operator approach
* also work with command line scripts

use `source /sware/exp/pynx/devel.p9/bin/activate` for pynx-cdi-analysis.py

# Kernels on slurm
* p9.widgets : optimisé pour utiliser les widgets et thorondor
* p9.bcdi : pour les scrips sur le terminal avec bcdi, comme strain.py  : `source /home/esrf/simonne/Documents/Environments/p9.bcdi/bin/activate`, inutile pour l'instant
* p9.pynx-devel : fonctionne pour pynx : `source /sware/exp/pynx/devel.p9/bin/activate`
* p9.pynx-gap : ne fonctionne pas pour modes.h5

# Local environments
* linux.bcdi works for all bcdi scripts, possible to also use on notebook for scripts, almost ok for strain

```(
linux.bcdi) david@ord00003:~/Documents/PhD/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw$ python strain_old.py
/home/david/Documents/PhD/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw/modes.h5
Initial data size: ( 128 , 300 , 294 )
FFT size before accounting for binning (128, 300, 294)
Binning used during phasing: (1, 1, 1)
Padding back to original FFT size (128, 300, 294)
Data shape used for orthogonalization and plotting: ( 182 , 188 , 192 )

Averaging using 1 candidate reconstructions

Opening  /home/david/Documents/PhD/PhDScripts/Pt_p2/50_Ar/S1404/pynxraw/modes.h5
This reconstruction will serve as reference object.

Average performed over  1 reconstructions

Extent of the phase over an extended support (ceil(phase range))~  58 (rad)
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( -0.016 0.586 -0.361 ) rad
Max FFT= 1542504.6122274657
Apodization using a 3d Blackman window
Max apodized FFT after normalization = 1542504.6122274657

Shape before orthogonalization (182, 188, 192)
Direct space voxel sizes (z, y, x) based on initial FFT shape: ( 9.25 nm, 11.24 nm, 12.39 nm )
Tilt, pixel_y, pixel_x based on cropped array shape: ( 0.0077 deg, 87.77 um, 84.22 um)
Sanity check, recalculated direct space voxel sizes: ( 9.25  nm, 11.24 nm, 12.39 nm )
using SIXS geometry
rocking angle is mu, with beta non zero
VTK spacing : 5.00 nm
Angle between q and y = 71.79132269042893 deg
Angle with y in zy plane -45.36658787319518 deg
Angle with y in xy plane -70.76682162800394 deg
Angle with z in xz plane 109.46236623829827 deg
Normalized wavevector transfer [z, y, x]: [-0.31650317  0.31247879  0.89564655]
Wavevector transfer: (angstroms) 2.6627
Atomic plane distance: (angstroms) 2.3597 angstroms
center of mass at (z, y, x): ( 87.22 , 94.53 , 96.42 )
center of mass offset: ( 4 , -1 , 0 ) pixels
Gradient: Phase_ramp_z, Phase_ramp_y, Phase_ramp_x: ( 0.001 -0.005 -0.001 ) rad

Aligning Q along  y : [0 1 0]
Rotating back the crystal in laboratory frame
Voxel size:  5.00 nm
Final data shape: 200 200 200
Phase extent before and after thresholding: 10.680021563201016 3.06318850840551
phase.max() =  1.5176890162824492 , at coordinates  96 29 138
Traceback (most recent call last):
  File "/home/david/anaconda3/envs/linux.bcdi/lib/python3.6/site-packages/bcdi-0.0.9-py3.6.egg/bcdi/graph/graph_utils.py", line 208, in combined_plots
TypeError: object of type 'NoneType' has no len()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "strain_old.py", line 706, in <module>
    tuple_scale='linear', cmap=my_cmap, is_orthogonal=True, reciprocal_space=False)
  File "/home/david/anaconda3/envs/linux.bcdi/lib/python3.6/site-packages/bcdi-0.0.9-py3.6.egg/bcdi/graph/graph_utils.py", line 210, in combined_plots
ValueError: "position" should be a tuple of subplot positions
```


id01 
no module named bcdi.graph.graph.utils