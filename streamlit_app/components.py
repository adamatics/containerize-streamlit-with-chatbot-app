import os
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from utils import load_mock_data, load_readme

def sidebar():
    st.sidebar.title("Project Manager")
    st.sidebar.markdown("Manage your projects efficiently with this app.")

    st.sidebar.subheader("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "Analytics", "Settings", "Documentation", "ChatBot"])
    st.sidebar.info("Use the navigation to switch between pages.")
    
    if st.sidebar.button("ChatBot"):
        page = "ChatBot"
    
    return page

def main_content(page):
    if page == "Home":
        display_home()
    elif page == "Analytics":
        display_analytics()
    elif page == "Settings":
        display_settings()
    elif page == "Documentation":
        display_documentation()
    elif page == "ChatBot":
        embed_script()

def display_home():
    st.title("Welcome to the Project Manager App")
    st.markdown("This app helps you manage your projects with various features like analytics and settings.")
    
    st.header("Project Overview")
    st.write("Add your project overview content here.")
    
    data = load_mock_data()
    st.dataframe(data)

def display_analytics():
    st.title("Analytics")
    st.markdown("Visualize your project data with these charts.")
    
    data = load_mock_data()
    st.line_chart(data.set_index('Date')[['Metric A', 'Metric B']])
    st.bar_chart(data.set_index('Date')[['Metric C']])

def display_settings():
    st.title("Settings")
    st.markdown("Configure your project settings here.")
    
    st.subheader("Project Configuration")
    project_name = st.text_input("Project Name", "My Project")
    st.write(f"Current Project Name: {project_name}")
    
    st.subheader("Data Settings")
    st.file_uploader("Upload Project Data", type=["csv", "xlsx"])

def display_documentation():
    st.title("Documentation")
    st.markdown("Below is the README.md content of the project.")
    
    readme_content = load_readme()
    st.markdown(readme_content)

def embed_script():
    button = """
    <body>
    <script
        data-embed-id="62c05f50-ccdc-445a-9a26-f1da6197a726"
        data-base-api-url="https://{your-adalab-installation.com}/apps/anything-llm/api/embed"
        data-chat-icon="support"
        data-no-sponsor="cheap"
        data-assistant-name="DHItto"
        data-window-height="95%"
        data-window-width="95%"
        data-position="top-right"
        data-greeting="Welcome! How can I help you today?"
        data-open-on-load=True
        data-support-email="support@adamatics.com"
        data-button-color="#194D33"
        data-user-bg-color="#194D33"
        data-assistant-bg-color="#E8C3E7"
        src="https://{your-adalab-installation.com}/apps/anything-llm/embed/anythingllm-chat-widget.min.js">
    </script>
    </body>
    """
    height = 800
    components.html(button, height=height)