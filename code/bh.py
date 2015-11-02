#!/usr/bin/env python3
import numpy as np
import nibabel as nib
import matplotlib as mpl
import matplotlib.pyplot as plt
img = nib.load('./data/run1.nii.gz')
data = img.get_data()
mpl.style.use('bmh')
fig, ax = plt.subplots(1)
ax.plot(data[32, 32, 15])
ax.set_xlabel('Time (TR)')
ax.set_ylabel('fMRI signal (a.u.)')
