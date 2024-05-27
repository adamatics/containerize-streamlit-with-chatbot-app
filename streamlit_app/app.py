import streamlit as st
from components import sidebar, main_content

st.set_page_config(page_title="Project Manager", layout="wide")


def main():
    page = sidebar()
    main_content(page)

if __name__ == "__main__":
    main()
