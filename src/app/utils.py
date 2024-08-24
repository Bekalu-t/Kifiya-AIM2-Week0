# utils.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore

# Function to load data
def load_data(country):
    if country == 'Togo':
        return pd.read_csv('path_to_togo_dataset.csv')
    elif country == 'Sierra Leone':
        return pd.read_csv('path_to_sierra_leone_dataset.csv')
    elif country == 'Benin':
        return pd.read_csv('path_to_benin_dataset.csv')

# Function to plot correlation heatmap
def plot_correlation_heatmap(df):
    corr = df[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot()

# Function to plot histograms
def plot_histograms(df):
    variables = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']
    for var in variables:
        sns.histplot(df[var], kde=True)
        st.pyplot()

# Function to plot wind polar plot
def plot_wind_polar_plot(df):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.scatter(np.deg2rad(df['WD']), df['WS'], c=df['WSgust'], cmap='viridis', alpha=0.75)
    ax.set_theta_direction(-1)
    ax.set_theta_offset(np.pi / 2)
    st.pyplot(fig)

# Function to plot temperature analysis
def plot_temperature_analysis(df):
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['RH'], y=df['TModA'], hue=df['GHI'], palette='coolwarm', ax=ax)
    ax.set_xlabel('Relative Humidity (%)')
    ax.set_ylabel('Temperature of Module A (°C)')
    st.pyplot(fig)

# Function for Z-Score analysis
def z_score_analysis(df):
    df['Z_GHI'] = zscore(df['GHI'])
    outliers = df[df['Z_GHI'].abs() > 3]
    st.write(f"Outliers in GHI (Z-Score > 3): {len(outliers)} points")
    st.dataframe(outliers[['Timestamp (yyyy-mm-dd hh:mm)', 'GHI', 'Z_GHI']])

# Function to plot bubble chart
def bubble_chart(df):
    fig, ax = plt.subplots()
    bubble = ax.scatter(df['GHI'], df['WS'], s=df['DNI']/10, alpha=0.5, c=df['DHI'], cmap='viridis')
    ax.set_xlabel('GHI (W/m²)')
    ax.set_ylabel('Wind Speed (m/s)')
    fig.colorbar(bubble, ax=ax, label='DHI (W/m²)')
    st.pyplot(fig)
