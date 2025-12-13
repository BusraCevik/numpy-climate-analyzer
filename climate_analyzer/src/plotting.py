import matplotlib.pyplot as plt
import numpy as np


def plot_yearly_trend(unique_years, yearly_means, save_path="data/outputs/yearly_trend.png"):
    """Plot yearly average temperature trend and save to file"""
    years_numeric = unique_years.astype(int)

    plt.figure(figsize=(12, 6))
    plt.plot(years_numeric, yearly_means, marker='o', linestyle='-', color='orange')
    plt.title("Yearly Average Temperature Trend")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(save_path)  # save to data/ folder
    plt.show()


def plot_anomalies(unique_years, yearly_means, yearly_anomalies, save_path="data/outputs/yearly_anomalies.png"):
    """Plot anomalies on top of yearly average temperatures and save to file"""
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

    plt.savefig(save_path)  # save to data/ folder
    plt.show()
