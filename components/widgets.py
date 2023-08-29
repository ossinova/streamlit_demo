import streamlit as st
import pandas as pd
import openpyxl

def button(text: str):
    def click_button():
        st.session_state.button = not st.session_state.button
    st.button(text, help='This will save your settings for the current session', on_click=click_button)

def toggle():
    color_on = st.toggle('Activate color feature')
    comma_on = st.toggle('Activate comma feature')

    if color_on:
        st.write('Color feature activated!')
    if comma_on:
        st.write('Comma feature activated!')

def file_uploader():
    # File Reader
    uploaded_files = st.file_uploader("Choose a CSV file", type="xlsx", accept_multiple_files=True)
    return uploaded_files

def file_renderer(uploaded_files):
    uploaded_files.seek(0)
    st.write("Input filename:", uploaded_files.name)
    uploaded_data_read = pd.read_excel(uploaded_files, engine='openpyxl')
    st.write(uploaded_data_read)
    return uploaded_data_read

def progress_bar():
    # Progress Bar
    import time
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

def file_processing(uploaded_files):
    # File Processing
    st.write("Processing...")
    upload_processed = uploaded_files
    st.write(upload_processed)

def file_downloader(my_large_df):
    # Download Button
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_excel().encode('utf-8')

    csv = convert_df(my_large_df)

    st.download_button(
        label="Download data as XLSX",
        data=csv,
        file_name='large_df.XLSX',
        mime='text/xlsx',
    )