"""
RAIN PROJECTION — NASA Space Apps Challenge demo
Historical monsoon rainfall trend explorer for Vidarbha, Maharashtra, India.

IMPORTANT:
- The bundled CSV is illustrative synthetic data for demonstrating the app.
- Replace it with a NASA GPM IMERG monthly time-series export before making
  scientific claims about observed rainfall.
- This is a historical trend-analysis tool, not an operational weather forecast.
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kendalltau, linregress

st.set_page_config(page_title="Rain Projection", page_icon="🌧️", layout="wide")

BLUE = "#DCEFFC"
DARK = "#174A6E"
st.markdown("""
<style>
.stApp {background: #F5FAFE;}
h1, h2, h3 {color: #174A6E;}
div[data-testid="stMetric"] {background: #E8F4FC; padding: 12px; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

st.title("🌧️ Rain Projection")
st.subheader("Exploring historical monsoon rainfall patterns in Vidarbha, India")
st.caption("NASA Space Apps Challenge 2026 • Challenge 02: Be an Earth System Trend Detective!")

st.info(
    "Demo mode: the bundled dataset is synthetic and is used only to demonstrate the workflow. "
    "Upload a real NASA Giovanni GPM IMERG monthly CSV to analyse observed precipitation."
)

@st.cache_data
def load_sample():
    return pd.read_csv("data/sample_rainfall_demo.csv", parse_dates=["date"])

def normalize_data(df):
    # Find likely date and precipitation columns, or ask the user to map them.
    cols = list(df.columns)
    date_candidates = [c for c in cols if any(k in c.lower() for k in ["date", "time", "month"])]
    rain_candidates = [c for c in cols if any(k in c.lower() for k in ["precip", "rain", "value", "gpm"])]
    c1 = date_candidates[0] if date_candidates else cols[0]
    c2 = rain_candidates[0] if rain_candidates else (cols[1] if len(cols) > 1 else cols[0])
    return c1, c2

with st.sidebar:
    st.header("Data source")
    upload = st.file_uploader("Upload monthly rainfall CSV", type=["csv"])
    st.markdown("---")
    st.markdown("**Study area**")
    st.write("Vidarbha region, Maharashtra, India")
    st.markdown("**Suggested NASA dataset**")
    st.code("GPM_3IMERGM")
    st.markdown("[Open NASA Giovanni](https://giovanni.gsfc.nasa.gov/)")
    st.markdown("[NASA GES DISC](https://disc.gsfc.nasa.gov/)")

if upload is not None:
    raw = pd.read_csv(upload)
    st.success("Uploaded CSV loaded. Select the correct columns below.")
    dcol, rcol = normalize_data(raw)
    c1, c2 = st.columns(2)
    with c1:
        date_col = st.selectbox("Date / time column", raw.columns, index=list(raw.columns).index(dcol))
    with c2:
        rain_col = st.selectbox("Precipitation column (mm/month)", raw.columns, index=list(raw.columns).index(rcol))
    df = pd.DataFrame({
        "date": pd.to_datetime(raw[date_col], errors="coerce"),
        "rain_mm": pd.to_numeric(raw[rain_col], errors="coerce")
    }).dropna()
    source_label = "Uploaded dataset"
else:
    df = load_sample()
    source_label = "Illustrative synthetic demo data"

if df.empty:
    st.error("No usable rows found. Check that the selected columns contain dates and numeric precipitation values.")
    st.stop()

df = df.sort_values("date")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["is_monsoon"] = df["month"].isin([6, 7, 8, 9])
df["season"] = np.where(df["is_monsoon"], "Monsoon (Jun–Sep)", "Other months")

st.caption(f"Data source: **{source_label}** | Records: **{len(df)}** | "
           f"Period: **{df.date.min():%b %Y} – {df.date.max():%b %Y}**")

# Monthly climatology
monthly_avg = df.groupby("month")["rain_mm"].mean().reindex(range(1,13))
month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

# Monsoon total by year; only sum available Jun-Sep records
monsoon = df[df["is_monsoon"]].groupby("year")["rain_mm"].sum().rename("monsoon_total_mm")
if len(monsoon) >= 3:
    x = monsoon.index.to_numpy(dtype=float)
    y = monsoon.values.astype(float)
    slope, intercept, r_value, p_reg, stderr = linregress(x, y)
    tau, p_kendall = kendalltau(x, y)
else:
    slope = intercept = r_value = p_reg = stderr = tau = p_kendall = np.nan

a, b, c = st.columns(3)
a.metric("Monthly records", f"{len(df):,}")
b.metric("Average monthly precipitation", f"{df.rain_mm.mean():.1f} mm")
c.metric("Monsoon years available", f"{len(monsoon)}")

st.header("1. Monthly rainfall pattern")
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.bar(month_names, monthly_avg.values, color="#79BDE8")
ax.set_ylabel("Mean precipitation (mm/month)")
ax.set_xlabel("Month")
ax.set_title("Average precipitation by calendar month")
ax.grid(axis="y", alpha=.25)
st.pyplot(fig, use_container_width=True)
plt.close(fig)

st.header("2. Monsoon rainfall across years")
if len(monsoon):
    fig, ax = plt.subplots(figsize=(10, 3.8))
    ax.plot(monsoon.index, monsoon.values, marker="o", linewidth=2, color="#2476A8", label="Monsoon total")
    if len(monsoon) >= 3:
        ax.plot(x, intercept + slope*x, linestyle="--", color="#E28B42", label="Linear trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("June–September precipitation (mm)")
    ax.set_title("Annual monsoon precipitation")
    ax.grid(alpha=.25)
    ax.legend()
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)
else:
    st.warning("No June–September records were found in the selected dataset.")

st.header("3. Trend test")
if len(monsoon) >= 3:
    left, right = st.columns(2)
    left.metric("Estimated linear slope", f"{slope:.2f} mm/year")
    right.metric("Kendall trend p-value", f"{p_kendall:.4f}")
    if p_kendall < 0.05:
        st.write("The Mann–Kendall-style Kendall rank test indicates a statistically significant monotonic association at the 5% level.")
    else:
        st.write("The trend test does not show statistically significant monotonic evidence at the 5% level.")
    st.caption(f"Kendall tau = {tau:.3f}. Linear regression R² = {r_value**2:.3f}. "
               "Statistical association does not establish climate-change causation.")
else:
    st.warning("At least three years with monsoon records are needed for this demo trend summary.")

st.header("4. Explore the data")
st.dataframe(df[["date","rain_mm","year","month"]], use_container_width=True, hide_index=True)
st.download_button("Download cleaned data as CSV", df[["date","rain_mm"]].to_csv(index=False),
                   file_name="rain_projection_cleaned_data.csv", mime="text/csv")

with st.expander("How to prepare NASA Giovanni data"):
    st.markdown("""
    1. Open [NASA Giovanni](https://giovanni.gsfc.nasa.gov/).
    2. Select **GPM_3IMERGM – GPM IMERG Monthly Precipitation** (confirm the current product/version shown in Giovanni).
    3. Choose the Vidarbha study-area bounding box or a suitable region/area average.
    4. Select a monthly time-series output and a time range supported by the product.
    5. Generate the plot and download the time-series data as CSV.
    6. Upload that CSV in the sidebar. Select the date/time and precipitation-value columns.
    7. Check the units, spatial averaging method, missing values, and date coverage before interpreting results.

    The exact export column names can vary. This app therefore asks you to map the columns.
    """)

st.markdown("---")
st.caption("Rain Projection is an educational historical-data explorer. It does not predict future rainfall or provide warnings.")
