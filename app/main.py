import streamlit as st

st.set_page_config(page_title="Medical AI Agent", page_icon="🏥")

st.title("🏥 Medical AI Agent")
st.markdown("### Coming Soon")

st.info("""
This is a placeholder for the Medical AI Agent.

The full agent with autonomous reasoning, clinical tools, and RAG system 
is under development.

**Planned Features:**
- Multi-step reasoning
- Clinical decision support
- Literature search
- Drug interactions
- SOAP note generation
""")

if st.button("Test"):
    st.success("App is working!")