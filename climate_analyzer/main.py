import numpy as np

# ===============================
# LOAD DATASET
# ===============================

# Load climate dataset as string to handle missing values
data = np.genfromtxt(
    'data/climate.csv',
    delimiter=',',
    skip_header=1,
    dtype=str
)

print("Data loaded successfully")
print("Shape:", data.shape)

# ===============================
# DATA CLEANING
# ===============================

# Select date and temperature columns
dates = data[:, 0]          # First column -> dates (YYYY-MM-DD)
temp_raw = data[:, 1]       # Second column -> mean temperature

# Remove empty temperature values
valid_mask = temp_raw != "" #temp_raw = ['3.0', '', '5.0'] → valid_mask = [True, False, True] called boolean mask or filtering mask
temperatures = temp_raw[valid_mask].astype(float)
dates = dates[valid_mask]

print("\nFirst 5 dates:")
print(dates[:5])

print("\nFirst 5 temperatures:")
print(temperatures[:5])

# ===============================
# BASIC STATISTICS
# ===============================

mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("\nGeneral Statistics")
print("Average temperature:", mean_temp)
print("Max temperature:", max_temp)
print("Min temperature:", min_temp)

# ===============================
# YEARLY AGGREGATION
# ===============================

# Extract year from date strings
years = np.array([date[:4] for date in dates])

unique_years = np.unique(years)
yearly_means = []

# Compute yearly average temperature
for year in unique_years:
    year_mask = years == year
    yearly_mean = np.mean(temperatures[year_mask])
    yearly_means.append(yearly_mean)

yearly_means = np.array(yearly_means)

print("\nFirst 5 yearly averages:")
for i in range(5):
    print(unique_years[i], " -> ", yearly_means[i])

# ===============================
# YEARLY ANOMALIES & VARIABILITY
# ===============================

yearly_std = []
yearly_anomalies = []

for year in unique_years:
    year_mask = years == year
    year_temps = temperatures[year_mask]

    year_mean = np.mean(year_temps)
    year_sigma = np.std(year_temps)
    yearly_std.append(year_sigma)

    # Detect anomalies using 2-sigma rule
    anomalies_mask = np.abs(year_temps - year_mean) > (2 * year_sigma) #absolute value(tr. mutlak değer)
    anomalies = year_temps[anomalies_mask]
    yearly_anomalies.append(anomalies)

yearly_std = np.array(yearly_std)

print("\nYearly anomalies (first 5 years):")
for i in range(5):
    print(unique_years[i], " -> ", yearly_anomalies[i])

print("\nYearly variability (std) - first 5 years:")
for i in range(5):
    print(unique_years[i], " -> ", yearly_std[i])

# ===============================
# YEARLY TEMPERATURE CHANGE
# ===============================

# Year-to-year temperature differences
yearly_change = np.diff(yearly_means)

print("\nYearly temperature changes (first 5 years):")
for i in range(5):
    if i < len(yearly_change):
        print(unique_years[i], " -> ", yearly_change[i])

# ===============================
# LONG-TERM TREND ANALYSIS
# ===============================

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

# Convert years to numeric for regression
years_numeric = unique_years.astype(int)

# Linear regression: temperature trend over years
coeffs = np.polyfit(years_numeric, yearly_means, 1)
trend_slope = coeffs[0]

print("\nLong-term trend analysis")
print("Temperature change per year:", trend_slope)

# ===============================
# EXTREME YEARS
# ===============================

# Identify hottest and coldest years
hottest_year = unique_years[np.argmax(yearly_means)]
coldest_year = unique_years[np.argmin(yearly_means)]

print("\nExtreme years")
print("Hottest year:", hottest_year)
print("Coldest year:", coldest_year)
