import streamlit as st

def show():
    """Display the home page"""
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