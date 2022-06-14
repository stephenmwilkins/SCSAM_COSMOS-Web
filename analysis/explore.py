
import h5py

# This code simply opens the catalogue and tells you the available datasets

filename = 'Minal'

# --- open the HDF5 file
cat = h5py.File(f'../data/{filename}.h5', 'r')

# --- print all the datasets
cat.visititems(print)
