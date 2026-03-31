from src.eda import generate_eda_report

file_path = "Data/IPL_matches.csv"

report = generate_eda_report(file_path)

print("\n===== EDA REPORT =====\n")
print(report)

with open("reports/eda_report.txt", "w", encoding="utf-8") as f:
    f.write(report)