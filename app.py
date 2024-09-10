import streamlit as st
import docx
import pandas as pd 
import io
import plotly.express as px


tab1, tab2, tab3 = st.tabs(["Questionnaire", "Questionnaire Part 2", "Final evaluation"])

with tab1:
    st.title("Welcome to the the Mock-up Questionnaire")

    hockey_score = st.slider("How much do you enjoy hockey?", min_value=1, max_value=5)

    football_score = st.slider("How much do you enjoy football?", min_value=1, max_value=5)
    

with tab2:
    st.title("Questionnaire Part 2")
    
    rugby_score = st.slider("How much do you enjoy rugby?", min_value=1, max_value=5)

    tennis_score = st.slider("How much do you enjoy tennis?", min_value=1, max_value=5)

    triathlon_score = st.slider("How much do you enjoy Triathlon?", min_value=1, max_value=5)



with tab3:
    st.write("Results") 

    df = pd.DataFrame(dict(
    r=[hockey_score, football_score, rugby_score, tennis_score , triathlon_score],
    theta=['Hockey','Football','Rugby',
           'Tennis', 'Triathlon']))
    fig = px.line_polar(df, r=5, theta='theta', line_close=True)
    st.plotly_chart(fig)
