import streamlit as st

def load_css():
    """Load custom CSS styling for the portfolio"""
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
        .section-header {
            font-size: 2rem;
            color: #1e40af;
            margin-bottom: 1rem;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }
        .metric-container {
            background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin: 0.5rem 0;
        }
        .achievement-item {
            background-color: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 0.75rem;
            margin: 0.5rem 0;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)