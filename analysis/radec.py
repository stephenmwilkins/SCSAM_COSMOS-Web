import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# --- make a simple redshift histogram of galaxies in the sample


filename = 'Minal'

# --- open the HDF5 file
cat = h5py.File(f'../data/{filename}.h5', 'r')

z = cat['lightcone/redshift'][()] # the redshift of the galaxy

ra = cat['lightcone/ra'][()] # right ascension
dec = cat['lightcone/dec'][()] # declination

# --- shift the central ra to make it easier for now
ra = ra + 10.
ra[ra>360] = ra[ra>360] - 360

# --- get min, median, max
for nm, x in zip(['ra','dec'],[ra,dec]):
    print(nm, '-'*10)
    for fun in [np.min, np.median, np.max]:
        print(fun.__name__, f'{fun(x):.2f}')






fig = plt.figure(figsize = (8, 8)) # 4" x 4" square

left  = 0.15
bottom = 0.15
width = 0.8 # space left for a colour bar
height = 0.8 # space left for a colour bar

ax = fig.add_axes((left, bottom, width, height)) # add an axis

ax.scatter(ra, dec, s=1, lw=0, alpha = 0.01)

ax.set_xlabel(r'$\rm ra$') # colour notation is e.g. Y-J
ax.set_ylabel(r'$\rm dec$') # colour notation is e.g. Y-J

fig.savefig(f'radec.png')

fig.clf() # clear figure

fig.clf() # clear figure
