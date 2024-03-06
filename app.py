import streamlit as st
from Feature_01 import return_even
from Feature_02 import return_odd
import random
import matplotlib.pyplot as plt
import math
import yagmail

st.set_page_config(page_title="Rent-a-Swiss-boyfriend :cheese_wedge:")

st.title("Welcome to the Rent-a-Swiss-boyfriend - your solution to finding your dream cheese-loving gentleman")

st.write("First things first: Select thine cheese preferences")

man_type = st.radio(
    "Which Swiss dream man calls to you",
    ["Hardcore (probably inbred) Swiss traditionalist", "International Zürich boy", "French-speaking slob"],
    captions = ["(Dating level: Impossible if not a milkmaid)", "Our absolute best-seller", "Will insult your friends and quote pretentious french movies at you"])
    

if man_type == "Hardcore (probably inbred) Swiss traditionalist":
    st.write("So sorry, we are out of stock of this option for now.")

elif man_type == "French-speaking slob":
    st.write("We are (luckily) not offering this option anymore")


elif man_type == "International Zürich boy":
    st.write("Excellent choice. This is by far our most booked option, and at 50 USD per hour, a real catch!")
    st.write("As this boi is in high demand, please specify the use case for which you will need to rent a swiss boyfriend. We will contact you if our agent finds this assignment pleasing")
    user_input = st.text_area("Please describe your use case here:", "Nothing here yet...")

    
    if st.button('Submit'):

        server = "imap.gmail.com"
        mail_key = "grcp zrks hihm tmyc"
        yag = yagmail.SMTP('davimont151@gmail.com', mail_key)
        contents = ['Booking request']
        yag.send('david.montani@student.unisg.ch', 'A booking request has arrived', user_input)
        yag.close()
        


