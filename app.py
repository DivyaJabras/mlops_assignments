import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CSV Data Visualizer")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV
    data = pd.read_csv(uploaded_file)
    st.write("Data Overview:", data.head())

    # Sidebar for choosing chart type
    chart_type = st.sidebar.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Histogram"])

    st.write("Data Visualization")
    if chart_type == "Line Chart":
        st.line_chart(data)
    elif chart_type == "Bar Chart":
        st.bar_chart(data)
    elif chart_type == "Histogram":
        column = st.selectbox("Select column for histogram", data.columns)
        fig, ax = plt.subplots()
        sns.histplot(data[column], ax=ax)
        st.pyplot(fig)
else:
    st.write("Please upload a CSV file to visualize.")
