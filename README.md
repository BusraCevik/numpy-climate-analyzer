# Climate Change Analyzer with NumPy

## Description
This project analyzes global land temperature data using only NumPy.  
It performs statistical analysis, trend estimation, anomaly detection,  
and time-based aggregation to explore climate change patterns.

---

## Features
- Data cleaning and preprocessing with NumPy  
- Statistical climate profiling (mean, std, variance, yearly averages)  
- Global warming trend analysis using linear regression  
- Climate anomaly detection using sigma thresholds  
- Yearly temperature aggregation  
- Extreme years identification (hottest and coldest years)  
- CSV export of yearly summaries  
- Visualization of yearly trends and anomalies (saved as PNGs)  

---

## Technologies
- Python 3.x  
- NumPy  
- Matplotlib (for visualization)  

---


## Project Structure

```text
climate_analyzer/
│
├── data/                     # Dataset
│   └── climate.csv
│
├── data/outputs/             # Generated files
│   ├── yearly_summary.csv
│   ├── yearly_trend.png
│   └── yearly_anomalies.png
│
├── src/                      # Modular code
│   ├── aggregations.py       # Yearly aggregation functions
│   ├── anomalies.py          # Anomaly detection functions
│   ├── loader.py             # Data loading & cleaning
│   ├── statistics.py         # Basic statistics functions
│   ├── trends.py             # Trend analysis functions
│   └── plotting.py           # Visualization functions
│
├── main_unmodularized.py     # Original version before modularization
├── main.py                   # Modularized version
└── README.md


---

## Development History
1. **Initial Version** (`main_unmodularized.py`)  
   - All code was written in a single file  
   - Basic statistics, yearly aggregation, anomalies, trend analysis, and extreme years detection  
   - Terminal output only

2. **Modular Version** (`main.py`)  
   - Code refactored into reusable functions in `src/`  
   - CSV export of yearly summaries  
   - Visualizations of yearly trends and anomalies saved to `data/`  
   - Easier maintenance and scalability

---

## Use Case
This project demonstrates how large-scale numerical datasets  
can be processed efficiently using only NumPy without external libraries.  
It also shows a workflow from **raw data analysis** to **modular, reusable code**  
with persistent outputs (CSV, PNGs) for further analysis or reporting.
