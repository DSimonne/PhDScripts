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

## Strain analysis