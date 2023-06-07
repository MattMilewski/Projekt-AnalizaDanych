import streamlit as st # import streamlit do wizualizacji rozwiazania
import pandas as pd # import pandas do dzialania na danych tabelarycznych
import matplotlib.pyplot as plt # import pyplot z biblioteki matplotlib do wykresu histogramu

st.write("Application") # wyswietl tytul programu

input_ingredients = st.text_input("Choose ingredients:") # wyswietl label nad inputem ze skladnikami i pobierz skladniki w postaci tekstu
input_ingredients = input_ingredients.lower() # zamien wszystkie znaki na male
input_ingredients = input_ingredients.split(", ") # podziel string na tablice skladnikow dzielac po przecinku

st.write(input_ingredients) # wyswietl tablice wpisanych skladnikow

df = pd.read_csv("indian_food.csv") # wczytaj dane z przepisami

if input_ingredients != ['']: # jesli uzytkownik cos wpisal, dokonaj filtrowania, jesli nie to wyswietl wszystko
    df = df[
        df.ingredients.apply(
            lambda ingredients_string: all(
                el.lower() in input_ingredients for el in ingredients_string.split(", ")
            )
        )
    ]
    # wybierz podzbior danych na podstawie warunku kolumny ingredients:
    # dla danego wiersza (ingredients_string) sprawdz czy kazdy skladnik (z malych liter) zawiera sie w liscie input_ingredients)
    
    df.reset_index(inplace=True) # zresetuj index aby ponumerowac pofiltrowane przepisy w kolejnosci

st.dataframe(df) # wyswietl calosc lub pofiltrowany zbior danych

fig, ax = plt.subplots() # stworz miejsce na wykres
ax.hist(df.prep_time, bins=5) # wyswietl histogram w zaleznosci od czasu przygotowania posilku w minutach
ax.set_xlabel("Czas przygotowania w danym czasie (minuty)") # nazwij os X
ax.set_ylabel("Ilosc produktow") # nazwij os Y
st.pyplot(fig) # wyswietl wykres histogramu

