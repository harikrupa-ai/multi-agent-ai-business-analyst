import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from agents.requirements_agent import gather_requirements
from agents.user_story_agent import generate_user_stories
from agents.risk_agent import analyze_risks
from agents.architecture_agent import suggest_architecture

# -----------------------
# Streamlit Configuration
# -----------------------
st.set_page_config(
    page_title="AI Business Analyst",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Business Analyst")

# -----------------------
# User Input
# -----------------------
user_request = st.text_area(
    "Describe your software requirement:",
    height=200
)

# -----------------------
# Run Analysis
# -----------------------
if st.button("Run Multi-Agent Analysis"):

    if user_request:

        with st.spinner("Requirements Agent analyzing..."):
            requirements = gather_requirements(user_request)

        with st.spinner("User Story Agent generating stories..."):
            user_stories = generate_user_stories(requirements)

        with st.spinner("Risk Agent analyzing risks..."):
            risks = analyze_risks(requirements)

        with st.spinner("Architecture Agent creating solution design..."):
            architecture = suggest_architecture(requirements)

        st.success("Multi-Agent Analysis Complete")

        # -----------------------
        # Tabs
        # -----------------------
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "📋 Requirements",
                "📝 User Stories",
                "⚠️ Risks",
                "🏗️ Architecture"
            ]
        )

        with tab1:
            st.markdown(requirements)

        with tab2:
            st.markdown(user_stories)

        with tab3:
            st.markdown(risks)

        with tab4:
            st.markdown(architecture)

        # -----------------------
        # Download Report
        # -----------------------
        full_report = f"""
# Multi-Agent AI Business Analyst Report

## Stakeholder Request
{user_request}

---

## 1. Requirements Analysis
{requirements}

---

## 2. User Stories
{user_stories}

---

## 3. Risk Analysis
{risks}

---

## 4. Architecture Recommendation
{architecture}
"""

        st.download_button(
            label="📥 Download Business Analysis Report",
            data=full_report,
            file_name="business_analysis_report.md",
            mime="text/markdown"
        )

    else:
        st.warning("Please enter a requirement first.")