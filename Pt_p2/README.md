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
* linux.bcdi works for all bcdi scripts