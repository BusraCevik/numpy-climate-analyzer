import csv


def save_full_yearly_summary(filepath, years, yearly_means, yearly_std, yearly_change, anomalies):
    """
    Save computed yearly climate analytics into a structured CSV file.
    """
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)

        # Write headers for the CSV file
        writer.writerow([
            "Year", "Yearly_Mean", "Yearly_Std", "Yearly_Change", "Anomalies"
        ])

        # Iterate through the data and write row by row
        for i, year in enumerate(years):
            # Handle index boundary since yearly_change has one less element
            change = yearly_change[i] if i < len(yearly_change) else ""

            writer.writerow([
                year,
                yearly_means[i],
                yearly_std[i],
                change,
                anomalies[i]
            ])