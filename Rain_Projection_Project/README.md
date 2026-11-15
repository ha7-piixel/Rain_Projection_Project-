# Rain Projection

**Project:** Rain Projection  
**Study region:** Vidarbha, Maharashtra, India  
**Challenge:** NASA Space Apps Challenge 2026 — Challenge 02, *Be an Earth System Trend Detective!*

## What this demo does
- Loads a bundled illustrative monthly rainfall CSV or a user-uploaded CSV.
- Displays average precipitation by month.
- Calculates June–September monsoon totals by year.
- Displays a yearly monsoon chart and a linear trend line.
- Reports a Kendall rank trend test and a linear regression slope.
- Lets users download cleaned data.

## Important data note
`data/sample_rainfall_demo.csv` is **synthetic illustrative data** created only to demonstrate the software. It is not NASA data and must not be cited as an observed rainfall record. Upload an actual NASA Giovanni GPM IMERG monthly time-series export before reporting scientific findings.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the demo:
   ```bash
   streamlit run app.py
   ```
6. Open the local URL printed by Streamlit (usually `http://localhost:8501`).

## NASA data workflow
1. Open https://giovanni.gsfc.nasa.gov/
2. Find the GPM IMERG monthly precipitation product. The product identifier commonly shown is `GPM_3IMERGM`; verify the current version and product description in Giovanni.
3. Choose a spatial selection representing Vidarbha and a supported historical period.
4. Request a monthly time-series / area-average output and download its CSV.
5. Upload the CSV in the app and map the date and precipitation columns.
6. Verify units (the app expects precipitation depth in mm per month), missing values, selected region, and data coverage.

The exact export format may vary, so the app includes column selectors rather than assuming fixed column names.

## Analysis notes
- Monsoon season is defined here as June, July, August, and September.
- The yearly monsoon value is the sum of those monthly values for each year.
- The trend test uses Kendall's rank correlation (`scipy.stats.kendalltau`) as a simple monotonic-trend significance check.
- The app also reports a linear regression slope in mm/year.
- A p-value below 0.05 is conventionally treated as statistically significant for this exploratory analysis. It does not prove climate-change causation.
- If years have missing monsoon months, totals may be incomplete. Inspect data completeness before interpreting.

## Suggested project summary (edit after using real NASA data)
Rain Projection is a lightweight rainfall-trend analysis demo focused on Vidarbha, Maharashtra, a monsoon-dependent region. It uses monthly precipitation time-series data from NASA's GPM IMERG product, accessed through NASA Giovanni, to explore seasonal rainfall patterns and changes over time. The application visualizes monthly rainfall averages and June–September monsoon totals, and applies a Kendall rank trend test and linear regression to summarize possible trends. The goal is to make historical rainfall variability easier to explore for learning and discussion related to agriculture and water planning. The current bundled dataset is synthetic and is used only to demonstrate the interface; scientific findings will be generated only after a real NASA data export is uploaded. This is a historical trend-analysis tool, not a future rainfall forecasting system.

## Suggested demo narration (about 60–90 seconds)
"Rain Projection is a simple tool for exploring historical monsoon rainfall in Vidarbha, Maharashtra. We use NASA GPM IMERG monthly precipitation data, accessed through Giovanni. The user can upload the downloaded CSV, and the application converts it into a clean monthly time series. It then shows the average rainfall pattern across the year and the June-to-September monsoon total for each year. Finally, it applies a Kendall trend test and calculates a linear trend slope, so users can inspect whether the historical series shows a monotonic trend. The included sample is synthetic and only demonstrates the workflow; the real analysis uses the NASA export. The project supports understanding historical rainfall variability, but it does not forecast future rainfall."

## Project structure
- `app.py` — Streamlit application
- `data/sample_rainfall_demo.csv` — synthetic demonstration data
- `requirements.txt` — Python dependencies
- `PROJECT_DOCUMENTATION.pdf` — complete project report
- `assets/` — diagrams and charts used in the report

## Limitations and next improvements
- Use a clearly documented region boundary / polygon or explain the chosen bounding box.
- Confirm the exact units and temporal interpretation of the selected NASA product.
- Add completeness checks for all four monsoon months per year.
- Compare with station observations or another trusted dataset for validation.
- Consider Sen's slope and a formal Mann–Kendall implementation for a more rigorous analysis.
- Add district-level analysis only if suitable spatial data and time are available.
