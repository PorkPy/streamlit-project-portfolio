import streamlit as st

def show():
    """Display the about page"""
    st.title("About Me")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.info("📷 Add your profile image here")
        
        st.markdown("### Quick Links")
        st.markdown("🔗 [LinkedIn](#)")
        st.markdown("💻 [GitHub](#)")
        st.markdown("📄 [arXiv Papers](#)")
        st.markdown("🤖 [Live Apps](#)")
    
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