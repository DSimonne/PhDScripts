#!C:\ProgramData\Anaconda3\python.exe
# -*- coding: utf-8 -*-

# PyNX - Python tools for Nano-structures Crystallography
#   (c) 2015-present : ESRF-European Synchrotron Radiation Facility
#       authors:
#         Julio Cesar da Silva (mailto: jdasilva@esrf.fr)
#         Vincent Favre-Nicolin, favre@esrf.fr

help_text = """
Perform an analysis of the resolution by comparing two images (objects from ptycho analysis)
using Fourier Shell (Ring) Correlation.

Example:
    pynx-resolution-FSC.py data1.cxi data2.cxi save_plot

command-line arguments: (all keywords are case-insensitive)
    data1.cxi data2.cxi (or data1.npz, data2.npz) : files including the original object, 
            either as a npz or CXI file produced by a PynX ptycho script.
            
    type=phase: calculate resolution angains the phase of the objects (the default)
                Alternatively, use type=amplitude
    
    subpixel: if used, this keyword will activate subpixel image registration.
"""

import os
import sys
import copy
from pynx.utils.matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fftn, ifftn, fftshift

try:
    import hdf5plugin
except:
    pass
import h5py

from skimage.feature import register_translation
from skimage.restoration import unwrap_phase
from scipy.ndimage.fourier import fourier_shift
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage.measurements import center_of_mass
from pynx.utils.fourier_shell_correlation import *
from pynx.utils.phase import minimize_grad_phase
from pynx.utils.plot_utils import cm_phase

params = {'save_plot': False, 'subpixel': False, 'snrt': [], 'type': 'phase'}


class FSCRunnerException(Exception):
    pass


