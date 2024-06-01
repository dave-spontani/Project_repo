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
    st.write("We munch and crunch your lame paperwork for you so you can focus on providing the best ESG reports for your company")
    st.image('obligator.jpg', caption='Our trusty Obli-Gator hard at work')
    st.write("This tool will help you with designing, setting up and drafting your ESG reports in both human-readable and machine-readable formats!")
    st.header("First, let us get started on some questions")

    name = st.text_input("What is the name of your company?")

    type = st.radio("What is your compliance region you need to report in?",["EU", "CH", "US"])

    sic_code = st.selectbox("What industry do you operate in?",("Agriculture", "Mining", "Finance"))

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

    st.write(f"The sector you selected is {firstreport.code}")
    if firstreport.code == "Mining":
        st.write("Mining operations and other extractive industries need to report on additional compliance topics.")
        st.write("We will guide you through these steps during the selection process")
    else:
        pass

    st.header("Framework")
    st.write("Most companies choose a specific framework they want to follow. While this is not strictly necessary under the Code of Obligations, it is encouraged")
    st.write("We can help you on your journey to set up framework-compliance - or you can choose to fulfil the legal obligations solely by following the letter of the law (OR compliance)")
    st.write("Frameworks are typically a lot more time intensive and comprehensive than OR-Compliance, but do enjoy a greater scope and cohesive reporting strategy")
    compliance_type = st.selectbox("Please choose the type of compliance you want to have",["OR-compliance", ""])

    st.write("You have chosen your compliance type and given us your industry you are working in.")
    st.write("Based on the law, these are the broad areas you must report progress in. We will show you what legal provsions you must comply with, and what KPI's othe companies use in order to comply:")
    st.write("We will guide you through the best selection process for your reporting goals. Choose KPI you are certain you can obtain within your company")


    st.header("Environmental Reporting")
    st.write("The legal provision to supply Environmental Reporting is blah blah blah")
    st.write("Concretely, this means you need to track progress in this field. Most companies in your field have X KPI in this reporting criteria. Here is a selection of KPI that other companies in your area use in order to comply with this requirement:")
    options1 = st.selectbox("What Env KPI's do you want to choose for your report",[list(info_dict.keys())[0]])
    st.write("Et cetera....")

    st.header("Social Reporting")
    st.write("The legal provision to supply Environmental Reporting is blah blah blah")
    st.write("Concretely, this means you need to track progress in this field. Most companies in your field have X KPI in this reporting criteria. Here is a selection of KPI that other companies in your area use in order to comply with this requirement:")
    options2 = st.selectbox("What Social KPI's do you want to choose for your report",[list(info_dict.keys())[1]])
    st.write("Et cetera....")

    st.header("Governance Reporting")
    st.write("The Governance provision to supply Social Reporting is blah blah blah")
    st.write("Concretely, this means you need to track progress in this field. Most companies in your field have X KPI in this reporting criteria. Here is a selection of KPI that other companies in your area use in order to comply with this requirement:")
    options3 = st.selectbox("What Governance KPI's do you want to choose for your report",[list(info_dict.keys())[2]])
    st.write("Et cetera....")


    st.write("Here it would be nice to have a sort of Tracker that tells you how comprehensive the reporting is. We can weigh different KPI and based on these scores and show people how well they are doing comparatively")

with tab3:
    st.write("Now that you have selected the report framework and the KPI you want to focus on, we can move to building the report!")

    st.write("Please input the values for your chosen KPI.")

    st.number_input(f"Please input a value for the following KPI: {options1}")

    st.number_input(f"Please input the value for the following KPI: {options2}")

    st.number_input(f"Please input any value for the following KPI: {options2}")

    st.write("No time to do this now -but you get the gist, this is the actual building section of the whole solution.")
        


