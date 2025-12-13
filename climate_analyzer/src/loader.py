import numpy as np

def load_data(filepath ='data/climate.csv'):
    """ Load climate dataset and clean empty temperature values """
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1, dtype=str)
    dates = data[:,0] # First column -> dates (YYYY-MM-DD)
    temp_raw = data[:,1]  # Second column -> mean temperature

    # Remove empty temperature values
    valid_mask = temp_raw != ""
    temperatures = temp_raw[valid_mask].astype(float)
    dates = dates[valid_mask]

    return dates, temperatures

