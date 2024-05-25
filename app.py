import streamlit as st

info_dict = {"C02_Emissions": "", "Number of Women in Leadership positions": "", "Anti-Corruption measures": ""}

class CH_Report:

    def __init__(self, x, y):
        print("Create a new object of the CH_Report class")
        self.name = x
        self.type = y
        self.information = info_dict



tab1, tab2, tab3 = st.tabs(["Questionnaire", "KPI Selection", "Fill in values"])

with tab1:
    st.title("Welcome to the Obli-Gator!")

    st.header("First, let us get started on some questions")

    name = st.text_input("What is the name of your company?")

    type = st.radio("What is your compliance type?",["EU", "CH", "US"])

    firstreport = CH_Report(name, type)


    if st.button("Submit"):
        st.write(type)
        st.write(firstreport.information)

with tab2:
    st.write(type)


with tab3:
    st.write(firstreport.information)

        


