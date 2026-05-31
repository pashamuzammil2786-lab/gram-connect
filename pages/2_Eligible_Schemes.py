import streamlit as st

from backend.eligibility import (
    check_eligibility,
    explain_near_matches
)

st.title("🎯 Eligible Government Schemes")

if "user_data" not in st.session_state:
    st.warning("Please register first.")
    st.stop()

user_data = st.session_state["user_data"]

eligible_schemes = check_eligibility(user_data)

if eligible_schemes:

    st.success(
        f"Found {len(eligible_schemes)} eligible scheme(s) for you."
    )

    for scheme in eligible_schemes:

        st.subheader(f"📌 {scheme['scheme_name']}")

        st.write("### Description")
        st.write(scheme["description"])

        st.write("### Benefits")
        st.write(scheme["benefits"])

        st.write("### Why You Are Eligible")

        for reason in scheme["reasons"]:
            st.write(f"✅ {reason}")

        st.write("### Application Process")
        st.write(scheme["application_process"])

        if scheme["application_link"]:
            st.markdown(
                f"🔗 [Apply Here]({scheme['application_link']})"
            )

        st.markdown("---")

else:

    st.error("No exact matches found.")

    st.write("### Closest Matching Schemes")

    near_matches = explain_near_matches(user_data)

    for scheme in near_matches:

        st.subheader(f"📌 {scheme['scheme_name']}")

        st.write(scheme["description"])

        st.write("Requirements not met:")

        for item in scheme["missing"]:
            st.write(f"❌ {item}")

        st.markdown("---")