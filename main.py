import streamlit as st
from src.pages import home, about, projects, live_apps, skills, contact
from src.utils.styling import load_css

# Page configuration
st.set_page_config(
    page_title="Your Name - AI/ML Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Load custom CSS
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("🤖 AI/ML Portfolio")
    page = st.sidebar.selectbox("Navigate to:", 
                               ["🏠 Home", "👤 About", "🚀 Projects", "🛠️ Live Apps", "💡 Skills", "📬 Contact"])
    
    # Page routing
    if page == "🏠 Home":
        home.show()
    elif page == "👤 About":
        about.show()
    elif page == "🚀 Projects":
        projects.show()
    elif page == "🛠️ Live Apps":
        live_apps.show()
    elif page == "💡 Skills":
        skills.show()
    elif page == "📬 Contact":
        contact.show()

if __name__ == "__main__":
    main()