# main.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, plot_correlation_heatmap, plot_histograms, plot_wind_polar_plot, plot_temperature_analysis, z_score_analysis, bubble_chart

# Title of the dashboard
st.title('Exploratory Data Analysis Dashboard for Togo, Sierra Leone, and Benin')

# Sidebar for dataset selection
st.sidebar.title('Select Dataset')
selected_country = st.sidebar.selectbox('Country', ['Togo', 'Sierra Leone', 'Benin'])

# Load the selected dataset
df = load_data(selected_country)

# Display the data
st.write(f"Showing data for {selected_country}")
st.dataframe(df.head())

# Correlation Analysis
st.write("Correlation Analysis: Solar Radiation and Temperature")
plot_correlation_heatmap(df)

# Wind Analysis: Polar Plot
st.write("Wind Analysis: Polar Plot of Wind Direction and Speed")
plot_wind_polar_plot(df)

# Temperature Analysis: RH vs Temperature and Solar Radiation
st.write("Temperature Analysis: RH vs Temperature and Solar Radiation")
plot_temperature_analysis(df)

# Histograms
st.write("Histograms of Key Variables")
plot_histograms(df)

# Z-Score Analysis
st.write("Z-Score Analysis: Identifying Outliers")
z_score_analysis(df)

# Bubble Chart
st.write("Bubble Chart: Solar Radiation vs Wind Speed")
bubble_chart(df)
