import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)

from parse import parse_with_ollama

st.title("AI Web Scraper")

url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping...")
    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    cleaned_body_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_body_content
    
    with st.expander("Body Content"):
        st.text_area("Body Content", cleaned_body_content, height=300)
        

if "dom_content" in st.session_state:
    parse_descriptions = st.text_area("Describe what you want to parse?")
    
    if st.button("Parse Content"):
        if parse_descriptions:
            st.write("Parsing...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_descriptions)
            st.write(result)