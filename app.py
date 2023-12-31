import streamlit as st
from Feature_01 import return_even
from Feature_02 import return_odd
import random
import matplotlib.pyplot as plt
import math

st.set_page_config(page_title="Fondue Optimizer")

st.title("Welcome to the Fondue Optimizer! :cheese_wedge:")

st.write("First things first: Select thine cheese preferences")

cheese_type = st.radio(
    "Which cheese calls to you",
    ["Hardcore Swiss traditionalist", "Visiting tourist", "American glutton"],
    captions = ["Wilkomme Eidgenoss!", "Welcome to Switzerland", "Your cheese isn't actually cheese, but okay"])


number_input = st.number_input("Enter how many friends will partake in your fondue (whole numbers only please):", min_value=1, max_value=15, value=5, step=1)

hunger_level = st.radio("Are you and your friends hungry hungry hippos or trendy fashionistas on a diet?", 
                        ["We have small tummies", "I would like to have room for dessert", "Put me in a coma"])


if hunger_level == "We have small tummies":
    level = 150
elif hunger_level == "I would like to have room for dessert":
    level = 200
elif hunger_level == "Put me in a coma":
    level = 300

st.write("Check that all of your imputs are correct! Once you have verified this, click the button below")

if st.button('Get recipe'):

    total = level * number_input
    wine = round(total * 0.0044, 1)
    maizena = total // 200
    st.subheader("We will now calculate the rest of the ingredients for your ideal recipe!", divider='red')

    if cheese_type == "Hardcore Swiss traditionalist":
        st.write("Moitie-moitie is an excellent fondue mix. Go buy:")
        st.write(f"{int(total/2)}g of Gruyère cheese (mild)")
        st.write(f"{int(total/2)}g of Vacherin fribourgeois cheese (strong)")
        st.write(f"Add {wine} dl of white wine (Fondent du Valais is ideal)")
        st.write(f"And don't forget to add {maizena} tea-spoons of Maizena")

    elif cheese_type == "Visiting tourist":

        st.write("We will get you started with some simple cheesy goodness:")
        st.write(f"{int(total/2)}g of Swiss mountain cheese (mild)")
        st.write(f"{int(total/2)}g of Gruyère cheese (mild)")
        st.write(f"Add {wine} dl of white wine (Fondent du Valais is ideal)")
        st.write(f"And don't forget to add {maizena} tea-spoons of Maizena")


    elif cheese_type == "American glutton":
        st.write("I disapprove of your lifestyle choices. I just want you to know. Go get")
        st.write(f"{int(total/2)}g of Cheddar")
        st.write(f"{int(total/2)}g of 'Swiss' cheese (whatever that means)")
        st.write(f"Add {wine} dl of white wine (Fondent du Valais is ideal)")
        st.write(f"And don't forget to add {maizena} tea-spoons of Maizena")

    st.write("People usually also like to add pepper and nutmeg - don't be shy in spicing things up!")
    st.write("Enjoy!")