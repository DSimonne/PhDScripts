# Welcome 

## This github is focused on the scripts that will be used during my thesis

Contact : david.simonne@synchrotron-soleil.fr

# Files

All the *.cxi*, *.npz*, *.vti*, *.nxs*, *.h5* files are not included because they are too heavy.


# Clusters at ESRF

## Firewall
cmd:
`ssh -X -p 5022 <login>@firewall.esrf.fr`

NoMachine:
`ssh -X -p 5622 <login>@firewall.esrf.fr`

## ID01
`ssh -X <login>@lid01gpu1`

`cd /data/id01/inhouse/david/`

 BCDI | PyNX
------------ | -------------
`source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate` | `source /sware/exp/pynx/devel.debian9/bin/activate`


## rnice9
`ssh -X <login>@rnice9`

 BCDI | Paraview
------------ | -------------
`source /data/id01/inhouse/richard/bcdiDevel.debian9/bin/activate` | `source /sware/exp/paraview/envar.sh`
`conda activate rnice.bcdi` | `rnice8-1902:david/Pt_p2/pynxraw % paraview S1398_amp-disp-strain_gap_iso0.2_mode_avg3_apodize_blackman_lab-frame.vti`


## slurm
`ssh -X <login>@slurm-access`

Demande GPU

`srun -N 1 --partition=p9gpu --gres=gpu:1 --time=06:00:00 --pty bash`

 BCDI | PyNX
------------ | -------------
No bcdi | `source /data/id01/inhouse/richard/pynx-gap.p9/bin/activate` 
 | or `source /sware/exp/pynx/devel.p9/bin/activate`

### Kernels on slurm
* p9.widgets : optimisé pour utiliser les widgets et thorondor
* p9.bcdi : pour les scrips sur le terminal avec bcdi, comme strain.py  : `source /home/esrf/simonne/Documents/Environments/p9.bcdi/bin/activate`, inutile pour l'instant
* p9.pynx-devel : fonctionne pour pynx : `source /sware/exp/pynx/devel.p9/bin/activate`
* p9.pynx-gap : ne fonctionne pas pour modes.h5



# Cluster at SOLEIL

## sixs3
`ssh -X sixs3`

`df -h` (pour voir les disques accessibles)

`cd /nfs/ruche-sixs/sixs-soleil/com-sixs/David`

 BCDI | PyNX
------------ | -------------
Installed on python3 | Installed on python3

### IPython sur ligne

`xcat`

### Macros

`/nfs/ruche-sixs/sixs-soleil/com-sixs/2021/Shutdown5/test/`

On peut créer des macros et les lancer avec `do.run("<filename>")`
Ils doivent respecter la syntaxe python et se lisent ligne par ligne
Possible d'éditer les scripts de la ligne dans `cd python/`



# Local

## linux

 BCDI | PyNX
------------ | -------------
`conda activate linux.BCDI_MI` (update on 14/21/2021) | no pynx