# California Patient Safety Overview (2005–2015)

End-to-end analytics project analyzing California patient safety event trends using a public PSI dataset. The project covers ingestion into MySQL, standardized SQL metrics, data quality validation, and an executive Power BI dashboard.

## Objective
Provide an executive-friendly view of patient safety performance over time, including:
- Trend in events per 100k population
- Latest-year KPIs
- Year-over-year (YoY) change

## Business Context
This project simulates a healthcare operations analytics use case focused on patient safety events. The goal is to:
- Track trends in adverse event rates over time
- Surface executive-level KPIs for operational monitoring
- Enable data-driven quality improvement initiatives

The dashboard is designed for healthcare administrators, quality leaders, and operations teams.

## Data
Public California OSHPD Patient Safety Indicators dataset (2005–2015), aggregated by county and year. No PHI.

## Data Flow
1. Raw data is ingested from CSV source files
2. Python is used to normalize and standardize fields
3. SQL models define core metrics and data quality checks
4. Power BI consumes curated tables for visualization


## Tools
- **MySQL** (storage + reusable SQL views)
- **Python (pandas)** (CSV ingestion and type handling)
- **SQL** (metrics + data quality checks)
- **Power BI + DAX** (dashboard + “latest year” KPIs)
- **ODBC DSN** (Power BI ↔ MySQL connection)

## What I Built
- CSV → MySQL ingestion pipeline
- Metrics layer implemented as SQL views (standardized definitions)
- Data quality checks (nulls, duplicates, PSI description consistency)
- Executive dashboard:
  - Events per 100k trend line (2005–2015)
  - Latest-year cards: total events, events per 100k, YoY change %

## Repository Structure
- `data/` – raw dataset
- `python/` – ingestion scripts
- `sql/` – metrics + data quality checks
- `dashboards/` – Power BI report file (`.pbix`)

## Dashboard
Open the `.pbix` file in `dashboards/` using Power BI Desktop.
![Executive Overview](dashboards/executive_overview.png)

## Key Insights
- Patient safety events per 100k population declined ~50% from 2005 to 2015.
- The most recent year showed a ~9% improvement compared to the prior year.
- This suggests sustained quality improvements rather than short-term variance.

## Future Improvements
- Add drill-downs by hospital or region
- Include control charts to distinguish signal vs noise
- Automate data refresh using scheduled pipelines


## Author
Austin Knighton

