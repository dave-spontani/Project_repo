import streamlit as st
import docx
import pandas as pd 
import io

info_dict = {"C02_Emissions in Megatonnes this year": "", "Number of Women in Leadership positions as a percentage": "", "Anti-Corruption initiatives launches this year": ""}

class Gen_Report:

    def __init__(self, x, y, z):
        print("Create a new object of the CH_Report class")
        self.name = x
        self.type = y
        self.code = z
        self.information = info_dict

tab1, tab2, tab3 = st.tabs(["Questionnaire", "Questionnaire Part 2", "Final evaluation"])

with tab1:
    st.title("Welcome to the the Mock-up Questionnaire")

with tab2:
    st.title("Questionnaire Part 2")


with tab3:
    st.write("Results") 
