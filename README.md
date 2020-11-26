# Welcome 

## This github is focused on the scripts that will be used during my thesis

contact : david.simonne@synchrotron-soleil.fr

# Identification
cmd:
`ssh -X -p 5022 simonne@firewall.esrf.fr`

NoMachine:
`ssh -X -p 5622 simonne@firewall.esrf.fr`



# BCDI

## Sur slurm

`ssh -X simonne@slurm-access`

Demande GPU

`srun -N 1 --partition=p9gpu --gres=gpu:1 --time=06:00:00 --pty bash`

Activer environnement virtuel

%`source /sware/exp/pynx/devel.p9/bin/activate`    NO bcdi

`source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate`

## Sur id01 / rnice

Cluster : nice

`ssh -X simonne@rnice9`

`source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate`

## pre_processing: OK sur le pc, pas sur le cluster

`python preprocess_bcdi_sixs2019.py`


## post_processing: not ok
slurm, gpu, pynxgap

*python strain.py* does not create the necessary figures
AttributeError: module bcdi.postprocessing.postprocessing_utils has no atribute 'remove_offset'


# PyNX

## Sur lid01

`ssh -X -p 5022 simonne@firewall.esrf.fr`

`ssh -X simonne@lid01gpu1`

`cd /data/id01/inhouse/david/analysis/RESULTS/s553/pynxraw`

`source /sware/exp/pynx/devel.debian9/bin/activate`

`pynx-id01cdi.py pynx-cdi-input_try0.txt`

## Sur slurm

`ssh -X simonne@slurm-access`

Demande GPU

`srun -N 1 --partition=p9gpu --gres=gpu:1 --time=06:00:00 --pty bash`

Activer environnement virtuel

`source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate`

# Additional notes
use `gedit` in linux