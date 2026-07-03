import os
import numpy as np
from src.loader import load_data, load_country_data
from src.statistics import basic_statistics
from src.aggregations import yearly_averages, yearly_change
from src.anomalies import yearly_anomalies_and_std
from src.trends import long_term_trend, extreme_years
from src.utils import save_full_yearly_summary
from src.plotting import plot_yearly_trend, plot_anomalies, plot_yearly_summary, plot_country_temperature_map

# Paths configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'datasets')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'outputs')

CLIMATE_DATA_PATH = os.path.join(DATA_DIR, 'climate.csv')
COUNTRY_DATA_PATH = os.path.join(DATA_DIR, 'climate_by_country.csv')
SUMMARY_CSV_PATH = os.path.join(OUTPUT_DIR, 'yearly_summary.csv')

# Visualization output paths
TREND_PNG_PATH = os.path.join(OUTPUT_DIR, 'yearly_trend.png')
ANOMALIES_PNG_PATH = os.path.join(OUTPUT_DIR, 'yearly_anomalies.png')
SUMMARY_PNG_PATH = os.path.join(OUTPUT_DIR, 'yearly_summary.png')
MAP_HTML_PATH = os.path.join(BASE_DIR, 'docs', 'index.html')

# Load and clean data
dates, temperatures = load_data(CLIMATE_DATA_PATH)
print("Data loaded successfully")
print("Total records:", len(dates))

# Basic statistics
mean_temp, max_temp, min_temp = basic_statistics(temperatures)
print("\nGeneral Statistics")
print("Average temperature:", mean_temp)
print("Max temperature:", max_temp)
print("Min temperature:", min_temp)

# Yearly aggregation
unique_years, yearly_means = yearly_averages(dates, temperatures)
print("\nFirst 5 yearly averages:")
for i in range(5):
    print(unique_years[i], "->", yearly_means[i])

# Yearly anomalies and variability
yearly_std, yearly_anomalies = yearly_anomalies_and_std(np.array([d[:4] for d in dates]), temperatures, unique_years)
print("\nYearly anomalies (first 5 years):")
for i in range(5):
    print(unique_years[i], "->", yearly_anomalies[i])

print("\nYearly variability (std) - first 5 years:")
for i in range(5):
    print(unique_years[i], "->", yearly_std[i])

# Yearly temperature change
yearly_diff = yearly_change(yearly_means)
print("\nYearly temperature changes (first 5 years):")
for i in range(5):
    if i < len(yearly_diff):
        print(unique_years[i], "->", yearly_diff[i])

# Long-term trend
trend_slope = long_term_trend(unique_years, yearly_means)
print("\nLong-term trend analysis")
print("Temperature change per year:", trend_slope)

# Extreme years
hottest_year, coldest_year = extreme_years(unique_years, yearly_means)
print("\nExtreme years")
print("Hottest year:", hottest_year)
print("Coldest year:", coldest_year)

# Save everything as a CSV file
save_full_yearly_summary(
    SUMMARY_CSV_PATH,
    unique_years,
    yearly_means,
    yearly_std,
    yearly_diff,
    yearly_anomalies
)

# ===============================
# VISUALIZATIONS
# ===============================

# Trends & anomalies plots (Matplotlib)
plot_yearly_trend(unique_years, yearly_means, TREND_PNG_PATH)
plot_anomalies(unique_years, yearly_means, yearly_anomalies, ANOMALIES_PNG_PATH)
plot_yearly_summary(unique_years, yearly_means, yearly_anomalies, yearly_std, SUMMARY_PNG_PATH)

# Country-level interactive map (Plotly)
df_country = load_country_data(COUNTRY_DATA_PATH)
plot_country_temperature_map(df_country, MAP_HTML_PATH)