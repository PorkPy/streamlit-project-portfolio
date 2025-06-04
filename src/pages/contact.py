import streamlit as st

def show():
    """Display the contact page"""
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
            <p><strong>LinkedIn:</strong> <a href="#">linkedin.com/in/yourprofile</a></p>
            <p><strong>GitHub:</strong> <a href="#">github.com/yourusername</a></p>
            <p><strong>Research:</strong> <a href="#">arXiv Papers</a></p>
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