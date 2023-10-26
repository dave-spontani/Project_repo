import streamlit as st
from Feature_01 import return_even
from Feature_02 import return_odd
import random
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Fondue Optimizer", page_icon=":cheese:")

st.title("Welcome to the Fondue Optimizer!")

number_input = st.number_input("Enter how much cheese in total you will add (in Grams)")

st.write("We will now calculate the rest of the ingredients for your ideal recipe!")

if number_input:

    st.write("Moitie-moitie is an excellent fondue mix. Go buy:")
    st.write(f"{number_input/2}g of Gruyère cheese (mild)")
    st.write(f"{number_input/2}g of Vacherin fribourgeois cheese (strong)")

    