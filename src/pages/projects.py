import streamlit as st
from src.data.projects_data import PROJECTS, PROJECT_CATEGORIES

def show():
    """Display the projects page"""
    st.title("🚀 Projects Portfolio")
    
    # Project categories
    category = st.selectbox("Filter by domain:", PROJECT_CATEGORIES)
    
    # Filter projects
    if category != "All Projects":
        filtered_projects = [p for p in PROJECTS if p["category"] == category]
    else:
        filtered_projects = PROJECTS
    
    # Display projects
    for i, project in enumerate(filtered_projects):
        _render_project_card(project)

def _render_project_card(project):
    """Render a single project card"""
    with st.container():
        st.markdown(f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p><strong>Domain:</strong> {project['category']}</p>
            <p>{project['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Key Achievements
        st.markdown("**🎯 Key Achievements:**")
        for achievement in project['achievements']:
            st.markdown(f"""
            <div class="achievement-item">
                • {achievement}
            </div>
            """, unsafe_allow_html=True)
        
        # Impact
        if project.get('impact'):
            st.markdown(f"""
            <div class="impact-metric">
                <strong>💡 Impact:</strong> {project['impact']}
            </div>
            """, unsafe_allow_html=True)
        
        # Tech stack tags
        st.markdown("**🛠️ Technologies:**")
        _render_tech_stack(project['tech_stack'])
        
        # Links
        st.markdown("**🔗 Links:**")
        _render_project_links(project['links'])
        
        st.markdown("---")

def _render_tech_stack(tech_stack):
    """Render technology stack tags"""
    cols = st.columns(min(len(tech_stack), 5))
    for j, tech in enumerate(tech_stack[:5]):
        with cols[j % 5]:
            st.markdown(f'<span class="skill-tag">{tech}</span>', 
                      unsafe_allow_html=True)
    
    # Additional tech tags if more than 5
    if len(tech_stack) > 5:
        remaining_cols = st.columns(len(tech_stack) - 5)
        for j, tech in enumerate(tech_stack[5:]):
            with remaining_cols[j]:
                st.markdown(f'<span class="skill-tag">{tech}</span>', 
                          unsafe_allow_html=True)

def _render_project_links(links):
    """Render project links"""
    link_cols = st.columns(len(links))
    for j, (link_type, url) in enumerate(links.items()):
        with link_cols[j]:
            if link_type == "streamlit":
                st.markdown(f"[🚀 Streamlit App]({url})")
            elif link_type == "demo":
                st.markdown(f"[🎬 Live Demo]({url})")
            elif link_type == "github":
                st.markdown(f"[💻 GitHub]({url})")
            elif link_type == "api":
                st.markdown(f"[🔌 API]({url})")
            elif link_type == "paper":
                st.markdown(f"[📄 Paper]({url})")
            elif link_type == "blog":
                st.markdown(f"[📝 Blog]({url})")