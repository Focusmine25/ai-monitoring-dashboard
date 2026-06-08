import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "data" / "monitoring_data.csv"
model_path = BASE_DIR / "models" / "anomaly_model.pkl"

st.set_page_config(
    page_title="AI Monitoring Dashboard",
    layout="wide"
)

st.title("AI Monitoring Dashboard")

data = pd.read_csv(data_path)

model = joblib.load(model_path)

predictions = model.predict(data)

data["prediction"] = predictions

anomalies = data[data["prediction"] == -1]

total_records = len(data)
anomaly_count = len(anomalies)

anomaly_rate = round(
    (anomaly_count / total_records) * 100,
    2
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Records",
        total_records
    )

with col2:
    st.metric(
        "Anomalies",
        anomaly_count
    )

with col3:
    st.metric(
        "Anomaly Rate",
        f"{anomaly_rate}%"
    )

st.divider()

if anomaly_rate < 5:
    st.success(
        "System Status: HEALTHY"
    )

elif anomaly_rate < 10:
    st.warning(
        "System Status: WARNING"
    )

else:
    st.error(
        "System Status: CRITICAL"
    )

st.subheader("Infrastructure Metrics")

cpu_col, memory_col = st.columns(2)

with cpu_col:
    st.line_chart(data["cpu"])

with memory_col:
    st.line_chart(data["memory"])

st.subheader("Disk Usage")

st.line_chart(data["disk"])

st.subheader("Recent Anomalies")

st.dataframe(
    anomalies.head(10)
)

csv = anomalies.to_csv(
    index=False
)

st.download_button(
    label="Download Anomaly Report",
    data=csv,
    file_name="anomaly_report.csv",
    mime="text/csv"
)