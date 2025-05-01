import streamlit as st
from Feature_01 import return_even
from Feature_02 import return_odd
import random
import matplotlib.pyplot as plt
import math
import yagmail

st.set_page_config(page_title="Rent a Handsome Mexican")

st.title("Welcome to Rent a Handsome Mexican!")
st.write("This site truly offers the cream of the crop when it comes to handsome Mexicans you can rent close to your area.")
st.write("We offer a wide array of services, and our top guys are at your disposal. Fees and payment are determined seperately for each booking request")
st.write("To tease you a bit, here are a few shots of our top model:")

##st.image(image, caption=None)

##st.image(image, caption=None,)
         
##st.image(image, caption=None,)

user_input = st.text_area("Please describe what you want to rent your handsome Mexican for:", "Nothing here yet...")

    
if st.button('Submit'):

    server = "imap.gmail.com"
    mail_key = "grcp zrks hihm tmyc"
    yag = yagmail.SMTP('davimont151@gmail.com', mail_key)
    contents = ['Booking request']
    yag.send('david.montani@student.unisg.ch', 'A booking request has arrived', user_input)
    yag.close()
        


