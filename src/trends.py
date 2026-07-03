import numpy as np

def long_term_trend(unique_years, yearly_means):
    """
    Perform linear regression to calculate the long-term annual temperature trend.
    Uses a 1st-degree polynomial (y = mx + b) where the slope represents the change per year.
    """
    years_numeric = unique_years.astype(int)
    coeffs = np.polyfit(years_numeric, yearly_means, 1)
    trend_slope = coeffs[0]
    return trend_slope

def extreme_years(unique_years, yearly_means):
    """
    Identify the hottest and coldest years from the yearly averages.
    """
    hottest_year = unique_years[np.argmax(yearly_means)]
    coldest_year = unique_years[np.argmin(yearly_means)]
    return hottest_year, coldest_year