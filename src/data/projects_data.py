"""
Project data definitions for the portfolio
"""

PROJECTS = [
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

LIVE_APPS = [
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

PROJECT_CATEGORIES = [
    "All Projects", 
    "Transformer Architecture", 
    "LLM Applications", 
    "Research Tools", 
    "MLOps & Production", 
    "Applied NLP"
]