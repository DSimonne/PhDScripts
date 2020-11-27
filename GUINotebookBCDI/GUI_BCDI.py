# -*- coding: utf-8 -*-
"""Try to provide a more user-friendly approach to the BCDI package, we make a jupyter notebook widget"""
try :
    import numpy as np
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import glob
    import errno
    import os
    import shutil
    import math

    import lmfit
    from lmfit import minimize, Parameters, Parameter
    from lmfit.models import LinearModel, ConstantModel, QuadraticModel, PolynomialModel, StepModel
    from lmfit.models import GaussianModel, LorentzianModel, SplitLorentzianModel, VoigtModel, PseudoVoigtModel
    from lmfit.models import MoffatModel, Pearson7Model, StudentsTModel, BreitWignerModel, LognormalModel, ExponentialGaussianModel, SkewedGaussianModel, SkewedVoigtModel, DonaichModel
    import corner
    import numdifftools
    from scipy.stats import chisquare

    import ipywidgets as widgets
    from ipywidgets import interact, Button, Layout, interactive, fixed
    from IPython.display import display, Markdown, Latex, clear_output

    from scipy import interpolate
    from scipy import optimize, signal
    from scipy import sparse

    from datetime import datetime
    from importlib import reload
    import pickle
    import inspect
    import warnings

    import tables as tb

    from matplotlib import rcParams
    rcParams['font.serif'] = 'Times'
    rcParams['font.size'] = '14'

except ModuleNotFoundError:
    raise ModuleNotFoundError("""The following packages must be installed: numpy, pandas, matplotlib, glob, errno, os, shutil, math, lmfit, corner, numdifftools, scipy, ipywidgets, importlib, pickle, inspect, warnings""")

# Dernière version de BCDI preprocess
from preprocess_bcdi_GUI import *

def GUI(
    scans, root_folder, sample_name, user_comment, debug, binning,
    flag_interact, background_plot,
    centering, fix_bragg, fix_size, center_fft, pad_size,
    normalize_flux, 
    mask_zero_event, flag_medianfilter, medfilt_order,
    reload_previous, reload_orthogonal, previous_binning, save_previous,
    save_rawdata, save_to_npz, save_to_mat, save_to_vti, save_asint,
    beamline, is_series, custom_scan, custom_images, custom_monitor, rocking_angle, follow_bragg, specfile_name,
    detector, x_bragg, y_bragg, photon_threshold, photon_filter, background_file, flatfield_file, hotpixels_file, template_imagefile,
    use_rawdata, correct_curvature, sdd, energy, custom_motors,
    beam_direction, sample_inplane, sample_outofplane, offset_inplane, sample_offsets, cch1, cch2, detrot, tiltazimuth, tilt,
    LAUNCH):
    if LAUNCH:
        for w in ListWidgets.children[:-2]:
            w.disabled = True

        # Reste des paramètres

        # roi_detector = []
        # roi_detector = [1202, 1610, x_bragg - 256, x_bragg + 256]  # HC3207  x_bragg = 430
        roi_detector = [y_bragg-160, y_bragg+160, x_bragg-160, x_bragg+160]  # [553, 1063, 1041, 1701]
        # roi_detector = [y_bragg - 168, y_bragg + 168, x_bragg - 140, x_bragg + 140]  # CH5309
        # roi_detector = [552, 1064, x_bragg - 240, x_bragg + 240]  # P10 2018
        # roi_detector = [y_bragg - 290, y_bragg + 350, x_bragg - 350, x_bragg + 350]  # PtRh Ar
        # [Vstart, Vstop, Hstart, Hstop]
        # leave it as [] to use the full detector. Use with center_fft='skip' if you want this exact size.

        # On lance BCDI
        print("BCDI logs : \n \n")
        Run_BCDI(scans, root_folder, sample_name, user_comment, debug, binning,
            flag_interact, background_plot,
            centering, fix_bragg, fix_size, center_fft, pad_size,
            normalize_flux, 
            mask_zero_event, flag_medianfilter, medfilt_order,
            reload_previous, reload_orthogonal, previous_binning, save_previous,
            save_rawdata, save_to_npz, save_to_mat, save_to_vti, save_asint,
            beamline, is_series, custom_scan, custom_images, custom_monitor, rocking_angle, follow_bragg, specfile_name,
            detector, x_bragg, y_bragg, roi_detector, photon_threshold, photon_filter, background_file, flatfield_file, hotpixels_file, template_imagefile,
            use_rawdata, correct_curvature, sdd, energy, custom_motors,
            beam_direction, sample_inplane, sample_outofplane, offset_inplane, sample_offsets, cch1, cch2, detrot, tiltazimuth, tilt)

    if not LAUNCH:
        for w in ListWidgets.children[:-2]:
            w.disabled = False

