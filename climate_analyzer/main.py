import numpy as np
from src.loader import load_data, load_country_data
from src.statistics import basic_statistics
from src.aggregations import yearly_averages, yearly_change
from src.anomalies import yearly_anomalies_and_std
from src.trends import long_term_trend, extreme_years
from src.utils import save_full_yearly_summary
from src.plotting import plot_yearly_trend, plot_anomalies, plot_yearly_summary, plot_country_temperature_map


# 1️⃣ Load and clean data
dates, temperatures = load_data()
print("Data loaded successfully")
print("Total records:", len(dates))

# 2️⃣ Basic statistics
mean_temp, max_temp, min_temp = basic_statistics(temperatures)
print("\nGeneral Statistics")
print("Average temperature:", mean_temp)
print("Max temperature:", max_temp)
print("Min temperature:", min_temp)

# 3️⃣ Yearly aggregation
unique_years, yearly_means = yearly_averages(dates, temperatures)
print("\nFirst 5 yearly averages:")
for i in range(5):
    print(unique_years[i], "->", yearly_means[i])

# 4️⃣ Yearly anomalies and variability
yearly_std, yearly_anomalies = yearly_anomalies_and_std(np.array([d[:4] for d in dates]), temperatures, unique_years)
print("\nYearly anomalies (first 5 years):")
for i in range(5):
    print(unique_years[i], "->", yearly_anomalies[i])

print("\nYearly variability (std) - first 5 years:")
for i in range(5):
    print(unique_years[i], "->", yearly_std[i])

# 5️⃣ Yearly temperature change
yearly_diff = yearly_change(yearly_means)
print("\nYearly temperature changes (first 5 years):")
for i in range(5):
    if i < len(yearly_diff):
        print(unique_years[i], "->", yearly_diff[i])

# 6️⃣ Long-term trend
trend_slope = long_term_trend(unique_years, yearly_means)
print("\nLong-term trend analysis")
print("Temperature change per year:", trend_slope)

# 7️⃣ Extreme years
hottest_year, coldest_year = extreme_years(unique_years, yearly_means)
print("\nExtreme years")
print("Hottest year:", hottest_year)
print("Coldest year:", coldest_year)

# save everything as a csv file
save_full_yearly_summary(
    "yearly_summary.csv",
    unique_years,
    yearly_means,
    yearly_std,
    yearly_diff,
    yearly_anomalies
)


# Trends graph
plot_yearly_trend(unique_years, yearly_means)

# Anomalies graph
plot_anomalies(unique_years, yearly_means, yearly_anomalies)

# ===============================
# OPTIONAL VISUALIZATIONS
# ===============================

# Trends & anomalies plots (matplotlib)
plot_yearly_trend(unique_years, yearly_means)               # yearly_trend.png
plot_anomalies(unique_years, yearly_means, yearly_anomalies) # yearly_anomalies.png
plot_yearly_summary(unique_years, yearly_means, yearly_anomalies, yearly_std) # yearly_summary_plot.png

# Country-level interactive map (Plotly)
df_country = load_country_data()
plot_country_temperature_map(df_country) # interactive_country_map.html
