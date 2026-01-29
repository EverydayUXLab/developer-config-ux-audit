import streamlit as st

st.set_page_config(
    page_title="Developer Configuration Tool UX Audit",
    layout="wide"
)

st.sidebar.title("Audit Sections")

sections = [
    "Overview",
    "Configuration Areas Reviewed",
    "UX Issues Identified",
    "Risk & Safety Patterns",
    "Outcomes & Recommendations"
]

selected = st.sidebar.radio("", sections)

st.title("Developer Configuration Tool UX Audit")
st.caption("Developer Tools · UX & Performance Audit (Anonymized)")
st.divider()

if selected == "Overview":
    st.header("Audit Context")
    st.write("""
    This UX audit reviews a developer-facing configuration interface used
    to manage runtime flags, environment variables, and production toggles.

    The interface exposed powerful controls but made it easy to introduce
    accidental misconfigurations, particularly under time pressure.
    """)
    st.info(
        "Focus: risk reduction, clarity, and safety — not restricting advanced users."
    )

elif selected == "Configuration Areas Reviewed":
    st.header("Configuration Areas Reviewed")
    st.markdown("""
    - Environment variables
    - Feature flags
    - Runtime toggles
    - Deployment-specific overrides
    """)

elif selected == "UX Issues Identified":
    st.header("UX Issues Identified")
    st.markdown("""
    **High-risk UX patterns**
    - Destructive actions placed near safe actions
    - Defaults that were unsafe or unclear
    - Lack of preview before applying changes

    **Validation gaps**
    - Missing warnings for risky combinations
    - No confirmation for high-impact changes
    """)

elif selected == "Risk & Safety Patterns":
    st.header("Risk & Safety Patterns")
    st.markdown("""
    - Lack of impact visibility before save
    - No differentiation between safe vs risky flags
    - Inconsistent confirmation behavior
    """)
    st.warning(
        "Accidental misconfiguration was possible without clear user intent."
    )

elif selected == "Outcomes & Recommendations":
    st.header("Outcomes & Value")
    st.markdown("""
    - Reduced likelihood of accidental configuration changes
    - Improved clarity for first-time and on-call users
    - Lower reliance on external documentation
    - Safer workflows without limiting expert flexibility
    """)
    st.success(
        "All recommendations were UX-level and backend-safe."
    )
