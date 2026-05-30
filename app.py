import streamlit as st

st.set_page_config(
    page_title="Gram Connect",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Gram Connect")

st.subheader("Government Scheme Eligibility Finder")

st.write(
    "Gram Connect helps citizens discover government welfare schemes they are eligible for based on their profile."
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("✅ Find Eligible Schemes")

with col2:
    st.info("✅ Simple and Easy Interface")

st.markdown("---")

st.success("Use the left sidebar to get started.")