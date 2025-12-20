import numpy as np

def  basic_statistics(temperatures):
    """ Compute mean, max, min temperatures. """
    mean_temp = np.mean(temperatures)
    max_temp = np.max(temperatures)
    min_temp = np.min(temperatures)

    return mean_temp, max_temp, min_temp