class FSCRunner:
    """
    Class to process parameters from the command-line to analyse resolution from a couple of images.
    """

    def __init__(self, argv, params):
        """

        :param argv: the command-line parameters
        :param params: parameters for the optimization, with some default values.
        """
        self.params = copy.deepcopy(params)
        self.argv = argv
        self.parse_arg()
        self.check_params()
        self.image_filenames = None
        self.images = None
        self.pixel_size = None

    def parse_arg(self):
        """
        Parses the arguments given on a command line

        Returns: nothing

        """
        self.image_filenames = []
        for arg in self.argv:
            print(os.path.isfile(arg), os.path.splitext(arg)[-1])
            if os.path.isfile(arg) and os.path.splitext(arg)[-1] in ['.npz', '.cxi']:
                self.image_filenames.append(arg)
            elif arg.lower() in ['save_plot', 'subpixel']:
                self.params[arg.lower()] = True
            else:
                s = arg.find('=')
                if s > 0 and s < (len(arg) - 1):
                    k = arg[:s].lower()
                    v = arg[s + 1:]
                    print(k, v)
                    if k in ['snrt']:
                        self.params[k] = float(v)
                    elif k in ['type']:
                        self.params[k] = v
                    else:
                        print("WARNING: argument not interpreted: %s=%s" % (k, v))
                else:
                    if arg.find('.py') < 0:
                        print("WARNING: argument not interpreted: %s" % (arg))

    def check_params(self):
        """
        Check if self.params includes a minimal set of valid parameters

        Returns: Nothing. Will raise an exception if necessary
        """
        pass

    def run(self):
        """
        Run all the resolution analysis

        :return: Nothing
        """
        if len(self.image_filenames) != 2:
            print(self.image_filenames)
            raise FSCRunnerException(" There are more (or less) than two input images !")

        print("################################################################################################")
        print("Analysing the resolution by cross-correlation opf two images using Fourier Shell Correlation")
        print("Original Python code from Julio Cesar da Silva (mailto: jdasilva@esrf.fr)")
        print("Reference: van Heel & Schatz, J. Struct. Biol. 151 (2005), 250–62. doi:10.1016/j.jsb.2005.05.009")
        print("################################################################################################")

        # Load two images from ptychography scans
        if os.path.splitext(self.image_filenames[0])[-1] == 'npz':
            file1 = np.load(self.image_filenames[0])
            data1 = np.squeeze(file1["obj"])
            mask1 = file1["scan_area_obj"]
            if np.isscalar(file1['pixelsize']):
                pixel_size = float(file1['pixelsize'])
            else:
                pixel_size = np.array(file1['pixelsize']).mean()
        else:
            # Should be a CXI file
            h = h5py.File(self.image_filenames[0], 'r')
            # Find last entry in file
            i = 1
            while True:
                if 'entry_%d' % i not in h:
                    break
                i += 1
            entry = h['entry_%d' % (i - 1)]
            data1 = np.squeeze(entry['object/data'][()])
            mask1 = entry['object/mask'][()]
            pixel_size = (entry['probe/x_pixel_size'][()] + entry['probe/y_pixel_size'][()]) / 2

        if os.path.splitext(self.image_filenames[1])[-1] == 'npz':
            file2 = np.load(self.image_filenames[1])
            data2 = np.squeeze(file2["obj"])
            mask2 = file2["scan_area_obj"]
            if np.isscalar(file2['pixelsize']):
                pixel_size2 = float(file2['pixelsize'])
            else:
                pixel_size2 = np.array(file2['pixelsize']).mean()
        else:
            # Should be a CXI file
            h = h5py.File(self.image_filenames[1], 'r')
            # Find last entry in file
            i = 1
            while True:
                if 'entry_%d' % i not in h:
                    break
                i += 1
            entry = h['entry_%d' % (i - 1)]
            data2 = np.squeeze(entry['object/data'][()])
            mask2 = entry['object/mask'][()]
            pixel_size2 = (entry['probe/x_pixel_size'][()] + entry['probe/y_pixel_size'][()]) / 2

        if self.params['type'].lower() == 'phase':
            print("Analysing resolution from the PHASE of the images")
            # Remove phase gradient
            print("Removing phase gradient from both images")
            data1 = minimize_grad_phase(data1, mask=(mask1 < 0.5), center_phase=0, global_min=False, rebin_f=2)[0]
            data2 = minimize_grad_phase(data2, mask=(mask2 < 0.5), center_phase=0, global_min=False, rebin_f=2)[0]
            image1 = unwrap_phase(np.angle(data1))
            image2 = unwrap_phase(np.angle(data2))
            cm_imshow = cm_phase
        else:
            print("Analysing resolution from the AMPLITUDE of the images")
            # Analyse amplitude
            image1 = abs(data1)
            image2 = abs(data2)
            cm_imshow = 'gray'

        # get the pixel size
        print("Pixel size of data1 is %.2f nm" % (pixel_size * 1e9))
        print("Pixel size of data2 is %.2f nm" % (pixel_size2 * 1e9))

        # Scale according to 1-99%, otherwise correlation can be artificially high with a low contrast !
        # TODO: more systematic scaling and phase gradient compensation between the two images..
        print("Scaling the images to 5-95%% to normalize contrast")
        v1, v2 = np.percentile(image1[mask1 > 0.5], (5, 95))
        print(v1, v2)
        image1 = (image1 - v1) / (v2 - v1)
        v1, v2 = np.percentile(image2[mask2 > 0.5], (5, 95))
        print(v1, v2)
        image2 = (image2 - v1) / (v2 - v1)

        # cropping the image to an useful area
        ix0, ix1 = np.nonzero(mask1.sum(axis=0))[0][[0, -1]]
        dx = (ix1 - ix0) // 2 + 10
        x0 = (ix1 + ix0) // 2
        iy0, iy1 = np.nonzero(mask1.sum(axis=1))[0][[0, -1]]
        dy = (iy1 - iy0) // 2 + 10
        y0 = (iy1 + iy0) // 2
        image1 = image1[y0 - dy:y0 + dy, x0 - dx:x0 + dx]
        mask1 = mask1[y0 - dy:y0 + dy, x0 - dx:x0 + dx]
        ix0, ix1 = np.nonzero(mask2.sum(axis=0))[0][[0, -1]]
        x0 = (ix1 + ix0) // 2
        iy0, iy1 = np.nonzero(mask2.sum(axis=1))[0][[0, -1]]
        y0 = (iy1 + iy0) // 2
        image2 = image2[y0 - dy:y0 + dy, x0 - dx:x0 + dx]
        mask2 = mask2[y0 - dy:y0 + dy, x0 - dx:x0 + dx]

        # For manual access to data
        self.data1 = data1
        self.data2 = data2
        self.image1 = image1
        self.image2 = image2

        # Image registration
        print("Image registration")
        if mask1.ndim == 2:
            # TODO: take care of 3D data
            # Cut a square image completely inside the mask
            print("Using unmasked part of image for registration")
            c = center_of_mass(mask1)
            ny, nx = mask1.shape
            y, x = np.mgrid[0:ny, 0:nx]
            y0, x0 = int(c[0]), int(c[1])
            y -= y0
            x -= x0
            d = np.sqrt(x ** 2 + y ** 2).flatten()
            d0 = int(np.floor(d[np.nonzero((mask1 == 0).flat[d.argsort()])[0][0]] / np.sqrt(2)))
            if self.params['subpixel']:
                shift, error, diffphase = register_translation(image1[y0 - d0:y0 + d0], image2[y0 - d0:y0 + d0],
                                                               upsample_factor=100)
            else:
                shift, error, diffphase = register_translation(image1[y0 - d0:y0 + d0], image2[y0 - d0:y0 + d0])
            self.im1crop = image1[y0 - d0:y0 + d0]
            self.im2crop = image2[y0 - d0:y0 + d0]
        else:
            if self.params['subpixel']:
                shift, error, diffphase = register_translation(image1, image2, upsample_factor=100)
            else:
                shift, error, diffphase = register_translation(image1, image2)
        print("Detected pixel offset [y,x]: [%g, %g]" % (shift[0], shift[1]))
        offset_image2 = ifftn(fourier_shift(fftn(image2), shift))
        offset_mask2 = abs(ifftn(fourier_shift(fftn(mask2), shift)))

        regfsc = int(np.max(shift))
        img1 = image1[0 + regfsc:-1 - regfsc, 0 + regfsc:-1 - regfsc]
        img2 = offset_image2.real[0 + regfsc:-1 - regfsc, 0 + regfsc:-1 - regfsc]
        mask = (mask1 * offset_mask2)[0 + regfsc:-1 - regfsc, 0 + regfsc:-1 - regfsc] > 0.5
        self.mask = mask

        # Multiply (mask) images by Gaussian-filtered mask to avoid sharp border features
        sig = np.array(image1.shape) * 0.05
        sig[sig < 10] = 10
        self.g = gaussian_filter(mask.astype(np.float32), sig / 1.177, mode='constant', cval=0)

        if self.params['type'].lower() == 'phase' and img1.ndim == 2:
            # TODO: handle 3D case
            print("2D Phase images: minimization of the slope and contrast between images")
            # Find best plane fit to each image
            ny, nx = img1.shape
            y, x = np.mgrid[0:1:ny * 1j, 0:1:nx * 1j]
            # Image 1
            x1 = x[mask == 1]
            n = len(x1)
            x1 = x1.reshape((n, 1))
            y1 = y[mask == 1].reshape((n, 1))
            z1 = img1[mask == 1].reshape((n, 1))
            c1, res, rank, singul = np.linalg.lstsq(np.concatenate((x1, y1, np.ones((n, 1))), axis=1), z1)
            print("Image 1: found plane = %8.4fX + %8.4fY + %8.4f" % (c1[0], c1[1], c1[2]))
            self.img1corr = img1 - (x * c1[0] + y * c1[1] - c1[2])
            # Image 2
            z2 = img2[mask == 1].reshape((n, 1))
            c2, res, rank, singul = np.linalg.lstsq(np.concatenate((x1, y1, np.ones((n, 1))), axis=1), z2)
            print("Image 2: found plane = %8.4fX + %8.4fY + %8.4f" % (c2[0], c2[1], c2[2]))
            self.img2corr = img2 - (x * c2[0] + y * c2[1] - c2[2])

            img1 = self.img1corr
            img2 = self.img2corr

            # Least squares fit scale/shift of images
            z1 = self.img1corr[mask == 1]
            z2 = self.img2corr[mask == 1]
            alpha = ((z1 * z2).sum() - z1.sum() * z2.sum()) / ((z2 ** 2).sum() - z2.sum() ** 2)
            beta = z1.sum() - alpha * z2.sum()
            img2 = alpha * img2 + beta
            print("Scaling: img1 = %6.3f img2 + %6.3f" % (alpha, beta))

            # Re-do percentile with same parameters
            v1, v2 = np.percentile(img1[mask > 0.5], (5, 95))
            img1 = (img1 - v1) / (v2 - v1) * self.g
            img2 = (img2 - v1) / (v2 - v1) * self.g
        else:
            img1 *= self.g
            img2 *= self.g

        # For manual/debug access to images
        self.img1 = img1
        self.img2 = img2

        print("Estimating the resolution by Fourier Shell Correlation")
        # Use a minimal apodization since a mask has already been used from ptycho data
        FSC2D = FSCPlot(img1, img2, ring_thick=4, pixel_size=pixel_size, rad_apod=5, axial_apod=5)
        if self.params['save_plot']:
            n1 = os.path.splitext(os.path.split(self.image_filenames[0])[1])[0]
            n2 = os.path.splitext(os.path.split(self.image_filenames[1])[1])[0]
            n = "%s_%s-FSC.png" % (n1, n2)
            print("Saving figure to %s" % n)
        else:
            n = None
        print("Close plot window to exit")
        FSC2D.plot(save_plot=n, plot_images=True, cmap=cm_imshow)


if __name__ == '__main__':
    try:
        w = FSCRunner(sys.argv, params)
        w.parse_arg()
        w.check_params()
        w.run()
    except FSCRunnerException as ex:
        print(help_text)
        print('\n\n Caught exception: %s    \n' % (str(ex)))
        sys.exit(1)
