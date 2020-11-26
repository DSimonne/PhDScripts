# Logbook for Pt_p2

## Preprocessing the data
`preprocess_bcdi.py` was run to define a mask for the data. The environment was LAPTOP-David, I copied the variable values from `preprocess_bcdi_sisx2019_crystalD.py` but created a new preprocess file because of errors.

## Phase retrieval
 Output in \pynxraw

 `pynx-id01cdi.py` was run:
 	*the 5 best runs were kept
						nb_hio =  400
                        nb_raar =  1000
                          nb_er =  300
                          nb_ml =  0
                     positivity =  False
            support_only_shrink =  False
                           beta =  0.9
                         detwin =  False
                      live_plot =  100
          support_update_period =  20
     support_smooth_width_begin =  2.0
       support_smooth_width_end =  1.0
              support_threshold =  0.19765447624957455
       support_threshold_method =  rms
            support_post_expand =  (1, -2, 1)
 confidence_interval_factor_mask_min =  0.5
 confidence_interval_factor_mask_max =  1.2
                      zero_mask =  False
                        verbose =  100

Interesting fact : he removed by himself the *.cxi* file that he told me to read, it was the last one (nb 20), probably generic,

Cannot find the environment in which I can use silx view to I am copying the files back on my laptop.

## Create modes.h5
`python pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1`

DERNIERE ERREUR 

(pynx-gap.p9) p9-05:id01_david/Pt_p2/pynxraw % pynx-cdi-analysis.py S1398_pynx_norm_128_300_294_1_1_1-* modes=1
/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/skcuda/cublas.py:284: UserWarning: creating CUBLAS context to get version number
  warnings.warn('creating CUBLAS context to get version number')
Traceback (most recent call last):
  File "/data/id01/inhouse/richard/pynx-gap.p9/bin/pynx-cdi-analysis.py", line 4, in <module>
    __import__('pkg_resources').run_script('PyNX==2020.2b0', 'pynx-cdi-analysis.py')
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/pkg_resources/__init__.py", line 650, in run_script
    self.require(requires)[0].run_script(script_name, ns)
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/pkg_resources/__init__.py", line 1446, in run_script
    exec(code, namespace, namespace)
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/EGG-INFO/scripts/pynx-cdi-analysis.py", line 22, in <module>
    from pynx.cdi.cl_operator import PRTF
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/cdi/cl_operator.py", line 20, in <module>
    from ..processing_unit.cl_processing_unit import CLProcessingUnit
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/processing_unit/cl_processing_unit.py", line 38, in <module>
    class CLEvent(object):
  File "/data/id01/inhouse/richard/pynx-gap.p9/lib/python3.8/site-packages/PyNX-2020.2b0-py3.8.egg/pynx/processing_unit/cl_processing_unit.py", line 44, in CLEvent
    def __init__(self, event: cl.Event, nflop: int = 0, nbyte: int = 0):
NameError: name 'cl' is not defined
(pynx-gap.p9) p9-05:id01_david/Pt_p2/pynxraw % 


## Strain analysis