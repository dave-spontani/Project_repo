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


    st.header("Lets start by setting some goals!")
    st.write("Do you have a regular income? If yes, how high is your salary (how much lands on your bank account)?")
    salary = st.number_input("Input your salary here")
    st.write("Great! Next, allocate a budget to your most used categories. A suggestion list is down below. Feel free to add other categories.")
    rent = st.number_input("Input your rent payments here")
    groceries = st.number_input("Input your grocery payments here")
    savings = st.number_input("How much would you like to save every month?")
    st.write("(Dave here. You get the idea. In the end we make a rough calculation and showcase the biggest savings potentials)")

    st.write("Excellent! Thank you for submitting your plan. If you are interested in a budget consultation with our friendly budgeting advisor 'RoboDave', feel free to press the button. You can always come back to this feature later.")
    but = st.button("Take me to RoboDave!")
    if but:
        st.write("Man I was hoping you wouldnt test this out. Welp. I'm not that fast, this is only a concept demo after all, so this button leads nowhere")
        time.sleep(2)
        st.write("But do feel free to navigate to the second tab")

    if int(salary) > 0 and int(savings) > 0:

        try: savings_rate = round((int(savings) / int(salary)) * 100)

        except: savings_rate = 0

    else: savings_rate = 0

with tab2:
    st.title("Welcome to your Investing Profile!")

    st.header("We would like to ask you a few questions about the following topics: Your savings rate, your risk profile, your investing strategy, and your sustainability preferences")
    st.write("Here, obviously it would be different questions so we can arrive at a profile for the person. As a placeholder, they will just tell us.")
    st.subheader("Savings rate")
    st.write(f"It looks like your savings rate is {savings_rate}%")
    if savings_rate < 25:
        st.write("This puts you into the 'Small saver category'")
        saver_profile = "S" ##Saver
    else:
        st.write("This puts you into the 'Big saver category'")
        saver_profile = "E" ##Enjoyer
    
    st.subheader("Risk profile")
    risk = st.selectbox(
    "Are you prepared to see the value of your investments and savings to drastically shift? (i.e Losses of up to 50%)",
    ("Yes", "No"),)
    if risk == "Yes":
        risk_profile = "V" ##Volatile
    else: 
        risk_profile = "C" ##Conservative

    st.subheader("Investments")
    style = st.selectbox(
    "Do you want to invest in Traditional (Stocks, Bonds) or more Non-Traditional Investments (i.e Cryptocurrencies, Alternative investments)?",
    ("Traditional", "Non-Traditional"),)

    if style == "Traditional":
        style_profile = "T" ##Traditional
    else: 
        style_profile = "N" ##New-Age


    st.subheader("Sustainability preferences")
    sustainable= st.selectbox(
    "Do you want to invest more sustainable solutions in line with ESG goals, or do you prefer more market-oriented investments?",
    ("Sustainable", "Markets"),)


    if sustainable == "Sustainable":
        sust_profile = "S" ##Sustainable
    else: 
        sust_profile = "M" ##Markets

st.write("Thank you! We will calculate the results. Just a moment")

time.sleep(3)

buetton = st.button("Alright, we are ready. Press this button to see your profile results")

if buetton:
    st.write("HAHA! I actually have results here!")
    st.write(f"It looks like you are a {saver_profile}-{risk_profile}-{style_profile}-{sust_profile}")
    st.write("This means you:")
    time.sleep(1)
    st.write("Are more of a Saver (S) or an Enjoyer (E)")
    time.sleep(1)
    st.write("Prefer potentially Volatile Investments (V) or more conservative investments (C)")
    time.sleep(1)
    st.write("Want to invest in more Sustainable (S) or more Market-oriented (M) solutions")
    time.sleep(2)

    st.write("Our Robo-Advisor has done its thing and punched up a portfolio for you. Have a look!")

    brutton = st.button("This totally takes you to a portfolio, I swear")

    if brutton: 
        st.write("Psych!")


with tab3:
    st.write("Results") 
    st.write("Left blank for now so I can go get lunch.")

