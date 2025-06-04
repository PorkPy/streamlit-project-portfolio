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
    page_title="Your Name - AI/ML Portfolio",
    page_icon="🤖",
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
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .featured-project {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
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
    .app-preview {
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #ffffff;
    }
    .demo-button {
        background: linear-gradient(45deg, #4f46e5, #7c3aed);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin: 0.5rem;
        font-weight: bold;
    }
    .impact-metric {
        background-color: #ecfdf5;
        border-left: 4px solid #10b981;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Sidebar navigation
    st.sidebar.title("🤖 AI/ML Portfolio")
    page = st.sidebar.selectbox("Navigate to:", 
                               ["🏠 Home", "👤 About", "🚀 Projects", "🛠️ Live Apps", "💡 Skills", "📬 Contact"])
    
    if page == "🏠 Home":
        show_home()
    elif page == "👤 About":
        show_about()
    elif page == "🚀 Projects":
        show_projects()
    elif page == "🛠️ Live Apps":
        show_live_apps()
    elif page == "💡 Skills":
        show_skills()
    elif page == "📬 Contact":
        show_contact()

def show_home():
    st.markdown('<h1 class="main-header">AI/ML Engineer & Researcher</h1>', 
                unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### Hi, I'm [Your Name] 👋
        
        I'm an **AI/ML Engineer** specializing in **Large Language Models**, 
        **Transformer Architectures**, and **Production ML Systems**.
        
        From building transformers from scratch to deploying scalable AI solutions 
        on AWS, I turn cutting-edge research into practical applications.
        """)
    
    # Quick stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("AI Projects", "6+", "Production Ready")
    with col2:
        st.metric("Streamlit Apps", "5+", "Live & Interactive")
    with col3:
        st.metric("Research Areas", "NLP, Transformers", "Deep Learning")
    with col4:
        st.metric("Model Accuracy", "85%+", "Peer Review Prediction")
    
    # Featured project preview
    st.markdown("---")
    st.markdown("""
    <div class="featured-project">
        <h3>🔥 Featured: Custom Transformer from Scratch</h3>
        <p><strong>Built a complete transformer language model from PyTorch fundamentals to AWS production deployment</strong></p>
        <p>• Custom attention mechanisms & positional encoding implementation</p>
        <p>• Interactive training visualization with attention pattern analysis</p>
        <p>• Full MLOps pipeline: Docker → Lambda → API Gateway → Terraform IaC</p>
        <p>• Public inference API with auto-scaling and monitoring</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick access to live apps
    st.subheader("🚀 Explore Live Applications")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🧠 Transformer Visualizer**
        
        Interactive attention mechanism explorer
        
        [Launch App →](your-transformer-app-url)
        """)
    
    with col2:
        st.markdown("""
        **📝 Research Assistant**
        
        AI-powered paper evaluation system
        
        [Launch App →](your-research-app-url)
        """)
    
    with col3:
        st.markdown("""
        **🔬 Psycholinguistic Analyzer**
        
        Extract psychological insights from text
        
        [Launch App →](your-psycho-app-url)
        """)

def show_about():
    st.title("About Me")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.info("📷 Add your profile image here")
        
        st.markdown("### Quick Links")
        st.markdown("🔗 [LinkedIn](your-linkedin)")
        st.markdown("💻 [GitHub](your-github)")
        st.markdown("📄 [arXiv Papers](your-arxiv)")
        st.markdown("🤖 [Live Apps](your-apps)")
    
    with col2:
        st.markdown("""
        ## Background
        
        I'm an AI/ML Engineer with deep expertise in **transformer architectures**, 
        **large language models**, and **production ML systems**. My work spans from 
        implementing research papers from scratch to deploying scalable AI solutions 
        that serve real-world applications.
        
        ### Specializations
        - **Transformer Architectures** - Built from PyTorch fundamentals
        - **Large Language Models** - Fine-tuning, deployment, and evaluation
        - **MLOps & Production** - AWS serverless, containerization, IaC
        - **Research Applications** - Academic paper analysis, peer review prediction
        - **Applied NLP** - Psycholinguistic analysis, content generation
        
        ### Current Focus
        - Advancing transformer interpretability through attention visualization
        - Building production-ready LLM applications with robust evaluation frameworks
        - Developing AI tools for academic research and mental health assessment
        """)
    
    st.markdown("---")
    st.subheader("Philosophy & Approach")
    st.markdown("""
    I believe in **understanding AI systems from first principles**. Rather than just using 
    pre-built models, I implement architectures from scratch to truly understand their 
    mechanics. This deep understanding enables me to build more robust, interpretable, 
    and effective AI solutions.
    
    My projects bridge the gap between cutting-edge research and practical applications, 
    always with a focus on **transparency**, **reliability**, and **real-world impact**.
    """)

def show_projects():
    st.title("🚀 Projects Portfolio")
    
    # Project categories
    category = st.selectbox("Filter by domain:", 
                           ["All Projects", "Transformer Architecture", "LLM Applications", 
                            "Research Tools", "MLOps & Production", "Applied NLP"])
    
    # Your actual projects
    projects = [
        {
            "title": "Transformer Architecture: From-Scratch LLM Development",
            "category": "Transformer Architecture",
            "description": """Developed a fully-functional transformer language model from scratch, implementing 
            the complete architecture that powers modern AI systems. Created an interactive visualization 
            application that provides unprecedented insight into how transformers learn language patterns 
            through attention mechanisms.""",
            "tech_stack": ["PyTorch", "Streamlit", "Python", "NLP", "Deep Learning", "Attention Mechanisms", "Data Visualization"],
            "achievements": [
                "Implemented every transformer component using PyTorch from scratch",
                "Engineered complete training pipeline with adaptive learning rate scheduling",
                "Built intuitive Streamlit app visualizing attention patterns and token probabilities",
                "Demonstrated evolution of language understanding through training progression"
            ],
            "impact": "Provides hands-on platform for exploring transformer mechanics and training dynamics",
            "links": {
                "demo": "your-transformer-demo-url",
                "github": "your-transformer-github",
                "streamlit": "your-transformer-streamlit-url"
            }
        },
        {
            "title": "Custom Transformer: Research to Production Pipeline",
            "category": "MLOps & Production",
            "description": """Complete end-to-end transformer deployment showcasing MLOps best practices. 
            Built transformer from PyTorch fundamentals, deployed to AWS serverless architecture, 
            and created public-facing applications with monitoring and auto-scaling.""",
            "tech_stack": ["PyTorch", "AWS Lambda", "API Gateway", "Docker", "Terraform", "Streamlit", "MLOps"],
            "achievements": [
                "Built and trained transformer language model from scratch",
                "Deployed to AWS serverless using containerized Lambda functions",
                "Implemented Infrastructure as Code with Terraform",
                "Created both training visualization and public inference applications",
                "Demonstrated complete MLOps pipeline with monitoring and auto-scaling"
            ],
            "impact": "Showcases production-ready AI deployment with enterprise-grade infrastructure",
            "links": {
                "demo": "your-production-demo-url",
                "github": "your-production-github", 
                "api": "your-api-endpoint"
            }
        },
        {
            "title": "LLM-Based Research Assessment System",
            "category": "Research Tools",
            "description": """Cutting-edge scientific paper evaluation platform using AWS Bedrock, leveraging 
            large language models to predict peer review outcomes with ~85% accuracy. Generates detailed 
            assessments including acceptance probability, methodological analysis, and actionable recommendations.""",
            "tech_stack": ["AWS Bedrock", "Python", "LLMs", "Statistical Validation", "NLP"],
            "achievements": [
                "Achieved ~85% accuracy in peer review outcome prediction",
                "Implemented advanced self-assessment mechanisms for confidence quantification",
                "Rigorous validation on control test sets with expert human review alignment",
                "Generated detailed methodological analysis and improvement recommendations"
            ],
            "impact": "Accelerates peer review workflow and improves review quality for academic publishing",
            "links": {
                "demo": "your-research-demo-url",
                "paper": "your-research-paper-url"
            }
        },
        {
            "title": "LLM-Based Psycholinguistic Feature Extraction",
            "category": "Applied NLP",
            "description": """Advanced language model application leveraging LangChain and OpenAI APIs to extract 
            deep psychological and emotional insights from diverse text sources. Analyzes linguistic patterns 
            to identify emotional states, cognitive traits, and mental health indicators.""",
            "tech_stack": ["LangChain", "OpenAI APIs", "Python", "NLP", "Prompt Engineering"],
            "achievements": [
                "Developed sophisticated prompt engineering for psychological analysis",
                "Implemented analysis of emails and audio transcripts for mental health indicators",
                "Created early detection system for anxiety and neurodivergence markers",
                "Built scalable automated psycholinguistic analysis pipeline"
            ],
            "impact": "Enhances mental health assessments with actionable insights from unstructured communication data",
            "links": {
                "demo": "your-psycho-demo-url",
                "streamlit": "your-psycho-streamlit-url"
            }
        },
        {
            "title": "Automated arXiv Research Blog Generator",
            "category": "Research Tools",
            "description": """End-to-end automated content generation system that monitors new research papers 
            from arXiv, creates structured technical blog posts with AI-generated visuals, and distributes 
            content across social media platforms with zero-maintenance operation.""",
            "tech_stack": ["Python", "arXiv API", "AI Image Generation", "Meta Threads API", "GitHub Actions", "GitHub Pages"],
            "achievements": [
                "Built intelligent duplicate detection system",
                "Implemented scheduled execution via GitHub Actions",
                "Created AI-generated visuals for technical content",
                "Developed multi-platform content distribution pipeline"
            ],
            "impact": "Significantly reduced manual effort in academic content creation while boosting engagement",
            "links": {
                "blog": "your-blog-url",
                "github": "your-blog-github"
            }
        },
        {
            "title": "Jess – AI-Powered Educational Psychology Assistant",
            "category": "LLM Applications",
            "description": """Professional tool for Educational Psychologists built with Claude AI and Streamlit. 
            Streamlines statutory assessment process with AI-driven case consultations, automated report 
            generation, and professional document exports.""",
            "tech_stack": ["Python", "Streamlit", "LangChain", "Claude AI", "SQLite"],
            "achievements": [
                "Implemented AI-driven case consultation system",
                "Built automated multi-section report generation",
                "Created professional document export functionality",
                "Developed persistent data saving with SQLite integration"
            ],
            "impact": "Reduces report writing time while maintaining high professional standards for Educational Psychologists",
            "links": {
                "demo": "your-jess-demo-url",
                "streamlit": "your-jess-streamlit-url"
            }
        },
        {
            "title": "LLM-based Pharmacy Data Analysis Tool",
            "category": "LLM Applications", 
            "description": """AI-powered pharmaceutical analytics application using Anthropic Claude and multiple 
            pharmacy databases. Enables drug search, usage trend monitoring, biosimilar identification, 
            and AI-driven cost-effectiveness reporting.""",
            "tech_stack": ["Anthropic Claude", "Streamlit", "Python", "Pharmaceutical APIs", "Data Visualization"],
            "achievements": [
                "Integrated multiple open and closed-source pharmacy databases",
                "Built comprehensive drug search and trend monitoring system",
                "Implemented upcoming biosimilar identification features",
                "Created AI-driven cost-effectiveness reports with interactive charts"
            ],
            "impact": "Supports pharmacists and healthcare policymakers in optimizing drug formularies and patient care",
            "links": {
                "demo": "your-pharmacy-demo-url",
                "streamlit": "your-pharmacy-streamlit-url"
            }
        }
    ]
    
    # Filter projects
    if category != "All Projects":
        filtered_projects = [p for p in projects if p["category"] == category]
    else:
        filtered_projects = projects
    
    # Display projects
    for i, project in enumerate(filtered_projects):
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
                st.markdown(f"• {achievement}")
            
            # Impact
            if project.get('impact'):
                st.markdown(f"""
                <div class="impact-metric">
                    <strong>💡 Impact:</strong> {project['impact']}
                </div>
                """, unsafe_allow_html=True)
            
            # Tech stack tags
            st.markdown("**🛠️ Technologies:**")
            cols = st.columns(min(len(project['tech_stack']), 5))
            for j, tech in enumerate(project['tech_stack'][:5]):
                with cols[j % 5]:
                    st.markdown(f'<span class="skill-tag">{tech}</span>', 
                              unsafe_allow_html=True)
            
            # Additional tech tags if more than 5
            if len(project['tech_stack']) > 5:
                remaining_cols = st.columns(len(project['tech_stack']) - 5)
                for j, tech in enumerate(project['tech_stack'][5:]):
                    with remaining_cols[j]:
                        st.markdown(f'<span class="skill-tag">{tech}</span>', 
                                  unsafe_allow_html=True)
            
            # Links
            st.markdown("**🔗 Links:**")
            link_cols = st.columns(len(project['links']))
            for j, (link_type, url) in enumerate(project['links'].items()):
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
            
            st.markdown("---")

def show_live_apps():
    st.title("🛠️ Live Interactive Applications")
    
    st.markdown("""
    These are fully functional Streamlit applications that demonstrate my AI/ML work. 
    Each app provides hands-on interaction with the underlying models and systems.
    """)
    
    # App showcase
    apps = [
        {
            "title": "🧠 Transformer Architecture Visualizer",
            "description": "Interactive exploration of transformer attention mechanisms and training dynamics",
            "url": "your-transformer-viz-url",
            "features": ["Attention pattern visualization", "Token probability analysis", "Training progression tracking"],
            "tech": ["PyTorch", "Streamlit", "Plotly"]
        },
        {
            "title": "📝 Research Paper Evaluator", 
            "description": "AI-powered academic paper assessment with peer review prediction",
            "url": "your-research-eval-url",
            "features": ["85% accuracy peer review prediction", "Methodological analysis", "Improvement recommendations"],
            "tech": ["AWS Bedrock", "LLMs", "Statistical Analysis"]
        },
        {
            "title": "🔬 Psycholinguistic Text Analyzer",
            "description": "Extract psychological insights and mental health indicators from text",
            "url": "your-psycho-analyzer-url", 
            "features": ["Emotional state detection", "Cognitive trait analysis", "Mental health screening"],
            "tech": ["LangChain", "OpenAI", "Advanced Prompting"]
        },
        {
            "title": "👩‍🏫 Jess - Educational Psychology Assistant",
            "description": "Professional tool for Educational Psychologists with AI-driven assessments",
            "url": "your-jess-app-url",
            "features": ["Case consultation", "Automated reporting", "Professional exports"],
            "tech": ["Claude AI", "SQLite", "Professional UI"]
        },
        {
            "title": "💊 Pharmaceutical Analytics Dashboard",
            "description": "Comprehensive drug analysis with cost-effectiveness insights",
            "url": "your-pharma-app-url",
            "features": ["Drug trend monitoring", "Biosimilar tracking", "Cost analysis"],
            "tech": ["Multiple APIs", "Interactive Charts", "Export Features"]
        }
    ]
    
    # Display apps in a grid
    for i in range(0, len(apps), 2):
        cols = st.columns(2)
        for j, col in enumerate(cols):
            if i + j < len(apps):
                app = apps[i + j]
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

def show_skills():
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

def show_contact():
    st.title("📬 Let's Collaborate")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h3>🤝 Open to Opportunities</h3>
            <p>I'm passionate about pushing the boundaries of AI/ML and always excited to discuss:</p>
            <ul>
                <li><strong>Research Collaborations</strong> - Transformer architectures, LLM applications</li>
                <li><strong>Consulting Projects</strong> - AI strategy, model development, MLOps</li>
                <li><strong>Speaking Engagements</strong> - Technical talks on transformers and production ML</li>
                <li><strong>Open Source</strong> - Contributing to AI/ML projects and tools</li>
            </ul>
            
            <h4>📧 Get in Touch</h4>
            <p><strong>Email:</strong> your.email@example.com</p>
            <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/yourprofile">linkedin.com/in/yourprofile</a></p>
            <p><strong>GitHub:</strong> <a href="https://github.com/yourusername">github.com/yourusername</a></p>
            <p><strong>Research:</strong> <a href="https://arxiv.org/search/?query=yourname">arXiv Papers</a></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact form
        st.subheader("💬 Send a Message")
        with st.form("contact_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
            with col_b:
                company = st.text_input("Company/Organization")
                project_type = st.selectbox("Interest Area", 
                    ["Research Collaboration", "Consulting", "Speaking", "Open Source", "Other"])
            
            subject = st.text_input("Subject")
            message = st.text_area("Tell me about your project or idea", height=120)
            
            if st.form_submit_button("🚀 Send Message"):
                if name and email and message:
                    st.success("Thank you! I'll get back to you within 24 hours.")
                    st.balloons()
                else:
                    st.error("Please fill in the required fields (Name, Email, Message).")
    
    with col2:
        st.subheader("📊 Collaboration Stats")
        st.metric("Response Time", "< 24 hrs")
        st.metric("Active Projects", "3-5", "Concurrent")
        st.metric("Success Rate", "95%+", "Project Completion")
        
        st.markdown("---")
        st.subheader("🎯 Current Focus")
        st.markdown("""
        - **Transformer Interpretability Research**
        - **Production LLM Deployment**  
        - **Academic AI Tool Development**
        - **MLOps Best Practices**
        """)
        
        st.markdown("---")
        st.subheader("📄 Resources")
        if st.button("📋 Download Technical Resume"):
            st.info("Add your resume download functionality here")
        
        if st.button("📊 View Project Portfolio PDF"):
            st.info("Add portfolio PDF download here")

if __name__ == "__main__":
    main()