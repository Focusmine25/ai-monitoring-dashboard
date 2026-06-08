# AI Monitoring Dashboard

## Overview

AI Monitoring Dashboard is an AIOps and Machine Learning project that monitors infrastructure metrics, detects anomalies using Isolation Forest, and presents results through an interactive Streamlit dashboard.

The dashboard provides real-time visibility into system health, anomaly counts, infrastructure metrics, and downloadable reports.

## Dashboard Screenshots

### AI Monitoring Dashboard Overview

![Dashboard 1](screenshots/dashboard1.png)

---

### Infrastructure Metrics & Charts

![Dashboard 2](screenshots/dashboard2.png)

---

### Anomaly Detection View

![Dashboard 3](screenshots/dashboard3.png)

## Features

- Infrastructure monitoring
- AI anomaly detection
- Interactive dashboard
- CPU monitoring
- Memory monitoring
- Disk monitoring
- System health assessment
- Downloadable anomaly reports

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-Learn
- Isolation Forest
- Joblib
- Jupyter Notebook

## Project Structure

ai-monitoring-dashboard

├── app
│   └── dashboard.py
│
├── data
│   └── monitoring_data.csv
│
├── models
│   └── anomaly_model.pkl
│
├── notebooks
│   └── training.ipynb
│
├── reports
│
└── charts

## Machine Learning

The project uses Isolation Forest for anomaly detection across infrastructure metrics.

Metrics analyzed:

- CPU Usage
- Memory Usage
- Disk Usage

## Dashboard Features

- Total record count
- Anomaly count
- Anomaly rate
- System health status
- Infrastructure charts
- Downloadable anomaly report

## Future Improvements

- Real monitoring data
- Prometheus integration
- Grafana integration
- AWS CloudWatch integration
- Azure Monitor integration
- Kubernetes metrics
- Real-time streaming data

## Author

Built as part of a Machine Learning, AIOps, DevOps, and Cloud Engineering portfolio.