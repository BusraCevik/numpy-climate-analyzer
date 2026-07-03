import numpy as np

def yearly_anomalies_and_std(years, temperatures, unique_years):
    """
    Calculate yearly standard deviation and find anomalies using the 2-sigma rule.
    """
    yearly_std = []
    yearly_anomalies = []

    for year in unique_years:
        year_mask = years == year
        year_temps = temperatures[year_mask]

        year_mean = np.mean(year_temps)
        year_sigma = np.std(year_temps)
        yearly_std.append(year_sigma)

        # Detect days where temperature is further than 2 standard deviations from the mean
        anomalies_mask = np.abs(year_temps - year_mean) > (2 * year_sigma)
        anomalies = year_temps[anomalies_mask]
        yearly_anomalies.append(anomalies)

    return np.array(yearly_std), yearly_anomalies