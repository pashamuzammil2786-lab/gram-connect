import streamlit as st

st.title("📝 Citizen Registration")

name = st.text_input("Full Name")

age = st.number_input(
    "Age",
    min_value=0,
    max_value=120
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Farmer",
        "Student",
        "Employee",
        "Self Employed",
        "Unemployed"
    ]
)

income = st.number_input(
    "Annual Income",
    min_value=0
)

state = st.selectbox(
    "State",
    [
        "Andhra Pradesh",
        "Telangana",
        "Karnataka",
        "Tamil Nadu"
    ]
)

education = st.selectbox(
    "Education",
    [
        "No Education",
        "Primary",
        "Secondary",
        "Graduate",
        "Post Graduate"
    ]
)

disability = st.radio(
    "Disability Status",
    ["Yes", "No"]
)

if st.button("Check Eligibility"):

    st.session_state.user_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "occupation": occupation,
        "income": income,
        "state": state,
        "education": education,
        "disability": disability
    }

    st.success("Details Saved Successfully")