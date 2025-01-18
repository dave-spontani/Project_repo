import streamlit as st
import docx
import pandas as pd 
import io
import plotly.express as px
import time


tab1, tab2, tab3 = st.tabs(["Budget", "Saving & Investment Goals", "Final evaluation"])

with tab1:
    st.title("Welcome to the Equinox project!")
    st.write("Lets start with some questions. First off, let us define your budget goals!")


    st.subtitle("Lets start by setting some goals!")
    st.write("Do you have a regular income? If yes, how high is your salary (how much lands on your bank account)?")
    salary = st.number_input("Input your salary here")
    st.write("Great! Next, allocate a budget to your most used categories. A suggestion list is down below. Feel free to add other categories.")
    rent = st.number_input("Input your rent payments here")
    groceries = st.number_input("Input your grocery payments here")
    savings = st.number_input("How much would you like to save every month?")
    st.write("Dave here. You get the idea. In the end we make a rough calculation and showcase the biggest savings potentials")

    st.write("Excellent! Thank you for submitting your plan. If you are interested in a budget consultation with our friendly budgeting advisor 'RoboDave', feel free to press the button. You can always come back to this feature later.")
    but = st.button("Take me to RoboDave!")
    if but:
        st.write("Man I was hoping you wouldnt test this out. Welp. I'm not that fast, this is only a concept demo after all, so this button leads nowhere")
        time.sleep(2)
        st.write("But do feel free to navigate to the second tab")



with tab2:
    st.title("")
    
    rugby_score = st.slider("How much do you enjoy rugby?", min_value=1, max_value=5)

    tennis_score = st.slider("How much do you enjoy tennis?", min_value=1, max_value=5)

    triathlon_score = st.slider("How much do you enjoy Triathlon?", min_value=1, max_value=5)



with tab3:
    st.write("Results") 

