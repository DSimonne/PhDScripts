# Experiment details
Cristal D mesuré sur SixS :

flow: 40 ml/min Ar, 10 ml/min O2
1398, 1399, 1400, 1401

flow: 50 ml/min Ar
1404, 1406, 1408, 1410

flow: 5 ml/min CO, 45 ml/min Ar
S1414

Les fichiers nexus sont dans :
/data/id01/inhouse/otherlightsources/2019_sixs_nobackup/Pt_p2

1) si le champ de déplacement et le strain évoluent pour une condition de gaz donnée.
2) si ils évoluent d'une condition à l'autre.

# BCDI

* run once, check that the peak is well centered, if not run again after changing roi in file

Install BCDI inside the conda encironment and not in .local
* Go to the location of the virtual environment (for me: /users/mrichard/anaconda3/envs/bcdiDevel.conda/ )
* mkdir dev
* cd dev
* `git clone https://github.com/carnij/bcdi.git`
* cd bcdi
* conda activate my_env
* python3 setup.py install

# PyNX 

* use kernel pynxenv on jupyter notebook and try operator approach
* also work with command line scripts


The output of pynx without an input support are conjugate objects of each others, meaning that 50% of results are flipped compared to the others


# Data analysis
Weird chunks of particle missing, do an analysis of the evolution as a function of gas flow