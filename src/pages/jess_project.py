import streamlit as st

def show():
    """Display the Jess project page"""
    
    # Header
    st.markdown('<h1 class="main-header">👩‍🏫 Jess - AI Psychology Assistant</h1>', 
                unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #4f46e5;">Professional Tool for Educational Psychologists</h3>', 
                unsafe_allow_html=True)
    
    # Quick links
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🚀 [Live Demo](https://jess-ai3.streamlit.app/)**")
    with col2:
        st.markdown("**💻 [GitHub Repo](#)**")  # Add your GitHub link
    with col3:
        st.markdown("**📄 [Documentation](#)**")  # Add documentation link if available
    
    st.markdown("---")
    
    # Project overview
    st.subheader("🎯 Project Overview")
    st.markdown("""
    Jess is a **professional-grade AI assistant** designed specifically for Educational Psychologists to 
    streamline the statutory assessment process. Built with Python, Streamlit, LangChain, Claude AI, and SQLite, 
    this tool provides AI-driven case consultations, automated multi-section report generation, and 
    professional document exports with persistent data saving.
    
    The system is designed for **efficiency and accuracy**, reducing report writing time while supporting 
    collaboration and maintaining high professional standards required in educational psychology practice.
    """)
    
    # Key features
    st.subheader("⭐ Key Features")
    
    features = [
        "**AI-Driven Case Consultations**: Intelligent analysis and recommendations for complex educational psychology cases",
        "**Automated Report Generation**: Multi-section reports that meet statutory assessment requirements",
        "**Professional Document Exports**: Clean, professional formatting suitable for official use",
        "**Persistent Data Storage**: SQLite integration ensures secure data retention across sessions",
        "**Collaborative Workflow**: Designed to support team-based assessment processes",
        "**User-Friendly Interface**: Intuitive Streamlit interface designed for professional use"
    ]
    
    for feature in features:
        st.markdown(f"""
        <div class="achievement-item">
            {feature}
        </div>
        """, unsafe_allow_html=True)
    
    # Technical implementation
    st.markdown("---")
    st.subheader("🔧 Technical Implementation")
    
    # Architecture details
    with st.expander("**🏗️ System Architecture**"):
        st.markdown("""
        **AI/ML Components:**
        
        - **Claude AI Integration**: Leverages Anthropic's Claude for intelligent case analysis and report generation
        - **LangChain Framework**: Orchestrates complex AI workflows and prompt engineering
        - **Natural Language Processing**: Advanced text analysis for psychological assessment insights
        - **Prompt Engineering**: Carefully crafted prompts for professional psychology contexts
        
        **Data Management:**
        
        - **SQLite Database**: Lightweight, reliable database for case data and user sessions
        - **Data Persistence**: Secure storage of assessment data across multiple sessions
        - **Data Privacy**: Local storage ensures sensitive information remains secure
        - **Backup & Recovery**: Robust data management for professional reliability
        """)
    
    # User interface
    with st.expander("**💻 User Interface Design**"):
        st.markdown("""
        **Professional Design:**
        
        - **Clean Layout**: Streamlit interface optimized for professional use
        - **Intuitive Navigation**: Easy-to-use workflow for busy professionals
        - **Responsive Design**: Works seamlessly across different devices
        - **Accessibility**: Designed with accessibility standards in mind
        
        **Workflow Optimization:**
        
        - **Step-by-Step Process**: Guided workflow for systematic assessments
        - **Auto-Save Functionality**: Prevents data loss during long assessment sessions
        - **Quick Actions**: Streamlined common tasks for efficiency
        - **Export Options**: Multiple format options for different professional needs
        """)
    
    # Professional impact
    with st.expander("**👥 Professional Impact**"):
        st.markdown("""
        **Efficiency Improvements:**
        
        - **Time Reduction**: Significantly reduces time spent on report writing
        - **Consistency**: Ensures consistent quality across all assessments
        - **Accuracy**: AI assistance helps identify key assessment points
        - **Compliance**: Maintains adherence to statutory requirements
        
        **Quality Enhancement:**
        
        - **Comprehensive Analysis**: AI helps identify patterns and insights
        - **Professional Standards**: Maintains high professional documentation standards
        - **Evidence-Based**: Supports evidence-based practice in educational psychology
        - **Collaboration**: Facilitates team-based assessment approaches
        """)
    
    # Use cases
    st.markdown("---")
    st.subheader("🎯 Primary Use Cases")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Statutory Assessments:**
        
        - Education, Health and Care Plan (EHCP) assessments
        - Special Educational Needs (SEN) evaluations
        - Annual review documentation
        - Transition planning reports
        """)
    
    with col2:
        st.markdown("""
        **Professional Support:**
        
        - Case consultation and analysis
        - Report writing assistance
        - Documentation standardization
        - Collaborative assessment planning
        """)
    
    # Technology stack
    st.markdown("---")
    st.subheader("🛠️ Technology Stack")
    
    tech_categories = {
        "**AI/ML Framework**": ["Claude AI", "LangChain", "Anthropic API"],
        "**Backend**": ["Python", "SQLite", "Pandas"],
        "**Frontend**": ["Streamlit", "HTML/CSS", "JavaScript"],
        "**Development**": ["Git", "VS Code", "Jupyter"],
        "**Deployment**": ["Streamlit Cloud", "Requirements Management"]
    }
    
    cols = st.columns(len(tech_categories))
    for i, (category, techs) in enumerate(tech_categories.items()):
        with cols[i]:
            st.markdown(category)
            for tech in techs:
                st.markdown(f'<span class="skill-tag">{tech}</span>', unsafe_allow_html=True)
    
    # Professional considerations
    st.markdown("---")
    st.subheader("🔒 Professional & Ethical Considerations")
    
    st.markdown("""
    **Data Privacy & Security:**
    - Local data storage to protect sensitive information
    - Compliance with GDPR and professional guidelines
    - Secure handling of confidential case information
    
    **Professional Standards:**
    - Maintains Educational Psychology professional standards
    - Supports evidence-based practice requirements
    - Enables compliance with statutory assessment guidelines
    
    **Ethical AI Use:**
    - AI assistance supplements, never replaces, professional judgment
    - Transparent AI decision-making processes
    - Maintains professional accountability in all assessments
    """)
    
    # Call to action
    st.markdown("---")
    st.markdown("""
    <div class="featured-project">
        <h3>🚀 Experience Jess</h3>
        <p>See how AI can enhance professional Educational Psychology practice while maintaining the highest standards.</p>
        <br>
        <a href="https://jess-ai3.streamlit.app/" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px; margin-right: 1rem;">🎮 Try Live Demo</a>
        <a href="#" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px;">💻 View Documentation</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Previous: DIY LLM"):
            st.rerun()
    with col2:
        if st.button("Back to Portfolio"):
            st.rerun()
    with col3:
        if st.button("Next: NHS Data →"):
            st.rerun()