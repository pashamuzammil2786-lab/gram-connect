import streamlit as st

st.title("🎯 Eligible Schemes")

if "user_data" not in st.session_state:
    st.warning("Please register first.")
else:

    st.success("Based on your profile")

    schemes = [
        {
            "name": "PM Kisan",
            "benefit": "₹6000 per year"
        },
        {
            "name": "Ayushman Bharat",
            "benefit": "₹5 Lakh Health Insurance"
        },
        {
            "name": "PM Awas Yojana",
            "benefit": "Housing Assistance"
        }
    ]

    for scheme in schemes:

        st.subheader(scheme["name"])
        st.write("Benefit:", scheme["benefit"])
        st.markdown("---")