import numpy as np

def yearly_averages(dates, temperatures):
    """ Compute yearly average temperatures """
    years = np.array([date[:4] for date in dates])
    unique_years = np.unique(years)

    yearly_means = []
    for year in unique_years:
        year_mask = years == year
        yearly_mean = np.mean(temperatures[year_mask])
        yearly_means.append(yearly_mean)

    return unique_years, np.array(yearly_means)

def yearly_change(yearly_means):
    """Compute year-to-year temperature change """
    return np.diff(yearly_means)