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
    Generate an interactive, responsive animated world map using Plotly and save as HTML.
    Fixes colorbar jumping by anchoring limits and forces responsive scaling.
    """
    # Group and calculate annual means per country
    df_yearly = df_country.groupby(['Country', 'Year'], as_index=False)['AverageTemperature'].mean()

    # Establish absolute bounds from the entire dataset
    # This prevents the colorbar numbers and scale from changing dynamically during animation frames.
    abs_min = float(df_yearly['AverageTemperature'].min())
    abs_max = float(df_yearly['AverageTemperature'].max())

    fig = px.choropleth(
        df_yearly,
        locations="Country",
        locationmode="country names",
        color="AverageTemperature",
        hover_name="Country",
        animation_frame="Year",
        color_continuous_scale=px.colors.sequential.OrRd,
        range_color=[abs_min, abs_max]  # Hard-anchors the scale globally
    )

    # Ensure responsive viewport configuration and styling
    fig.update_layout(
        coloraxis_colorbar=dict(
            title="Temp (°C)",
            thicknessmode="pixels", thickness=15,
            lenmode="fraction", len=0.75
        ),
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="equirectangular"
        ),
        margin=dict(l=0, r=0, t=40, b=0),  # Removes wasted blank spaces around the map
        autosize=True  # Forces plotly core to adjust mathematically to container bounding boxes
    )

    # Inject direct HTML/CSS structural wrappers for raw browser responsiveness
    # Plotly's standard output uses a fixed pixel div. We wrap it in a clean fluid viewport contract.
    config = {'responsive': True}

    # Get raw HTML component representation from plotly engine
    raw_html = fig.to_html(include_plotlyjs='cdn', full_html=False, config=config)

    # Standard engineering template for web component scaling
    responsive_html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Global Temperature Simulation Dashboard</title>
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background-color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}
        .map-container {{
            width: 100vw;
            height: 100vh;
            display: block;
        }}
        /* Target internal plotly dynamic layouts to maintain strict 100% distribution */
        .plotly-graph-div {{
            width: 100% !important;
            height: 100% !important;
        }}
    </style>
</head>
<body>
    <div class="map-container">
        {raw_html}
    </div>
</body>
</html>
"""
    # Write the high-fidelity engineering bundle directly to disk
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(responsive_html_template)