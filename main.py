import streamlit as st
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import only the modules that definitely exist
from pages import home, about, projects, live_apps, skills, contact
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
    
    # Main navigation only for now
    page = st.sidebar.selectbox("Portfolio Navigation:", 
                               ["🏠 Home", "👤 About", "🚀 All Projects", "🛠️ Live Apps", "💡 Skills", "📬 Contact"])
    
    # Note about project pages
    st.sidebar.markdown("---")
    st.sidebar.info("Individual project pages coming soon!")
    
    # Page routing
    if page == "🏠 Home":
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