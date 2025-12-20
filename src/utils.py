import csv

def save_full_yearly_summary(filename, years, yearly_means, yearly_std, yearly_change, anomalies):
    """Save all yearly info to CSV inside data/ folder"""
    filepath = f"data/outputs/{filename}"
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            "Year", "Yearly_Mean", "Yearly_Std", "Yearly_Change", "Anomalies"
        ])
        for i, year in enumerate(years):
            change = yearly_change[i] if i < len(yearly_change) else ""
            writer.writerow([
                year,
                yearly_means[i],
                yearly_std[i],
                change,
                anomalies[i]
            ])