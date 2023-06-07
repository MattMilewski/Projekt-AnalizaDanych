# Projekt analiza danych

## Uruchomienie

Aby uruchomic projekt, nalezy:
1. Wejsc do katalogu z plikiem main.py
2. Zainstalowac biblioteki poleceniem `pip install -r requirements.txt`
3. Uruchomic w terminalu polecenie `streamlit run main.py`

## Analiza kodu

Plik main.py realizuje nastepujace operacje:
1. import streamlit do wizualizacji rozwiazania
2. import pandas do dzialania na danych tabelarycznych
3. import pyplot z biblioteki matplotlib do wykresu histogramu
4. wyswietl tytul programu
5. wyswietl label nad inputem ze skladnikami i pobierz skladniki w postaci tekstu
6. zamien wszystkie znaki na male
7. podziel string na tablice skladnikow dzielac po przecinku
8. wyswietl tablice wpisanych skladnikow
9. wczytaj dane z przepisami
10. jesli uzytkownik cos wpisal, dokonaj filtrowania, jesli nie to wyswietl wszystko
11. wybierz podzbior danych na podstawie warunku kolumny ingredients:
12. dla danego wiersza (ingredients_string) sprawdz czy kazdy skladnik (z malych liter) zawiera sie w liscie input_ingredients)
13. zresetuj index aby ponumerowac pofiltrowane przepisy w kolejnosci
14. wyswietl calosc lub pofiltrowany zbior danych
15. stworz miejsce na wykres
16. wyswietl histogram w zaleznosci od czasu przygotowania posilku w minutach
17. nazwij os X
18. nazwij os Y
19. wyswietl wykres histogramu

