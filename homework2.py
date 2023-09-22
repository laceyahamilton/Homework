import streamlit as st 
import seaborn as sns
import pandas as pd
import plotly.express as px

iris = sns.load_dataset('iris')
st.write("""
# Iris Dataset 
""")
mychart = px.scatter_3d(iris, x ="petal_length", y="petal_width", z="sepal_width", color="species", color_continuous_scale="greens")
mychart2 = px.scatter_3d(iris, x="sepal_length", y="sepal_width", z="petal_width", color="species", color_continuous_scale="greens")

tab1, tab2 = st.tabs(["Petal Length vs Petal Width vs Sepal Width", "Sepal Length vs Sepal Width vs Petal Width"])

with tab1:
    st.plotly_chart(mychart, sharing="streamlit", theme=None)

with tab2:
    st.plotly_chart(mychart2, sharing="streamlit", theme=None)