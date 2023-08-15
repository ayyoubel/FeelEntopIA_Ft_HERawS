import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns

df= pd.read_excel("hhh.xlsx")

st.title('Scatter Plot App')

# Dropdowns to select x and y columns
x_column = st.selectbox('Select X Column', df.columns)
y_column = st.selectbox('Select Y Column', df.columns)


plot_button = st.button('PLOT')

# Handle plot button click
if plot_button:
    # Create a scatter plot using Seaborn
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    st.pyplot(plt)
