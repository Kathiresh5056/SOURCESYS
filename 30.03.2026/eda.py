import json
from src.utils import load_data, get_sample, get_basic_info

def generate_eda_report(file_path):
    df = load_data(file_path)

    sample_data = get_sample(df)
    basic_info = get_basic_info(df)

    # Generate EDA report
    report = f"""
===== EXPLORATORY DATA ANALYSIS REPORT =====

1. DATASET SHAPE & STRUCTURE
   - Number of rows: {basic_info['shape'][0]}
   - Number of columns: {basic_info['shape'][1]}
   - Total cells: {basic_info['shape'][0] * basic_info['shape'][1]}

2. COLUMN INFORMATION
   - Columns: {', '.join(basic_info['columns'])}
   
3. DATA TYPES
{chr(10).join(f"   - {col}: {dtype}" for col, dtype in basic_info['dtypes'].items())}

4. MISSING VALUES
{chr(10).join(f"   - {col}: {count} ({100*count/basic_info['shape'][0]:.1f}%)" for col, count in basic_info['missing_values'].items())}

5. DATA SAMPLE (First 5 Rows)
"""
    
    for idx, row in enumerate(sample_data, 1):
        report += f"\n   Row {idx}:\n"
        for col, val in row.items():
            report += f"      - {col}: {val}\n"

    return report