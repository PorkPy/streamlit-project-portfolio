portfolio/
├── main.py                          # Main application entry point
├── requirements.txt                 # Dependencies
├── README.md                        # Setup and deployment instructions
├── .gitignore                       # Git ignore file
├── config/
│   ├── __init__.py
│   └── settings.py                  # App configuration settings
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── projects_data.py         # Project definitions
│   │   ├── skills_data.py           # Skills and proficiency data
│   │   └── apps_data.py             # Live apps configuration
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── home.py                  # Home page
│   │   ├── about.py                 # About page
│   │   ├── projects.py              # Projects showcase
│   │   ├── live_apps.py             # Live apps gallery
│   │   ├── skills.py                # Skills and expertise
│   │   └── contact.py               # Contact information
│   ├── components/
│   │   ├── __init__.py
│   │   ├── project_card.py          # Reusable project card component
│   │   ├── skill_tags.py            # Skill tag components
│   │   ├── metrics.py               # Metric display components
│   │   └── navigation.py            # Navigation components
│   └── utils/
│       ├── __init__.py
│       ├── styling.py               # CSS management
│       ├── helpers.py               # Utility functions
│       └── constants.py             # App constants
├── assets/
│   ├── images/
│   │   ├── profile.jpg              # Profile image
│   │   └── project_screenshots/     # Project preview images
│   ├── documents/
│   │   ├── resume.pdf               # Downloadable resume
│   │   └── portfolio.pdf            # Portfolio summary
│   └── icons/
│       └── favicon.ico              # App favicon
└── tests/
    ├── __init__.py
    ├── test_pages.py                # Page tests
    ├── test_components.py           # Component tests
    └── test_data.py                 # Data validation tests