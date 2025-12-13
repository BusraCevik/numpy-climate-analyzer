import numpy as np
import pandas as pd

def load_data(filepath ='data/datasets/climate.csv'):
    """ Load climate dataset and clean empty temperature values """
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1, dtype=str)
    dates = data[:,0] # First column -> dates (YYYY-MM-DD)
    temp_raw = data[:,1]  # Second column -> mean temperature

    # Remove empty temperature values
    valid_mask = temp_raw != ""
    temperatures = temp_raw[valid_mask].astype(float)
    dates = dates[valid_mask]

    return dates, temperatures

def load_country_data(filepath='data/datasets/climate_by_country.csv'):
    import pandas as pd
    df = pd.read_csv(filepath)
    df['dt'] = pd.to_datetime(df['dt'])
    df = df.dropna(subset=['AverageTemperature'])
    df['Year'] = df['dt'].dt.year
    return df

