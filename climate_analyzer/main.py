import numpy as np

#load dataset
data = np.genfromtxt('data\climate.csv',
                     delimiter=',',
                     skip_header = 1,
                     dtype = str
)
print("Data loaded successfully")
print("Shape:", data.shape)

#select date and mean temperature columns
dates = data[:,0] #first column -> dates
temp_raw = data[:,1] #second column -> mean temperature

#remove empty temperature values
valid_mask = temp_raw != "" #temp_raw = ['3.0', '', '5.0'], valid_mask = [True, False, True]
temperatures = temp_raw[valid_mask].astype(float)
dates = dates[valid_mask]

print("\nFirst 5 dates:")
print(dates[:5])

print("\nFirst 5 temperatures:")
print(temperatures[:5])

# --- BASIC STATISTICS ---

mean_temp = np.mean(temperatures)
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

print("\nGeneral Statistics")
print("Average temperature:", mean_temp)
print("Max temperature:", max_temp)
print("Min temperature:", min_temp)

# --- YEARLY AVERAGE TEMPERATURE ---

years = np.array([date[:4] for date in dates])

unique_years = np.unique(years)
yearly_means = []

for year in unique_years:
    year_mask = years == year
    yearly_mean = np.mean(temperatures[year_mask])
    yearly_means.append(yearly_mean)
yearly_means =  np.array(yearly_means)

print("\nFirst 5 yearly averages:")
for i in range(5):
    print(unique_years[i]," -> ",yearly_means[i])

# --- YEARLY ANOMALIES ---

yearly_std = []
yearly_anomalies = []

for year in unique_years:
    year_mask = years == year
    year_temps = temperatures[year_mask]
    year_mean = np.mean(year_temps)
    year_sigma = np.std(year_temps)
    yearly_std.append(year_sigma)

    # anomalies = +2 values except std
    anomalies_mask = np.abs(year_temps - year_mean) > (2 * year_sigma)
    anomalies = year_temps[anomalies_mask]
    yearly_anomalies.append(anomalies)

yearly_std = np.array(yearly_std)
yearly_change = np.diff(yearly_means)

# anomalies example: ilk 5 yıl
print("\nYearly anomalies (first 5 years):")
for i in range(5):
    print(unique_years[i], " -> ", yearly_anomalies[i])

# yearly change example
print("\nYearly temperature changes (first 5 years):")
for i in range(5):
    if i < len(yearly_change):
        print(unique_years[i], " -> ", yearly_change[i])
