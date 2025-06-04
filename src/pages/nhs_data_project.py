import streamlit as st

def show():
    """Display the NHS Data project page"""
    
    # Header
    st.markdown('<h1 class="main-header">🏥 NHS Pharmacy Analytics</h1>', 
                unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #4f46e5;">AI-Powered Pharmaceutical Data Analysis</h3>', 
                unsafe_allow_html=True)
    
    # Quick links
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🚀 [Live Demo](https://nhs-data-app.streamlit.app/)**")
    with col2:
        st.markdown("**💻 [GitHub Repo](#)**")  # Add your GitHub link
    with col3:
        st.markdown("**📊 [Data Sources](#)**")  # Add data documentation link
    
    st.markdown("---")
    
    # Project overview
    st.subheader("🎯 Project Overview")
    st.markdown("""
    An **AI-powered pharmaceutical analytics application** using Anthropic Claude, Streamlit, and multiple 
    integrated pharmacy databases. This comprehensive tool enables healthcare professionals to search drugs, 
    monitor primary care usage trends, identify upcoming biosimilars, and generate AI-driven cost-effectiveness 
    reports with interactive charts and exportable visuals.
    
    The system supports **pharmacists, pharmacy technicians, and healthcare policymakers** by providing 
    actionable insights to optimize drug formularies, improve patient care, and inform cost-saving strategies at scale.
    """)
    
    # Key capabilities
    st.subheader("⭐ Key Capabilities")
    
    capabilities = [
        "**Comprehensive Drug Search** - Search across multiple open and closed-source pharmacy databases",
        "**Usage Trend Monitoring** - Track primary care prescribing patterns and identify emerging trends",
        "**Biosimilar Intelligence** - Identify upcoming biosimilar opportunities for cost optimization",
        "**AI-Driven Cost Analysis** - Generate detailed cost-effectiveness reports using advanced AI",
        "**Interactive Visualizations** - Dynamic charts and graphs for data exploration",
        "**Export Functionality** - Professional reports and visuals ready for stakeholder presentation"
    ]
    
    for capability in capabilities:
        st.markdown(f"""
        <div class="achievement-item">
            {capability}
        </div>
        """, unsafe_allow_html=True)
    
    # Technical architecture
    st.markdown("---")
    st.subheader("🔧 Technical Architecture")
    
    # Data integration
    with st.expander("**🗃️ Data Integration & Sources**"):
        st.markdown("""
        **Primary Data Sources:**
        
        - **NHS Business Services Authority**: Prescription data and cost information
        - **NICE Guidelines**: Clinical effectiveness and cost-effectiveness data
        - **BNF (British National Formulary)**: Drug classification and prescribing information
        - **MHRA Database**: Regulatory and safety information
        - **Custom APIs**: Integration with specialized pharmaceutical databases
        
        **Data Processing Pipeline:**
        
        - **Real-time Data Fetching**: Live connections to multiple data sources
        - **Data Standardization**: Consistent formatting across disparate sources
        - **Quality Validation**: Automated checks for data accuracy and completeness
        - **Caching Strategy**: Optimized performance for frequently accessed data
        """)
    
    # AI/ML components
    with st.expander("**🤖 AI/ML Components**"):
        st.markdown("""
        **Claude AI Integration:**
        
        - **Natural Language Queries**: Ask questions about drug data in plain English
        - **Intelligent Analysis**: AI-driven insights into prescribing patterns and trends
        - **Report Generation**: Automated creation of comprehensive analysis reports
        - **Cost-Effectiveness Analysis**: Advanced economic modeling with AI assistance
        
        **Advanced Analytics:**
        
        - **Trend Detection**: Automatic identification of significant pattern changes
        - **Predictive Modeling**: Forecasting future prescribing trends and costs
        - **Comparative Analysis**: Intelligent comparison between drug alternatives
        - **Risk Assessment**: AI-powered evaluation of formulary changes
        """)
    
    # User interface
    with st.expander("**💻 User Interface & Experience**"):
        st.markdown("""
        **Professional Dashboard:**
        
        - **Intuitive Search**: Smart search functionality across all data sources
        - **Interactive Charts**: Plotly-powered visualizations for data exploration
        - **Customizable Views**: Tailored interfaces for different user roles
        - **Export Options**: Professional reports in multiple formats
        
        **Workflow Optimization:**
        
        - **Quick Actions**: Streamlined access to common pharmacy tasks
        - **Saved Searches**: Bookmark frequently used queries and analyses
        - **Collaboration Tools**: Share insights and reports with team members
        - **Mobile Responsive**: Works seamlessly on tablets and mobile devices
        """)
    
    # Use cases by user type
    st.markdown("---")
    st.subheader("👥 User-Specific Applications")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Pharmacists:**
        
        - Drug formulary optimization
        - Cost-effectiveness analysis
        - Alternative therapy identification
        - Clinical decision support
        - Patient safety monitoring
        """)
    
    with col2:
        st.markdown("""
        **Pharmacy Technicians:**
        
        - Inventory management insights
        - Supply chain optimization
        - Generic substitution analysis
        - Procurement cost analysis
        - Stock level optimization
        """)
    
    with col3:
        st.markdown("""
        **Healthcare Policymakers:**
        
        - Population health analysis
        - Healthcare cost optimization
        - Policy impact assessment
        - Resource allocation planning
        - Strategic decision support
        """)
    
    # Business impact
    st.markdown("---")
    st.subheader("💡 Business Impact & Value")
    
    impact_areas = {
        "**Cost Optimization**": [
            "Identify high-impact biosimilar opportunities",
            "Optimize drug formulary selections",
            "Reduce unnecessary prescribing costs",
            "Improve procurement decision-making"
        ],
        "**Clinical Excellence**": [
            "Support evidence-based prescribing",
            "Improve patient safety monitoring",
            "Enhance clinical decision-making",
            "Identify therapeutic alternatives"
        ],
        "**Operational Efficiency**": [
            "Streamline pharmacy workflows",
            "Automate routine analysis tasks",
            "Reduce manual data compilation",
            "Accelerate report generation"
        ]
    }
    
    cols = st.columns(len(impact_areas))
    for i, (area, benefits) in enumerate(impact_areas.items()):
        with cols[i]:
            st.markdown(area)
            for benefit in benefits:
                st.markdown(f"• {benefit}")
    
    # Technology stack
    st.markdown("---")
    st.subheader("🛠️ Technology Stack")
    
    tech_categories = {
        "**AI/ML**": ["Anthropic Claude", "Natural Language Processing", "Predictive Analytics"],
        "**Data Processing**": ["Python", "Pandas", "NumPy", "APIs"],
        "**Visualization**": ["Streamlit", "Plotly", "Interactive Charts"],
        "**Development**": ["Git", "VS Code", "Jupyter", "Requirements Management"],
        "**Deployment**": ["Streamlit Cloud", "API Integration", "Cloud Storage"]
    }
    
    cols = st.columns(len(tech_categories))
    for i, (category, techs) in enumerate(tech_categories.items()):
        with cols[i]:
            st.markdown(category)
            for tech in techs:
                st.markdown(f'<span class="skill-tag">{tech}</span>', unsafe_allow_html=True)
    
    # Data compliance
    st.markdown("---")
    st.subheader("🔒 Data Governance & Compliance")
    
    st.markdown("""
    **Healthcare Data Standards:**
    - Compliance with NHS data governance requirements
    - GDPR adherence for all data processing activities
    - Secure handling of sensitive healthcare information
    
    **Quality Assurance:**
    - Validated data sources with established provenance
    - Regular data quality checks and validation processes
    - Transparent methodology for all analyses and calculations
    
    **Professional Standards:**
    - Alignment with NICE guidelines and recommendations
    - Support for evidence-based healthcare decision making
    - Maintenance of professional pharmacy practice standards
    """)
    
    # Call to action
    st.markdown("---")
    st.markdown("""
    <div class="featured-project">
        <h3>🚀 Explore NHS Pharmacy Analytics</h3>
        <p>Experience comprehensive pharmaceutical data analysis with AI-powered insights for better healthcare outcomes.</p>
        <br>
        <a href="https://nhs-data-app.streamlit.app/" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px; margin-right: 1rem;">🎮 Try Live Demo</a>
        <a href="#" target="_blank" style="color: white; text-decoration: none; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 5px;">📊 View Data Sources</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Previous: Jess"):
            st.rerun()
    with col2:
        if st.button("Back to Portfolio"):
            st.rerun()
    with col3:
        if st.button("View All Projects →"):
            st.rerun()