# Rain Projection 🌧️
### Satellite-Based Rainfall Trend Analysis for Vidarbha, Maharashtra

**Challenge:** NASA Space Apps Challenge 2026 — Challenge 02: *Be an Earth System Trend Detective!*  
**Study Region:** Vidarbha, Maharashtra, India  
**Primary Data Source:** NASA Global Precipitation Measurement (GPM) — IMERG

## Project Overview

Rain Projection is a satellite-based rainfall monitoring and historical trend-analysis application developed to study precipitation patterns in Vidarbha, Maharashtra.

The project is designed around NASA's Global Precipitation Measurement (GPM) Integrated Multi-satellitE Retrievals for GPM (IMERG) dataset. Using monthly precipitation data accessed through NASA Giovanni, the application provides a framework for examining rainfall variability, monsoon patterns, and long-term precipitation trends.

The goal is to make satellite-derived rainfall information easier to explore and understand, particularly in a region where agriculture and water resources depend heavily on monsoon rainfall.

## Key Features

- **Monthly Rainfall Analysis:** Visualizes average precipitation patterns across the twelve months.
- **Monsoon Rainfall Monitoring:** Calculates and displays June–September rainfall totals for individual years.
- **Year-to-Year Comparison:** Helps explore variations in monsoon rainfall across different years.
- **Trend Analysis:** Uses Kendall's rank correlation test to examine possible monotonic rainfall trends.
- **Linear Regression:** Calculates the rainfall trend slope in mm/year.
- **Data Upload:** Supports uploading NASA Giovanni precipitation time-series CSV exports.
- **Data Export:** Allows users to download cleaned rainfall datasets for further analysis.

## NASA Data Source and Methodology

The project is designed to use NASA GPM IMERG monthly precipitation data.

**Data source:**  
NASA Giovanni — https://giovanni.gsfc.nasa.gov/

**Dataset:** GPM IMERG Monthly precipitation product (GPM_3IMERGM). The applicable product version and variable metadata should be verified when downloading data.

### Data Processing Workflow

1. Access monthly precipitation data through NASA Giovanni.
2. Select the geographical study region covering Vidarbha, Maharashtra.
3. Generate an area-averaged monthly precipitation time series.
4. Download the precipitation data in CSV format.
5. Upload the dataset into the Rain Projection application.
6. Select the date and precipitation columns.
7. Check precipitation units, missing values, and temporal coverage.
8. Calculate monthly and monsoon-season rainfall statistics.
9. Analyze historical rainfall trends using statistical methods.

**Precipitation units:** The application expects rainfall depth in mm/month. If the NASA export contains precipitation rate in mm/hr, it must first be converted using the correct temporal averaging period and calendar month length. Metadata must be checked before conversion.

## Monsoon Analysis

Vidarbha's primary monsoon analysis period is defined as June, July, August, and September (JJAS).

Annual monsoon rainfall is calculated as:

Monsoon Rainfall = June + July + August + September

The application uses this calculation to compare monsoon rainfall across years and investigate changes in seasonal precipitation.

## Statistical Trend Analysis

Two statistical approaches are included:

**1. Kendall Rank Correlation Test**

Used to examine whether rainfall exhibits a monotonic increasing or decreasing pattern over time.

**2. Linear Regression**

Estimates the direction and magnitude of the rainfall trend, expressed in mm/year.

A p-value below 0.05 is treated as statistically significant for this exploratory analysis. Statistical significance does not establish climate-change causation.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Plotly
- SciPy
- NASA GPM IMERG
- NASA Giovanni

## Project Structure

```text
Rain_Projection_Project/
│
├── app.py
├── data/
│   └── sample_rainfall_demo.csv
├── assets/
├── requirements.txt
├── PROJECT_DOCUMENTATION.pdf
└── README.md
```

## Project Objective and Impact

Rain Projection aims to make satellite-based rainfall information more accessible and understandable.

By examining historical rainfall patterns in Vidarbha, the project provides an exploratory tool that can help users understand monsoon variability, identify unusually wet or dry periods, and investigate long-term rainfall trends.

The analysis may support discussions around agricultural planning, water-resource management, and regional climate variability.

## Limitations and Future Improvements

- Integrate and validate an actual NASA GPM IMERG data export for the study period.
- Apply a precise Vidarbha geographical boundary for spatial averaging.
- Improve missing-data and monsoon completeness checks.
- Introduce Sen's slope and a formal Mann–Kendall trend analysis.
- Compare satellite-derived rainfall with IMD ground-station observations.
- Expand the analysis to individual districts within Vidarbha.
- Develop automated NASA data retrieval and updates.

## Important Data Transparency Note

The application includes an illustrative sample CSV to demonstrate its interface and analysis workflow. This sample is synthetic and must not be interpreted as observed NASA rainfall data.

NASA GPM IMERG is the intended primary observational data source. Scientific conclusions and reported rainfall trends should be based on an actual downloaded and validated NASA dataset, not the illustrative sample.

## Project Summary

Rain Projection is a Python and Streamlit-based satellite rainfall analysis application focused on Vidarbha, Maharashtra. Designed around NASA GPM IMERG precipitation data accessed through NASA Giovanni, it explores monthly rainfall patterns, June–September monsoon totals, year-to-year variations, and historical precipitation trends using statistical analysis. The project aims to improve understanding of regional rainfall variability and its relevance to agriculture and water-resource planning.
