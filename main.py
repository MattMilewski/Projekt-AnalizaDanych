import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Application")

input_ingredients = st.text_input("Choose ingredients:")
input_ingredients = input_ingredients.lower()
input_ingredients = input_ingredients.split(", ")

st.write(input_ingredients)

df = pd.read_csv("indian_food.csv")

if input_ingredients != ['']:
    df = df[
        df.apply(
            lambda row: all(elem in row.ingredients.lower().split(", ") for elem in input_ingredients),
            axis=1
        )
    ]

st.dataframe(df)

fig, ax = plt.subplots()
ax.hist(df.prep_time, bins=20)
st.pyplot(fig)
