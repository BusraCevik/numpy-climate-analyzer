import numpy as np

'''
Performing long-term trend analysis using linear regression.
y = m*x + b
- y: yearly average temperatures (yearly_means)
- x: years as integers (years_numeric)
- m: slope of the line, represents temperature change per year
- b: intercept, starting point of the trend line on y-axis

np.polyfit(years_numeric, yearly_means, 1) fits a 1st-degree polynomial (a straight line) 
to the data. It returns an array of coefficients [m, b].
trend_slope = coeffs[0] extracts the slope 'm', which shows the long-term annual 
temperature change.
'''

def long_term_trend(unique_years, yearly_means):
    """Perform linear regression to find yearly temperature change."""
    years_numeric = unique_years.astype(int)
    coeffs = np.polyfit(years_numeric, yearly_means, 1)
    trend_slope = coeffs[0]
    return trend_slope

def extreme_years(unique_years, yearly_means):
    """Identify hottest and coldest years."""
    hottest_year = unique_years[np.argmax(yearly_means)]
    coldest_year = unique_years[np.argmin(yearly_means)]
    return hottest_year, coldest_year
