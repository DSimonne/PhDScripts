# Welcome 

## This github is focused on the scripts that will be used during my thesis

contact : david.simonne@synchrotron-soleil.fr

# Firewall
cmd:
`ssh -X -p 5022 simonne@firewall.esrf.fr`

NoMachine:
`ssh -X -p 5622 simonne@firewall.esrf.fr`


# Clusters

## ID01
`ssh -X simonne@lid01gpu1`

`cd /data/id01/inhouse/david/`

 BCDI | PyNX
------------ | -------------
`source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate` | `source /sware/exp/pynx/devel.debian9/bin/activate`


## rnice9
`ssh -X simonne@rnice9`

 BCDI | PyNX
------------ | -------------
`source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate` | 


## slurm
`ssh -X simonne@slurm-access`

**Demande GPU**

`srun -N 1 --partition=p9gpu --gres=gpu:1 --time=06:00:00 --pty bash`

 BCDI | PyNX
------------ | -------------
%`source /sware/exp/pynx/devel.p9/bin/activate`    NO bcdi | `source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate`


# SCRIPTS
## 	BCDI - pre_processing: OK on laptop

`python preprocess_bcdi_sixs2019.py`


## BCDI - post_processing: ok on lid01

*python strain.py* does not create the necessary figures on the laptop
AttributeError: module bcdi.postprocessing.postprocessing_utils has no atribute 'remove_offset'


## PyNX

`pynx-id01cdi.py pynx-cdi-input_try0.txt`