# 🌧️ Rain Projection
### Satellite-Based Rainfall Monitoring and Trend Analysis for Vidarbha, Maharashtra

**Project:** Rain Projection  
**Study Region:** Vidarbha, Maharashtra, India  
**Challenge:** NASA Space Apps Challenge 2026 — Challenge 02: *Be an Earth System Trend Detective!*  
**Primary Data Source:** NASA Global Precipitation Measurement (GPM) — IMERG

## 📌 Project Overview

Rain Projection is a Python-based rainfall monitoring and historical trend-analysis web application designed to explore precipitation patterns in Vidarbha, Maharashtra.

The project is designed around NASA's Global Precipitation Measurement (GPM) Integrated Multi-satellitE Retrievals for GPM (IMERG) monthly precipitation dataset, accessed through NASA Giovanni.

The application helps users visualize monthly rainfall, analyze monsoon precipitation, compare rainfall across years, identify unusually wet and dry periods, and investigate long-term rainfall trends using statistical methods.

## ✨ Key Features

- **Monthly Rainfall Analysis:** Visualizes average precipitation patterns across all twelve months.
- **Monsoon Analysis:** Calculates June–September (JJAS) rainfall totals for individual years.
- **Yearly Comparison:** Explores variations in monsoon rainfall across different years.
- **Rainfall Trend Analysis:** Uses Kendall's rank correlation test to examine monotonic trends.
- **Linear Regression:** Estimates rainfall trends in mm/year.
- **NASA Data Integration:** Supports uploading monthly precipitation CSV exports from NASA Giovanni.
- **Data Export:** Allows users to download cleaned rainfall datasets.

## 🛰️ NASA Data Source

The project uses NASA GPM IMERG monthly precipitation data as its intended primary observational data source.

**NASA Giovanni:** https://giovanni.gsfc.nasa.gov/

**Dataset:** GPM IMERG Monthly precipitation product (GPM_3IMERGM).

The product version, variable, units, and temporal interpretation should be verified in the NASA data portal before analysis.

### NASA Data Processing Workflow

1. Open NASA Giovanni.
2. Select the GPM IMERG monthly precipitation product.
3. Define the geographical study region covering Vidarbha, Maharashtra.
4. Select the required historical time period.
5. Generate an area-averaged monthly precipitation time series.
6. Download the data as a CSV file.
7. Upload the CSV into Rain Projection.
8. Select the date and precipitation columns.
9. Verify units, missing values, and data coverage.
10. Explore rainfall patterns and perform statistical analysis.

**Important:** The application expects precipitation depth in mm/month. If the NASA export provides a precipitation rate in mm/hr, convert it using the correct averaging period and calendar month length. Do not convert a dataset that is already expressed in mm/month.

## 📊 Analysis Methodology

### 1. Monthly Rainfall Analysis

Examines monthly precipitation patterns to understand seasonal rainfall variability throughout the year.

### 2. Monsoon Rainfall Analysis

The monsoon period is defined as June, July, August, and September (JJAS).

Annual monsoon rainfall:

Monsoon Rainfall = June + July + August + September

### 3. Wet and Dry Period Analysis

Compares rainfall values against a selected historical reference period to identify unusually wet and dry conditions.

### 4. Statistical Trend Analysis

- Kendall rank correlation test: Examines monotonic rainfall trends.
- Linear regression: Estimates the direction and magnitude of rainfall trends in mm/year.
- Statistical significance: A p-value below 0.05 is treated as significant for exploratory analysis.

Statistical significance does not establish climate-change causation.

## 🛠️ Technologies Used

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Plotly
- SciPy
- NASA GPM IMERG
- NASA Giovanni

## 📁 Project Structure

```text
Rain_Projection_Project/
│
├── app.py
├── data/
│   └── sample_rainfall_demo.csv
├── assets/
├── requirements.txt
├── PROJECT_DOCUMENTATION.pdf
├── README.md
└── .gitignore
```

## 💻 Installation and Setup

### Prerequisites

- Python 3.10 or newer
- Git
- Internet connection

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/ha7-piixel/Rain_Projection_Project-.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Rain_Projection_Project-
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows Git Bash:

```bash
source .venv/Scripts/activate
```

For Linux or WSL:

```bash
source .venv/bin/activate
```

### Step 4: Install Required Libraries

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install dependencies:

```bash
pip install streamlit pandas numpy matplotlib plotly scipy
```

Alternatively, install everything listed in the requirements file:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

### Step 6: Open the Application

Open the local URL displayed in your terminal, usually:

http://localhost:8501

## 📈 Expected Output

The application provides:

- Monthly rainfall visualizations.
- Annual monsoon rainfall comparisons.
- Historical rainfall trend charts.
- Statistical trend-test results.
- Downloadable cleaned rainfall data.

## 🎯 Project Objective and Impact

Rain Projection aims to make satellite-derived rainfall information more accessible and understandable.

By exploring historical rainfall variability in Vidarbha, the project can support discussions around agricultural planning, water-resource management, and regional climate patterns.

## ⚠️ Data Transparency and Limitations

The bundled `data/sample_rainfall_demo.csv` is synthetic illustrative data used to demonstrate the application's interface and functionality. It is not an observed NASA rainfall dataset.

The application supports importing NASA Giovanni GPM IMERG precipitation exports. Scientific results and conclusions must be generated using actual downloaded and validated NASA data.

Further improvements include:

- Applying a precise Vidarbha geographical boundary for spatial averaging.
- Adding complete monsoon-month validation.
- Implementing Sen's slope and a formal Mann–Kendall trend test.
- Comparing satellite rainfall with IMD ground-station observations.
- Expanding analysis to individual Vidarbha districts.
- Automating NASA data retrieval.

## 👨‍💻 Project Summary

Rain Projection is a satellite-based rainfall monitoring and trend-analysis application focused on Vidarbha, Maharashtra. Designed around NASA GPM IMERG monthly precipitation data, the application explores monthly rainfall patterns, monsoon variability, year-to-year comparisons, and historical precipitation trends using statistical analysis. It aims to make rainfall information easier to understand and support discussions about regional climate variability, agriculture, and water-resource planning.
