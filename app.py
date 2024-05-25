import streamlit as st

info_dict = {"C02_Emissions": "", "Number of Women in Leadership positions": "", "Anti-Corruption measures": ""}

class Gen_Report:

    def __init__(self, x, y, z):
        print("Create a new object of the CH_Report class")
        self.name = x
        self.type = y
        self.code = z
        self.information = info_dict



tab1, tab2, tab3 = st.tabs(["Basic Questionnaire", "Report_Design", "Fill in values"])

with tab1:
    st.title("Welcome to the Obli-Gator!")
    st.write("This tool will help you with designing, setting up and drafting your ESG reports in both human-readable and machine-readable formats!")
    st.header("First, let us get started on some questions")

    name = st.text_input("What is the name of your company?")

    type = st.radio("What is your compliance region you need to report in?",["EU", "CH", "US"])

    sic_code = st.text_input("Please input your company's SIC code (Operating Area)")
    

    firstreport = Gen_Report(name, type, sic_code)

    if st.button("Submit"):
        if type == "EU":
            st.write("You need to comply with the standards for the EU market. These will be published in 2026.")
        elif type == "US":
            st.write("The US has no regulatory mandate on publishing standards.")

        elif type == "CH":
            st.write("The Swiss Confederation legally obliges you to publish a report on how well you are underway concerning your ESG Goals")
            st.write("The Obli-Gator will help you navigate this challenge. Please swap to the Report Design Section")

with tab2:
    st.title("Obli-Gator report design")
    st.write("As a company operating in the Swiss market, you must comply with the new laws governing ESG reporting as listed in CO Article 956c and beyond")
    st.write("We will help you become compliant by showing you what the law demands, tailor strategies for compliance, and give you an overview how other companies in your sector address these problems")




with tab3:
    st.write(firstreport.information)

        


