import streamlit as st
import os
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Portfolio Projects", layout="wide")

st.title("🎯 Portfolio Projects Gallery")

# Project configuration with GitHub details
PROJECTS = {
    "k-raid": {
        "title": "K-RAID Framework",
        "description": "Agentic Kabaddi Reasoning Framework",
        "github": "kesav25155/k-raid",
        "tags": ["AI/ML", "Reasoning", "Framework"]
    },
    "campusvoice": {
        "title": "CampusVoice",
        "description": "Campus community platform",
        "github": "kesav25155/campusvoice",
        "tags": ["Web", "Community", "Platform"]
    },
    "civicconnect": {
        "title": "CivicConnect",
        "description": "Civic engagement platform",
        "github": "kesav25155/civicconnect",
        "tags": ["Web", "Civic Tech", "Social"]
    },
    "chess-platform": {
        "title": "Chess Platform",
        "description": "Online chess gaming platform",
        "github": "kesav25155/chess-platform",
        "tags": ["Gaming", "Web", "Real-time"]
    },
    "anna-university-intern": {
        "title": "Anna University Internship",
        "description": "University internship project",
        "github": "kesav25155/anna-university-intern",
        "tags": ["Education", "Project", "Internship"]
    },
    "football-injury": {
        "title": "Football Injury Analysis",
        "description": "Sports injury prediction and analysis",
        "github": "kesav25155/football-injury",
        "tags": ["Sports", "Data Science", "Analysis"]
    }
}

# Sidebar navigation
st.sidebar.title("📂 Projects")
projects_list = list(PROJECTS.keys())
selected_project = st.sidebar.selectbox("Select a project:", projects_list)

# Get the uploads path
base_path = Path(__file__).parent.parent

# Display selected project
if selected_project:
    project_data = PROJECTS[selected_project]
    project_path = base_path / selected_project

    # Project header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.header(f"📌 {project_data['title']}")
        st.write(f"*{project_data['description']}*")
    with col2:
        github_url = f"https://github.com/{project_data['github']}"
        st.markdown(f"[🔗 View on GitHub]({github_url})")

    # Tags
    st.write("**Tags:**", " | ".join([f"`{tag}`" for tag in project_data['tags']]))

    st.divider()

    # Display images if folder exists
    if project_path.exists():
        image_files = sorted([f for f in project_path.glob("*.png") + project_path.glob("*.jpg") + project_path.glob("*.jpeg")])

        if image_files:
            st.subheader(f"📸 Gallery ({len(image_files)} images)")

            # Image gallery with columns
            cols = st.columns(3)
            for idx, image_file in enumerate(image_files):
                with cols[idx % 3]:
                    try:
                        img = Image.open(image_file)
                        st.image(img, use_container_width=True)
                        with st.expander(f"View {image_file.name}"):
                            st.image(img)
                            st.caption(image_file.name)
                    except Exception as e:
                        st.error(f"Error loading {image_file.name}: {e}")
        else:
            st.info("No images found for this project.")
    else:
        st.warning(f"Project folder not found at {project_path}")

    # GitHub Stats
    st.divider()
    st.subheader("📊 Project Info")

    image_files = sorted([f for f in project_path.glob("*.png") + project_path.glob("*.jpg") + project_path.glob("*.jpeg")]) if project_path.exists() else []
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Project Folder", selected_project)
    with col2:
        st.metric("Images", len(image_files))
    with col3:
        st.metric("GitHub", project_data['github'])

# Footer
st.divider()
st.markdown("""
---
**Portfolio Streamlit App** | Built with ❤️ using Streamlit
[Visit Portfolio Website](https://kesav25155.github.io/)
""")
