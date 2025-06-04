import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Your Name - Data Science Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .project-card {
        background-color: #f8fafc;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
        margin: 1rem 0;
    }
    .skill-tag {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 0.25rem;
        display: inline-block;
    }
    .contact-info {
        background-color: #f1f5f9;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page:", 
                               ["Home", "About", "Projects", "Skills", "Contact"])
    
    if page == "Home":
        show_home()
    elif page == "About":
        show_about()
    elif page == "Projects":
        show_projects()
    elif page == "Skills":
        show_skills()
    elif page == "Contact":
        show_contact()

def show_home():
    st.markdown('<h1 class="main-header">Welcome to My Data Science Portfolio</h1>', 
                unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### Hi, I'm [Your Name] 👋
        
        I'm a passionate **Data Scientist** and **Machine Learning Engineer** 
        with expertise in transforming data into actionable insights.
        
        Welcome to my portfolio where I showcase my projects, skills, and journey 
        in the world of data science.
        """)
    
    # Quick stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Projects Completed", "12+")
    with col2:
        st.metric("Years Experience", "3+")
    with col3:
        st.metric("Technologies Used", "15+")
    with col4:
        st.metric("Models Deployed", "8+")
    
    # Featured project preview
    st.markdown("---")
    st.subheader("🌟 Featured Project")
    
    with st.container():
        st.markdown("""
        <div class="project-card">
            <h4>Customer Churn Prediction Model</h4>
            <p>Built a machine learning model to predict customer churn with 94% accuracy 
            using ensemble methods and feature engineering techniques.</p>
            <p><strong>Tech Stack:</strong> Python, Scikit-learn, Pandas, XGBoost</p>
        </div>
        """, unsafe_allow_html=True)

def show_about():
    st.title("About Me")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Placeholder for profile image
        st.info("📷 Add your profile image here")
        # st.image("path_to_your_image.jpg", width=250)
    
    with col2:
        st.markdown("""
        ## Background
        
        I'm a data scientist with a passion for uncovering insights from complex datasets 
        and building machine learning solutions that drive business value.
        
        ### Education
        - **Master's in Data Science** - University Name (Year)
        - **Bachelor's in [Field]** - University Name (Year)
        
        ### Experience
        - **Data Scientist** at Company Name (2022-Present)
        - **Junior Data Analyst** at Previous Company (2021-2022)
        
        ### Interests
        - Machine Learning & AI
        - Data Visualization
        - Statistical Analysis
        - Deep Learning
        - MLOps
        """)
    
    st.markdown("---")
    st.subheader("My Journey")
    st.markdown("""
    My journey in data science began with a curiosity about how data can tell stories 
    and drive decisions. Over the years, I've worked on various projects ranging from 
    predictive modeling to natural language processing, always focusing on delivering 
    practical solutions to real-world problems.
    """)

def show_projects():
    st.title("My Projects")
    
    # Project categories
    category = st.selectbox("Filter by category:", 
                           ["All", "Machine Learning", "Data Analysis", "Deep Learning", "NLP"])
    
    # Sample projects - replace with your actual projects
    projects = [
        {
            "title": "Customer Churn Prediction",
            "category": "Machine Learning",
            "description": "Developed a machine learning model to predict customer churn using ensemble methods.",
            "tech_stack": ["Python", "Scikit-learn", "Pandas", "XGBoost", "Streamlit"],
            "results": "Achieved 94% accuracy with significant business impact",
            "github": "https://github.com/yourusername/project1",
            "demo": "https://your-demo-link.com"
        },
        {
            "title": "Sales Forecasting Dashboard",
            "category": "Data Analysis",
            "description": "Built an interactive dashboard for sales forecasting using time series analysis.",
            "tech_stack": ["Python", "Plotly", "Prophet", "Streamlit", "SQL"],
            "results": "Improved forecast accuracy by 23%",
            "github": "https://github.com/yourusername/project2",
            "demo": "https://your-demo-link.com"
        },
        {
            "title": "Sentiment Analysis API",
            "category": "NLP",
            "description": "Created a REST API for real-time sentiment analysis of social media posts.",
            "tech_stack": ["Python", "NLTK", "Flask", "Docker", "AWS"],
            "results": "Processing 1000+ requests per minute",
            "github": "https://github.com/yourusername/project3",
            "demo": "https://your-api-demo.com"
        },
        {
            "title": "Computer Vision Object Detection",
            "category": "Deep Learning",
            "description": "Implemented YOLO algorithm for real-time object detection in video streams.",
            "tech_stack": ["Python", "PyTorch", "OpenCV", "YOLO", "Flask"],
            "results": "Achieved 89% mAP on custom dataset",
            "github": "https://github.com/yourusername/project4",
            "demo": "https://your-demo-link.com"
        }
    ]
    
    # Filter projects
    if category != "All":
        filtered_projects = [p for p in projects if p["category"] == category]
    else:
        filtered_projects = projects
    
    # Display projects
    for project in filtered_projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <p><strong>Category:</strong> {project['category']}</p>
                <p>{project['description']}</p>
                <p><strong>Results:</strong> {project['results']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Tech stack tags
            st.markdown("**Tech Stack:**")
            cols = st.columns(len(project['tech_stack']))
            for i, tech in enumerate(project['tech_stack']):
                with cols[i]:
                    st.markdown(f'<span class="skill-tag">{tech}</span>', 
                              unsafe_allow_html=True)
            
            # Links
            col1, col2, col3 = st.columns([1, 1, 4])
            with col1:
                st.markdown(f"[GitHub]({project['github']})")
            with col2:
                st.markdown(f"[Live Demo]({project['demo']})")
            
            st.markdown("---")

def show_skills():
    st.title("Skills & Technologies")
    
    # Skills data
    skills_data = {
        "Programming Languages": ["Python", "R", "SQL", "JavaScript", "Java"],
        "Machine Learning": ["Scikit-learn", "XGBoost", "Random Forest", "SVM", "Clustering"],
        "Deep Learning": ["TensorFlow", "PyTorch", "Keras", "CNN", "RNN"],
        "Data Visualization": ["Matplotlib", "Seaborn", "Plotly", "Tableau", "D3.js"],
        "Big Data": ["Apache Spark", "Hadoop", "Kafka", "Airflow"],
        "Cloud Platforms": ["AWS", "Google Cloud", "Azure", "Docker", "Kubernetes"],
        "Databases": ["PostgreSQL", "MongoDB", "Redis", "Snowflake"],
        "Tools": ["Git", "Jupyter", "VS Code", "Linux", "Streamlit"]
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
    st.subheader("Proficiency Levels")
    
    proficiency_data = {
        'Skill': ['Python', 'Machine Learning', 'Data Visualization', 'SQL', 'Deep Learning', 'Statistics'],
        'Proficiency': [95, 90, 85, 88, 75, 82]
    }
    
    fig = px.bar(proficiency_data, x='Proficiency', y='Skill', orientation='h',
                 title="Technical Skills Proficiency",
                 color='Proficiency', color_continuous_scale='Blues')
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def show_contact():
    st.title("Get In Touch")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>Let's Connect!</h3>
            <p>I'm always interested in discussing new opportunities, 
            collaborations, or just chatting about data science.</p>
            
            <p><strong>📧 Email:</strong> your.email@example.com</p>
            <p><strong>💼 LinkedIn:</strong> <a href="https://linkedin.com/in/yourprofile">linkedin.com/in/yourprofile</a></p>
            <p><strong>🐙 GitHub:</strong> <a href="https://github.com/yourusername">github.com/yourusername</a></p>
            <p><strong>📊 Kaggle:</strong> <a href="https://kaggle.com/yourusername">kaggle.com/yourusername</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact form
        st.subheader("Send me a message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            
            if st.form_submit_button("Send Message"):
                if name and email and message:
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("Please fill in all required fields.")
    
    with col2:
        st.subheader("Quick Stats")
        st.metric("Response Time", "< 24 hours")
        st.metric("Projects Available", "Open to discuss")
        st.metric("Collaboration", "Always interested")
        
        st.markdown("---")
        st.subheader("Download Resume")
        
        # Placeholder for resume download
        if st.button("📄 Download CV/Resume"):
            st.info("Add your resume file here and implement download functionality")

if __name__ == "__main__":
    main()