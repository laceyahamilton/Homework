streamlit 
seaborn
pandas
plotly.express

iris = seaborn.load_dataset('iris')
streamlit.write("""
# Iris Dataset 
""")
mychart = plotly.express.scatter_3d(iris, x ="petal_length", y="petal_width", z="sepal_width", color="species", color_continuous_scale="greens")
mychart2 = plotly.express.scatter_3d(iris, x="sepal_length", y="sepal_width", z="petal_width", color="species", color_continuous_scale="greens")

tab1, tab2 = streamlit.tabs(["Petal Length vs Petal Width vs Sepal Width", "Sepal Length vs Sepal Width vs Petal Width"])

with tab1:
    streamlit.plotly_chart(mychart, sharing="streamlit", theme=None)

with tab2:
    streamlit.plotly_chart(mychart2, sharing="streamlit", theme=None)
