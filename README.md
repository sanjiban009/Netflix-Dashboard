# NETFLIX

Independent BI demonstration by Sanjiban Das. All data is synthetic, not actual Netflix data.

1. Extract the ZIP and open index.html in Chrome, Edge, Firefox or Safari. No install, server or internet is required.
2. Use the left sidebar to switch between Executive Overview, Audience Engagement, Content Performance and Content Efficiency.
3. Use financial year, FYTD/full FY, end month, region, plan and genre slicers. All views, decision signals and recommended next actions use the current selection.


## Data and metric notes
3,100 synthetic monthly rows, April 2024–October 2026. Grain: month × region × subscription plan × genre. Completion rate = sum(completions) / sum(starts). Spend per watch hour = sum(allocated INR content spend) / sum(watch hours). Starts are events, not unique viewers. Allocated spend is illustrative and cannot establish profitability or causal effectiveness. L = lakh, Cr = crore.

Indian FY runs April through March. FYTD includes whole months through the selected month, capped at the latest month present. Prior-year comparisons use the same fiscal months and other filters. A full-FY selection for an incomplete year is explicitly flagged. Rate changes are in percentage points.

data.csv is the Excel-readable dataset; data.js embeds the same CSV for offline use. Run python3 generate.py in this folder to regenerate both files deterministically.
<img width="1688" height="1430" alt="04-dashboard" src="https://github.com/user-attachments/assets/868fad12-a0bb-4831-9253-1f24f5aecc03" />
<img width="1688" height="1430" alt="03-dashboard" src="https://github.com/user-attachments/assets/e64c6538-17d5-4c79-bb7e-dc10a9bce6db" />
<img width="1688" height="1430" alt="02-dashboard" src="https://github.com/user-attachments/assets/00b38f83-08f5-4548-a66c-7f4c7e413c1a" />
<img width="1688" height="1430" alt="01-dashboard" src="https://github.com/user-attachments/assets/d754b589-918c-4f08-9c68-b4573413b3f8" />
