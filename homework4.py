import streamlit as st 
import pandas as pd
import seaborn as sns

st.title("Chess Data EDA")
chess = pd.read_csv("~/Downloads/games.csv")

st.header("Distribution")
option = st.selectbox("Which distribution would you like to see?", ("Victory Status", "Winner"))

if option == "Victory Status":
    st.pyplot(sns.displot(chess, x="victory_status", hue="victory_status"))
elif option == "Winner":
    st.pyplot(sns.displot(chess, x="winner", hue="winner"))

st.header("Categorical")
option = st.selectbox("Which category would you like to see?", ("White Rating", "Black Rating"))

if option == "White Rating":
    st.pyplot(sns.catplot(data=chess, x="victory_status", y="white_rating", order=["outoftime", "resign", "mate", "draw"], hue="victory_status"))
elif option == "Black Rating":
    st.pyplot(sns.catplot(data=chess, x="victory_status", y="black_rating", order=["outoftime", "resign", "mate", "draw"], hue="victory_status"))

