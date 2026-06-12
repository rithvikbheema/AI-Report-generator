import pandas as pd

def generate_report(df):

    total_rows = len(df)

    report = f"""
Business Intelligence Report

Total Records: {total_rows}

Columns:
{', '.join(df.columns)}

Summary Statistics:

{df.describe(include='all')}
"""

    return report