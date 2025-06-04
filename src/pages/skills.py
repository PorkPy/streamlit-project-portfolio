import streamlit as st
import plotly.express as px

def show():
    """Display the skills page"""
    st.title("💡 Technical Skills & Expertise")
    
    # Skills data updated for AI/ML focus
    skills_data = {
        "AI/ML Frameworks": ["PyTorch", "TensorFlow", "Transformers", "LangChain", "Scikit-learn"],
        "Language Models": ["GPT Architecture", "BERT", "Claude", "OpenAI APIs", "AWS Bedrock"],
        "Cloud & MLOps": ["AWS Lambda", "API Gateway", "Docker", "Terraform", "GitHub Actions"],
        "Programming": ["Python", "SQL", "JavaScript", "Git", "Linux"],
        "Data & Visualization": ["Pandas", "NumPy", "Plotly", "Streamlit", "Statistical Analysis"],
        "NLP & Research": ["Attention Mechanisms", "Prompt Engineering", "Research Evaluation", "Academic Writing"],
        "Databases & APIs": ["SQLite", "PostgreSQL", "REST APIs", "arXiv API", "Pharmaceutical APIs"],
        "Specialized Domains": ["Educational Psychology", "Mental Health Tech", "Academic Publishing", "Healthcare Analytics"]
    }
    
    # Display skills in columns
    col1, col2 = st.columns(2)
    
    categories = list(skills_data.keys())
    for i, category in enumerate(categories):
        if i % 2 == 0:
            with col1:
                st.subheader(category)
                for skill in skills_data[category]:
                    st.markdown(f'<span class="skill-tag">{skill}</span>', 
                              unsafe_allow_html=True)
                st.markdown("")
        else:
            with col2:
                st.subheader(category)
                for skill in skills_data[category]:
                    st.markdown(f'<span class="skill-tag">{skill}</span>', 
                              unsafe_allow_html=True)
                st.markdown("")
    
    # Skill proficiency chart
    st.markdown("---")
    st.subheader("Core Competency Levels")
    
    proficiency_data = {
        'Skill': ['Transformer Architecture', 'PyTorch/Deep Learning', 'LLM Applications', 'AWS/MLOps', 'Streamlit Development', 'Research & Analysis'],
        'Proficiency': [95, 92, 88, 85, 90, 87]
    }
    
    fig = px.bar(proficiency_data, x='Proficiency', y='Skill', orientation='h',
                 title="Technical Expertise Proficiency Levels",
                 color='Proficiency', color_continuous_scale='Viridis',
                 text='Proficiency')
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    fig.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)
    
    # Research focus areas
    st.markdown("---")
    st.subheader("🔬 Research & Application Focus")
    
    focus_areas = {
        "Transformer Interpretability": "Understanding attention mechanisms and model behavior through visualization",
        "Production LLM Systems": "Deploying scalable, reliable AI applications with proper monitoring",
        "Academic AI Tools": "Building AI systems for research evaluation and academic workflows", 
        "Applied Psychology Tech": "Using NLP for mental health assessment and educational support",
        "MLOps Best Practices": "Infrastructure as Code, containerization, and automated deployment pipelines"
    }
    
    for area, description in focus_areas.items():
        st.markdown(f"**{area}:** {description}")