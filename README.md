# Identification
cmd:
ssh -X -p 5022 simonne@firewall.esrf.fr

NoMachine:
ssh -X -p 5622 simonne@firewall.esrf.fr



# BCDI
## pre_processing: OK sur le pc, pas sur le cluster

Cluster : nice
ssh -X simonne@rnice9

Juste slurm, pas nice, even on NoMachine !!
ssh -X simonne@slurm-access

Demande GPU
srun -N 1 --partition=p9gpu --gres=gpu:1 --time=06:00:00 --pty bash

Activer environnement virtuel
%source /sware/exp/pynx/devel.p9/bin/activate   NO bcdi

source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate

`python preprocess_bcdi_sixs2019.py`

### Sur id01
source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate


## post_processing: not ok
slurm, gpu, pynxgap

`python strain.py` does not create the necessary figures
AttributeError: module bcdi.postprocessing.postprocessing_utils has no atribute 'remove_offset'


# PyNX: OK on lid01, not on other clusters
ssh -X -p 5022 simonne@firewall.esrf.fr

ssh -X simonne@lid01gpu1

source /sware/exp/pynx/devel.debian9/bin/activate

cd /data/id01/inhouse/david/analysis/RESULTS/s553/pynxraw

pynx-id01cdi.py pynx-cdi-input_try0.txt

## Additional notes
use `gedit` in linux
