import streamlit as st
import docx
import pandas as pd 
import io
import plotly.express as px


tab1, tab2, tab3 = st.tabs(["Questionnaire", "Questionnaire Part 2", "Final evaluation"])

with tab1:
    st.title("Welcome to the the Mock-up Questionnaire")

    st.slider("How much do you enjoy hockey?", min_value=1, max_value=7)
    

with tab2:
    st.title("Questionnaire Part 2")
    st.slider("How much do you enjoy football?", min_value=1, max_value=7)


with tab3:
    st.write("Results") 

    df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.plotly_chart(fig)
