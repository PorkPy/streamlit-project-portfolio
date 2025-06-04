import streamlit as st

def show():
    """Display the DIY LLM project page"""
    
    # Header
    st.markdown('<h1 class="main-header">🧠 DIY Transformer Language Model</h1>', 
                unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #4f46e5;">From-Scratch Implementation & AWS Deployment</h3>', 
                unsafe_allow_html=True)
    
    # Quick links
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🚀 [Live Demo](https://diy-llm.streamlit.app/)**")
    with col2:
        st.markdown("**💻 [GitHub Repo](#)**")  # Add your GitHub link
    with col3:
        st.markdown("**🔌 [API Endpoint](#)**")  # Add your API link if available
    
    st.markdown("---")
    
    # Project overview
    st.subheader("🎯 Project Overview")
    st.markdown("""
    This project demonstrates a **complete understanding of transformer architecture** by implementing 
    every component from scratch using PyTorch fundamentals. Rather than using pre-built libraries, 
    I built the entire system to truly understand the mechanics that power modern AI systems.
    
    The project showcases the full journey from **research implementation to production deployment**, 
    including interactive visualizations that provide unprecedented insight into how transformers 
    learn language patterns through attention mechanisms.
    """)
    
    # Key achievements
    st.subheader("🏆 Key Achievements")
    
    achievements = [
        "**From-Scratch Implementation** - Built every transformer component using pure PyTorch - self-attention, positional encoding, feed-forward networks",
        "**Training Pipeline** - Engineered complete training infrastructure with adaptive learning rate scheduling, checkpointing, and evaluation metrics",
        "**Interactive Visualization** - Created intuitive Streamlit app that visualizes attention patterns, token probabilities, and training progression",
        "**Production Deployment** - Full MLOps pipeline deployed to AWS with serverless architecture using Lambda, API Gateway, and Terraform IaC",
        "**Educational Value** - Demonstrates the evolution of language understanding as the model progresses through training"
    ]
    
    for achievement in achievements:
        st.markdown(f"""
        <div class="achievement-item">
            {achievement}
        </div>
        """, unsafe_allow_html=True)
    
    # Technical deep dive
    st.markdown("---")
    st.subheader("🔧 Technical Deep Dive")
    
    # Architecture details
    with st.expander("**🏗️ Architecture Implementation**"):
        st.markdown("""
        **Core Components Built from Scratch:**
        
        - **Multi-Head Self-Attention**: Implemented the core attention mechanism with query, key, value projections
        - **Positional Encoding**: Created sinusoidal position embeddings to give the model spatial awareness
        - **Feed-Forward Networks**: Built the position-wise fully connected layers with ReLU activation
        - **Layer Normalization**: Implemented residual connections and normalization for stable training
        - **Transformer Blocks**: Assembled complete encoder/decoder blocks with proper residual connections
        
        **Training Infrastructure:**
        
        - **Adaptive Learning Rate**: Implemented warm-up and decay scheduling for optimal convergence
        - **Checkpointing System**: Built robust save/restore functionality for long training runs
        - **Evaluation Metrics**: Created comprehensive metrics for tracking loss, perplexity, and generation quality
        - **Data Pipeline**: Efficient tokenization and batching for training data
        """)
    
    # Visualization features
    with st.expander("**📊 Interactive Visualization Features**"):
        st.markdown("""
        **Attention Pattern Analysis:**
        
        - **Heat Maps**: Visual representation of which tokens the model attends to during processing
        - **Multi-Head Visualization**: See how different attention heads focus on different linguistic patterns
        - **Layer-by-Layer Analysis**: Track how attention patterns evolve through transformer layers
        
        **Training Progression:**
        
        - **Real-time Metrics**: Live updates of loss, learning rate, and other training statistics
        - **Generation Examples**: See how the model's text generation improves over time
        - **Token Probability Tracking**: Understand the model's confidence in its predictions
        
        **Interactive Elements:**
        
        - **Custom Text Input**: Test the model on your own text and see attention patterns
        - **Parameter Exploration**: Adjust temperature and other generation parameters
        - **Model Comparison**: Compare different checkpoints to see learning progression
        """)
    
    # MLOps implementation
    with st.expander("**☁️ MLOps & Production Deployment**"):
        st.markdown("""
        **AWS Serverless Architecture:**
        
        - **Containerized Lambda**: Model inference packaged in Docker containers for serverless deployment
        - **API Gateway**: RESTful API endpoints for model interaction with proper authentication
        - **S3 Storage**: Model weights and training artifacts stored in scalable cloud storage
        - **CloudWatch Monitoring**: Real-time monitoring of inference requests and performance
        
        **Infrastructure as Code:**
        
        - **Terraform Configuration**: Complete infrastructure defined as code for reproducible deployments
        - **Automated Deployment**: CI/CD pipeline for seamless updates and rollbacks
        - **Auto-scaling**: Serverless architecture automatically scales with demand
        - **Cost Optimization**: Pay-per-request model minimizes infrastructure costs
        
        **Development Workflow:**
        
        - **Local Development**: Full training and testing environment for rapid iteration
        - **Version Control**: Git-based workflow with proper branching and merging strategies
        - **Experiment Tracking**: Systematic tracking of model experiments and hyperparameters
        """)
    
    # Business impact & learnings
    st.markdown("---")
    st.subheader("💡 Impact & Key Learnings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Technical Impact:**
        
        - **Deep Understanding**: Building from scratch provides intuitive understanding of transformer mechanics
        - **Debugging Skills**: First-principles knowledge enables effective troubleshooting of complex models
        - **Architecture Insights**: Understanding attention patterns helps optimize model performance
        - **Production Experience**: Full deployment pipeline demonstrates MLOps best practices
        """)
    
    with col2:
        st.markdown("""
        **Key Learnings:**
        
        - **Attention is Everything**: Seeing how attention mechanisms actually work reinforces their importance
        - **Training Dynamics**: Understanding how transformers learn language patterns over time
        - **Optimization Challenges**: Experience with learning rate scheduling and gradient dynamics
        - **Scalability Considerations**: Lessons learned about deploying ML models at scale
        """)
    
    # Technology stack
    st.markdown("---")
    st.subheader("🛠️ Technology Stack")
    
    tech_categories = {
        "**Core ML Framework**": ["PyTorch", "NumPy", "Pandas"],
        "**Visualization**": ["Streamlit", "Plotly", "Matplotlib", "Seaborn"],
        "**Cloud Infrastructure**": ["AWS Lambda", "API Gateway", "S3", "CloudWatch"],
        "**DevOps**": ["Docker", "Terraform", "Git", "GitHub Actions"],
        "**Development**": ["Python", "Jupyter", "VS Code", "Linux"]
    }
    
    cols = st.columns(len(tech_categories))
    for i, (category, techs) in enumerate(tech_categories.items()):
        with cols[i]:
            st.markdown(category)
            for tech in techs:
                st.markdown(f'<span class="skill-tag">{tech}</span>', unsafe_allow_html=True)
    
    # Call to action
    st.markdown("---")
    st.markdown("""
    <div class="featured-project">
        <h3>🚀 Explore the Project</h3>
        <p>Experience the interactive transformer visualization and see how attention mechanisms work in real-time.</p>
        <br>
        <a href="https://diy-llm.streamlit.app/" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px; margin-right: 1rem;">🎮 Try Live Demo</a>
        <a href="#" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px;">💻 View Source Code</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Portfolio"):
            st.rerun()
    with col3:
        if st.button("Next Project: Jess →"):
            st.rerun()