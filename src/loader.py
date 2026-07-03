import numpy as np
import pandas as pd


def load_data(filepath):
    """
    Load climate dataset and clean empty temperature values using NumPy.
    """
    data = np.genfromtxt(filepath, delimiter=',', skip_header=1, dtype=str)
    dates = data[:, 0]
    temp_raw = data[:, 1]

    # Filter out missing or empty temperature elements
    valid_mask = temp_raw != ""
    temperatures = temp_raw[valid_mask].astype(float)
    dates = dates[valid_mask]

    return dates, temperatures


def load_country_data(filepath):
    """
    Load country-level climate data using Pandas.
    Note: Pandas is used only here for easy date parsing and table operations,
    while the main project functions are fully built with NumPy.
    """
    df = pd.read_csv(filepath)
    df['dt'] = pd.to_datetime(df['dt'])

    # Remove rows where average temperature is missing
    df = df.dropna(subset=['AverageTemperature'])
    df['Year'] = df['dt'].dt.year

    return df