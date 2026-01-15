SELECT * FROM v_year_kpis LIMIT 20;

SELECT * FROM v_year_kpis_yoy LIMIT 20;

SELECT *
FROM v_psi_year_summary
WHERE year = (SELECT MAX(year) FROM fact_patient_safety)
ORDER BY total_events DESC
LIMIT 10;

SELECT *
FROM v_county_latest_year
ORDER BY events_per_100k DESC
LIMIT 10;