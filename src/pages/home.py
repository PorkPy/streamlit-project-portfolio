import streamlit as st

def show():
    """Display the home page"""
    st.markdown('<h1 class="main-header">Dom McKean</h1>', 
                unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #4f46e5; margin-bottom: 2rem;">AI/ML Engineer & Data Scientist</h2>', 
                unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### Transforming Data into Actionable Intelligence 🧠
        
        Data Science professional who specializes in **transforming raw data into actionable intelligence**. 
        I excel at extracting meaningful signals from noisy datasets, identifying critical information gaps, 
        and designing targeted approaches to complete the intelligence picture. 
        
        My background spanning **engineering, robotics, and control systems** enhances my naturally distinctive 
        analytical approach, allowing me to distinguish between data volume and information value. This enables 
        me to build solutions that capture essential insights rather than simply processing available datasets, 
        resulting in **AI systems that deliver genuine business intelligence** even in complex, unpredictable environments.
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
        <h3>🔥 Featured: DIY Transformer Language Model</h3>
        <p><strong>Built a complete transformer architecture from scratch using PyTorch fundamentals</strong></p>
        <p>• Custom attention mechanisms, positional encoding, and training pipeline implementation</p>
        <p>• Interactive Streamlit visualization showing attention patterns and model behavior</p>
        <p>• Full MLOps deployment to AWS with serverless architecture</p>
        <p>• Demonstrates deep understanding of transformer mechanics from first principles</p>
        <br>
        <a href="https://diy-llm.streamlit.app/" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px;">🚀 Explore Live App</a>
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