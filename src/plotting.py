import os
import matplotlib.pyplot as plt
import plotly.express as px


def plot_yearly_trend(unique_years, yearly_means, save_path):
    """
    Plot yearly average temperature trend and save to file.
    """
    years_numeric = unique_years.astype(int)

    plt.figure(figsize=(12, 6))
    plt.plot(years_numeric, yearly_means, marker='o', linestyle='-', color='orange')
    plt.title("Yearly Average Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(save_path)
    plt.close()


def plot_anomalies(unique_years, yearly_means, yearly_anomalies, save_path):
    """
    Plot anomalies on top of yearly average temperatures and save to file.
    """
    years_numeric = unique_years.astype(int)

    plt.figure(figsize=(12, 6))
    plt.plot(years_numeric, yearly_means, marker='o', linestyle='-', color='orange', label='Yearly Mean')

    for i, anomalies in enumerate(yearly_anomalies):
        if len(anomalies) > 0:
            plt.scatter([years_numeric[i]] * len(anomalies), anomalies, color='red',
                        label='Anomalies' if i == 0 else "")

    plt.title("Yearly Temperature with Anomalies")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(save_path)
    plt.close()


def plot_yearly_summary(years, yearly_means, yearly_anomalies, yearly_std, save_path):
    """
    Plot a combined summary graph showing mean, standard deviation variance band, and anomalies.
    Converts string years to integers to prevent horizontal X-axis text crowding.
    """
    years_numeric = years.astype(int)

    plt.figure(figsize=(12, 6))
    plt.plot(years_numeric, yearly_means, label='Yearly Mean', color='blue')

    # Fill the standard deviation area around the mean line
    plt.fill_between(years_numeric, yearly_means - yearly_std, yearly_means + yearly_std, color='orange', alpha=0.2,
                     label='Std dev')

    # Extract the primary anomaly value per year for visualization mapping
    anomaly_points = [a[0] if len(a) > 0 else None for a in yearly_anomalies]
    plt.scatter(years_numeric, anomaly_points, color='red', label='Anomalies', zorder=3)

    plt.title('Yearly Mean Temperature with Anomalies and Volatility')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(save_path)
    plt.close()


def plot_country_temperature_map(df_country, save_path):
    """
    Generate an interactive animated world map using Plotly and save as HTML.
    """
    df_yearly = df_country.groupby(['Country', 'Year'], as_index=False)['AverageTemperature'].mean()

    temp_min = df_yearly['AverageTemperature'].min()
    temp_max = df_yearly['AverageTemperature'].max()

    fig = px.choropleth(
        df_yearly,
        locations="Country",
        locationmode="country names",
        color="AverageTemperature",
        hover_name="Country",
        animation_frame="Year",
        color_continuous_scale=px.colors.sequential.OrRd
    )

    fig.update_traces(
        zmin=temp_min,
        zmax=temp_max,
        selector=dict(type='choropleth')
    )

    fig.update_layout(
        coloraxis_colorbar=dict(title="Temp (°C)"),
        geo=dict(showframe=False, showcoastlines=True)
    )

    fig.write_html(save_path)