# Define widgets
try :
    root_path = os.getcwd()

    ## USER-DEFINED PARAMETERS INPUT AS WIDGETS
    ListWidgets = interactive(GUI,
        scans = widgets.BoundedIntText(
            value = "01305",
            description = 'Scan nb:',
            min = 0,
            max = 2000,
            disabled = False,
            continuous_update = False,
            layout=Layout(width='15%'),
            style = {'description_width': 'initial'}),

        root_folder = widgets.Text(
            value = os.getcwd(),
            placeholder = "path/to/data",
            description = 'Root folder',
            disabled = False,
            continuous_update = False,
            style = {'description_width': 'initial'}),

        sample_name = widgets.Text(
            value = "",
            placeholder = "",
            description = 'Sample Name',
            disabled = False,
            continuous_update = False,
            layout=Layout(width='15%'),
            style = {'description_width': 'initial'}),

        user_comment = widgets.Text(
            value = "",
            description = 'Comment',
            disabled = False,
            continuous_update = False,
            tooltip = "string, should start with _",
            style = {'description_width': 'initial'}),

        debug = widgets.ToggleButton(
            value = False,
            description = 'Debug',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to interact with plots, False to close it automatically',
            icon = 'check'),
        
        binning = fixed([1, 1, 1]),    # binning that will be used for phasing (stacking dimension, detector vertical axis, detector horizontal axis)

        ### Parameters used in masking 
        flag_interact = widgets.ToggleButton(
            value = True,
            description = 'Flag interact',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to interact with plots, False to close it automatically',
            icon = 'check'),

        background_plot = widgets.Text(
            value = "0.5",
            description = 'Background plot:',
            tooltip = "In level of grey in [0,1], 0 being dark. For visual comfort during masking",
            readout = True,
            style = {'description_width': 'initial'},
            disabled = False),


        ### Parameters related to data cropping/padding/centering
        centering  = widgets.Dropdown(
            options = ["max", "com"],
            value = "max",
            description = 'Centering:',
            disabled = False,
            tooltip = "Bragg peak determination: 'max' or 'com', 'max' is better usually. It will be overridden by 'fix_bragg' if not empty",
            style = {'description_width': 'initial'}),

        fix_bragg = fixed([]),  # fix the Bragg peak position [z_bragg, y_bragg, x_bragg] considering the full detector
        # It is useful if hotpixels or intense aliens. Leave it [] otherwise.
        fix_size = fixed([]),  # crop the array to predefined size considering the full detector,
        # leave it to [] otherwise [zstart, zstop, ystart, ystop, xstart, xstop]. ROI will be defaulted to []

        center_fft = widgets.Dropdown(
            options = ['crop_sym_ZYX','crop_asym_ZYX','pad_asym_Z_crop_sym_YX', 'pad_sym_Z_crop_asym_YX','pad_sym_Z', 'pad_asym_Z', 'pad_sym_ZYX','pad_asym_ZYX', 'skip'],
            value = "crop_asym_ZYX",
            description = 'Center FFT',
            disabled = False,
            style = {'description_width': 'initial'}),

        pad_size = fixed([]), 
        # size after padding, e.g. [256, 512, 512]. Use this to pad the array.
        # used in 'pad_sym_Z_crop_sym_YX', 'pad_sym_Z', 'pad_sym_ZYX'


        ### Parameters used in intensity normalization
        normalize_flux = widgets.Dropdown(
            options = ["skip", "monitor"],
            description = 'Normalize flux',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'Monitor to normalize the intensity by the default monitor values, skip to do nothing',
            icon = 'check',
            style = {'description_width': 'initial'}),


        ### Parameters for data filtering
        mask_zero_event = widgets.ToggleButton(
            value = False,
            description = 'Mask zero event',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'Mask pixels where the sum along the rocking curve is zero - may be dead pixels',
            icon = 'check'),

        flag_medianfilter = widgets.Dropdown(
            options = ['skip','median','interp_isolated', 'mask_isolated'],
            value = "skip",
            description = 'Flag median filter',
            disabled = False,
            tooltip = "set to 'median' for applying med2filter [3,3], set to 'interp_isolated' to interpolate isolated empty pixels based on 'medfilt_order' parameter, set to 'mask_isolated' it will mask isolated empty pixels, set to 'skip' will skip filtering",
            style = {'description_width': 'initial'}),

        medfilt_order = widgets.IntText(
            value = 8,
            description='Med filter order:',
            disabled = False,
            tooltip = "for custom median filter, number of pixels with intensity surrounding the empty pixel",
            style = {'description_width': 'initial'}),


        ### Parameters used when reloading processed dat
        reload_previous = widgets.ToggleButton(
            value = False,
            description = 'Reload previous',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to resume a previous masking (load data and mask)',
            icon = 'check'),

        reload_orthogonal = widgets.ToggleButton(
            value = False,
            description = 'Reload orthogonal',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True if the reloaded data is already intepolated in an orthonormal frame',
            icon = 'check'),

        previous_binning = fixed([1, 1, 1]),  # binning factors in each dimension of the binned data to be reloaded

        save_previous = widgets.ToggleButton(
            value = False,
            description = 'Save previous',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'if True, will save the previous data and mask',
            icon = 'check'),


        ### Saving options
        save_rawdata = widgets.ToggleButton(
            value = False,
            description = 'Save raw data',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'Save also the raw data when use_rawdata is False',
            icon = 'check'),

        save_to_npz = widgets.ToggleButton(
            value = True,
            description = 'Save to npz',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to save the processed data in npz format',
            icon = 'check'),

        save_to_mat = widgets.ToggleButton(
            value = False,
            description = 'Save to mat',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to save also in .mat format',
            icon = 'check'),

        save_to_vti = widgets.ToggleButton(
            value = True,
            description = 'Save to vti',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'Save the orthogonalized diffraction pattern to VTK file',
            icon = 'check'),

        save_asint = widgets.ToggleButton(
            value = False,
            description = 'Save as integers',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'if True, the result will be saved as an array of integers (save space)',
            icon = 'check'),


        ### Define beamline related parameters
        beamline = widgets.Dropdown(
            options = ['ID01', 'SIXS_2018', 'SIXS_2019', 'CRISTAL', 'P10', 'NANOMAX', '34ID'],
            value = "SIXS_2019",
            description = 'Beamline',
            disabled = False,
            tooltip = "Name of the beamline, used for data loading and normalization by monitor",
            style = {'description_width': 'initial'}),

        is_series = widgets.ToggleButton(
            value = False,
            description = 'Is series (P10)',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'specific to series measurement at P10',
            icon = 'check'),

        custom_scan = widgets.ToggleButton(
            value = False,
            description = 'Custom scan',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'set it to True for a stack of images acquired without scan, e.g. with ct in a macro, or when there is no spec/log file available',
            icon = 'check'),

        custom_images = fixed([3]),  # np.arange(11353, 11453, 1)  # list of image numbers for the custom_scan
        custom_monitor = fixed(np.ones(51)),  # monitor values for normalization for the custom_scan


        rocking_angle = widgets.Dropdown(
            options = ['inplane', 'outofplane', 'energy'],
            value = "inplane",
            description = 'Rocking angle',
            disabled = False,
            tooltip = "Name of the beamline, used for data loading and normalization by monitor",
            style = {'description_width': 'initial'}),

        follow_bragg = widgets.ToggleButton(
            value = False,
            description = 'Follow bragg',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'Only for energy scans, set to True if the detector was also scanned to follow the Bragg peak',
            icon = 'check'),

        specfile_name = widgets.Text(
            value = "alias_dict.txt",
            description = 'Specfile name',
            disabled = False,
            continuous_update = False,
            tooltip = """for ID01: name of the spec file without, for SIXS_2018: full path of the alias dictionnary, typically root_folder + 'alias_dict_2019.txt',
            .fio for P10, not used for CRISTAL and SIXS_2019""",
            style = {'description_width': 'initial'}),


        ### Detector related parameters
        detector = widgets.Dropdown(
            options = ["Eiger2M", "Maxipix", "Eiger4M", "Merlin", "Timepix"],
            value = "Maxipix",
            description = 'Detector',
            disabled = False,
            style = {'description_width': 'initial'}),

        # nb_pixel_y = 1614  # use for the data measured with 1 tile broken on the Eiger2M

        x_bragg = widgets.IntText(
            value = 160,
            description = 'X Bragg:',
            disabled = False,
            tooltip = "Horizontal pixel number of the Bragg peak, can be used for the definition of the ROI"),

        y_bragg = widgets.IntText(
            value = 325,
            description = 'Y Bragg:',
            disabled = False,
            tooltip = "Vertical pixel number of the Bragg peak, can be used for the definition of the ROI"),

        photon_threshold = widgets.IntText(
            value = 0,
            description = 'Photon Threshold:',
            disabled = False,
            tooltip = "data[data < photon_threshold] = 0",
            style = {'description_width': 'initial'}),

        photon_filter = widgets.Dropdown(
            options = ['loading','postprocessing'],
            value = "loading",
            description = 'Photon filter',
            disabled = False,
            tooltip = "When the photon threshold should be applied, if 'loading', it is applied before binning; if 'postprocessing', it is applied at the end of the script before saving",
            style = {'description_width': 'initial'}),

        background_file = widgets.Text(
            value = "",
            placeholder = "root_path + 'background.npz'",
            description = 'Background file',
            disabled = False,
            continuous_update = False,
            style = {'description_width': 'initial'}),

        flatfield_file = widgets.Text(
            value = "",
            placeholder = f"{root_path}flatfield_maxipix_8kev.npz",
            description = 'Flatfield file',
            disabled = False,
            continuous_update = False,
            style = {'description_width': 'initial'}),

        hotpixels_file = widgets.Text(
            value = f"{root_path}/mask1000dark.npz",
            placeholder = f"{root_path}/mask1000dark.npz",
            description = 'Hotpixels file',
            disabled = False,
            continuous_update = False,
            style = {'description_width': 'initial'}),

        template_imagefile = widgets.Text(
            value = 'Pt_ascan_mu_%05d.nxs',
            description = 'Template imagefile',
            disabled = False,
            tooltip = """Template for ID01: 'data_mpx4_%05d.edf.gz' or 'align_eiger2M_%05d.edf.gz'; Template for SIXS_2018: 'align.spec_ascan_mu_%05d.nxs'
                        ; Template for SIXS_2019: 'spare_ascan_mu_%05d.nxs'
                        ; Template for Cristal: 'S%d.nxs'
                        ; Template for P10: '_master.h5'
                        ; Template for NANOMAX: '%06d.h5'
                        ; Template for 34ID: 'Sample%dC_ES_data_51_256_256.npz'""",
            style = {'description_width': 'initial'}),

        ### Define parameters below if you want to orthogonalize the data before phasing
        use_rawdata = widgets.ToggleButton(
            value = True,
            description = 'Use Raw Data',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'False for using data gridded in laboratory frame/ True for using data in detector frame',
            icon = 'check'),

        correct_curvature = widgets.ToggleButton(
            value = False,
            description = 'Correct curvature',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            tooltip = 'True to correcture q values for the curvature of Ewald sphere',
            icon = 'check'),

        sdd = widgets.IntText(
            value = 1.8,
            description = 'Sample Detector Dist. (m):',
            disabled = False,
            tooltip = "sample to detector distance in m"),

        energy = widgets.IntText(
            value = 8300,
            description = 'X-ray energy in eV',
            disabled = False),
        # np.linspace(11100, 10900, num=51)

        # add a condition from beamline
        custom_motors = fixed({}),  # {"mu": 0, "phi": -15.98, "chi": 90, "theta": 0, "delta": -0.5685, "gamma": 33.3147}
        # use this to declare motor positions if there is not log file
        # example: {"eta": np.linspace(16.989, 18.989, num=100, endpoint=False), "phi": 0, "nu": -0.75, "delta": 36.65}
        # ID01: eta, phi, nu, delta
        # CRISTAL: mgomega, gamma, delta
        # SIXS: beta, mu, gamma, delta
        # P10: om, phi, chi, mu, gamma, delta
        # NANOMAX: theta, phi, gamma, delta, energy, radius
        # 34ID: mu, phi (incident angle), chi, theta (inplane), delta (inplane), gamma (outofplane)


        ### Parameters for xrayutilities to orthogonalize the data before phasing
        #xrayutilities uses the xyz crystal frame: for incident angle = 0, x is downstream, y outboard, and z vertical up

        beam_direction = fixed((1, 0, 0)),  # beam along z
        sample_inplane = fixed((1, 0, 0)),  # sample inplane reference direction along the beam at 0 angles
        sample_outofplane = fixed((0, 0, 1)),  # surface normal of the sample at 0 angles
        offset_inplane = fixed(0),  # outer detector angle offset, not important if you use raw data
        sample_offsets = fixed((-90, 0, 0)),  # tuple of offsets in degree of the sample around z (downstream), y (vertical up) and x
        # the sample offsets will be added to the motor values

        cch1 = fixed(1000),  # cch1 parameter from xrayutilities 2D detector calibration, vertical
        cch2 = fixed(1000),  # cch2 parameter from xrayutilities 2D detector calibration, horizontal

        # detector roi is taken into account below
        detrot = fixed(0),  # detrot parameter from xrayutilities 2D detector calibration
        tiltazimuth = fixed(0),  # tiltazimuth parameter from xrayutilities 2D detector calibration
        tilt =fixed(0), # tilt parameter from xrayutilities 2D detector calibration

        LAUNCH = widgets.ToggleButton(
            value = False,
            description = 'LAUNCH BCDI',
            disabled = False,
            button_style = '', # 'success', 'info', 'warning', 'danger' or ''
            icon = 'check')
    )
    ###################################
    # end of user-defined parameters #
    ###################################

    #Create the final window
    RowOneScan = widgets.HBox(ListWidgets.children[:4])
    RowTwoScan = widgets.HBox([ListWidgets.children[4]])

    TabScan = widgets.VBox([RowOneScan, RowTwoScan])

    
    TabMasking = widgets.HBox(ListWidgets.children[5:7])

    RowReduction = widgets.HBox(ListWidgets.children[7:9])
    RowNormalization = widgets.HBox([ListWidgets.children[9]])
    RowFiltering = widgets.HBox(ListWidgets.children[10:13])
    TabReduction = widgets.VBox([RowReduction, RowNormalization, RowFiltering])

    RowLoading = widgets.HBox(ListWidgets.children[13:16])
    RowSaving = widgets.HBox(ListWidgets.children[16:21])
    TabSaveLoad = widgets.VBox([RowSaving, RowLoading])

    RowOneBeamline = widgets.HBox(ListWidgets.children[21:24])
    RowTwoBeamline = widgets.HBox(ListWidgets.children[24:27])

    TabBeamline = widgets.VBox([RowOneBeamline, RowTwoBeamline])
    
    TabDetector = widgets.VBox([
        widgets.HBox(ListWidgets.children[27:30]),
        widgets.HBox(ListWidgets.children[30:32]),
        widgets.HBox(ListWidgets.children[32:34]),
        widgets.HBox(ListWidgets.children[34:36])
        ])


    TabOrtho = widgets.HBox(ListWidgets.children[36:40])
    
    TabXrayUtilities = widgets.HBox()

    TabLaunch = widgets.VBox([widgets.HBox([ListWidgets.children[-2]]), widgets.HBox([ListWidgets.children[-1]])])

    Window = widgets.Tab(children=[TabScan, TabMasking, TabReduction, TabSaveLoad, TabBeamline, TabDetector, TabOrtho, TabXrayUtilities, TabLaunch])
    Window.set_title(0, 'Scan detail')
    Window.set_title(1, "Masking")
    Window.set_title(2, "Data reduction")
    Window.set_title(3, "Data Loading/Saving")
    Window.set_title(4, 'Beamline related parameters')
    Window.set_title(5, 'Detector related parameters and region of interest')
    Window.set_title(6, 'Orthogonalization before phasing')
    Window.set_title(7, 'X-ray utilities')
    Window.set_title(8, 'Launch')

except Exception as e:
    raise e
