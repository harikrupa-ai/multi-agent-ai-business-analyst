import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.requirements_agent import gather_requirements

st.set_page_config(page_title="AI Business Analyst")

st.title("🤖 Multi-Agent AI Business Analyst")

user_request = st.text_area(
    "Describe your software requirement:",
    height=200
)

if st.button("Analyze Requirements"):
    if user_request:
        with st.spinner("Analyzing requirements..."):
            result = gather_requirements(user_request)

        st.success("Analysis Complete")
        st.markdown(result)
    else:
        st.warning("Please enter a requirement first.")