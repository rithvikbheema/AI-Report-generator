import streamlit as st
import pandas as pd
from report_generator import generate_report

st.title("AI Report Generator")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    if st.button("Generate Report"):
        report = generate_report(df)

        st.subheader("Generated Report")
        st.write(report)