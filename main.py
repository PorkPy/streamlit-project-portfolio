import streamlit as st
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now import the modules
from pages import home, about, projects, live_apps, skills, contact
from pages import diy_llm_project, jess_project, nhs_data_project
from utils.styling import load_css

# Page configuration
st.set_page_config(
    page_title="Dom McKean - AI/ML Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Load custom CSS
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("🤖 Dom McKean")
    st.sidebar.markdown("*AI/ML Engineer & Data Scientist*")
    
    # Main navigation
    page = st.sidebar.selectbox("Portfolio Navigation:", 
                               ["🏠 Home", "👤 About", "🚀 All Projects", "🛠️ Live Apps", "💡 Skills", "📬 Contact"])
    
    # Project-specific pages
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Featured Projects:**")
    project_page = st.sidebar.selectbox("Deep Dive:", 
                                       ["Select Project...", 
                                        "🧠 DIY Transformer LLM", 
                                        "👩‍🏫 Jess - AI Psychology Assistant", 
                                        "🏥 NHS Pharmacy Analytics"])
    
    # Page routing
    if project_page != "Select Project...":
        if project_page == "🧠 DIY Transformer LLM":
            diy_llm_project.show()
        elif project_page == "👩‍🏫 Jess - AI Psychology Assistant":
            jess_project.show()
        elif project_page == "🏥 NHS Pharmacy Analytics":
            nhs_data_project.show()
    elif page == "🏠 Home":
        home.show()
    elif page == "👤 About":
        about.show()
    elif page == "🚀 All Projects":
        projects.show()
    elif page == "🛠️ Live Apps":
        live_apps.show()
    elif page == "💡 Skills":
        skills.show()
    elif page == "📬 Contact":
        contact.show()

if __name__ == "__main__":
    main()