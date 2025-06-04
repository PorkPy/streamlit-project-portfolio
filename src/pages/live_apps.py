import streamlit as st
from data.projects_data import LIVE_APPS

def show():
    """Display the live apps page"""
    st.title("🛠️ Live Interactive Applications")
    
    st.markdown("""
    These are fully functional Streamlit applications that demonstrate my AI/ML work. 
    Each app provides hands-on interaction with the underlying models and systems.
    """)
    
    # Display apps in a grid
    for i in range(0, len(LIVE_APPS), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(LIVE_APPS):
                app = LIVE_APPS[i + j]
                with col:
                    st.markdown(f"""
                    <div class="app-preview">
                        <h4>{app['title']}</h4>
                        <p>{app['description']}</p>
                        <p><strong>Key Features:</strong></p>
                        <ul>
                    """, unsafe_allow_html=True)
                    
                    for feature in app['features']:
                        st.markdown(f"<li>{feature}</li>", unsafe_allow_html=True)
                    
                    st.markdown("</ul>", unsafe_allow_html=True)
                    
                    # Tech tags
                    for tech in app['tech']:
                        st.markdown(f'<span class="skill-tag">{tech}</span>', 
                                  unsafe_allow_html=True)
                    
                    st.markdown(f"""
                        <br><br>
                        <a href="{app['url']}" class="demo-button" target="_blank">🚀 Launch App</a>
                    </div>
                    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    ### 🔗 Unified Experience
    
    All applications are built with consistent design principles and can cross-reference each other, 
    creating a cohesive ecosystem of AI tools. The portfolio serves as the central hub connecting 
    all specialized applications.
    """)