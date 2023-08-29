
import streamlit as st
from components import widgets

def intro():
    import streamlit as st
    st.write("# Welcome to DataWrangler! 👋")
    st.sidebar.success("Select a veesion above.")

    st.markdown(
        """
        DataWrangleer is a tool to convert GeoLab reports from ALS into a format that 
        can be used and analyzed.

        **👈 Select a version from the dropdown on the left** to see some examples
        of what DataWrangler can do!

        ### Want to learn more?

        - Documentation

        ### Want to contribute?
        - Contact me

        ### Version History
        - V.1: Initial release
        - V.2: Added comma feature
    """
    )

def convert():
    import streamlit as st
    # Site Metadata
    st.title("Upload Example V.1")
 
    # File Reader
    uploads = widgets.file_uploader()
    
    # Widgets
    col1, col2 = st.columns(2)

    # Options
    with col1:
        widgets.toggle()

    # Connvert Button
    with col2:
        if 'button' not in st.session_state:
            st.session_state.button = False
        widgets.button("Save Settings")
    
    if st.session_state.button:
        # Progress Bar
        widgets.progress_bar()

    for file in uploads:
        # File Renderer
        input = widgets.file_renderer(file)
       

        # File Processing
        output = widgets.file_processing(input)

        # Data Preview
        with st.expander('Data preview'):
            st.write(output.head(10))
                     
        # File Downloader
        widgets.file_downloader(my_large_df=output)

def convert_2():
    import streamlit as st
    # Site Metadata
    st.title("Upload Example V.2")
    st.write("Multiple File Uploader")

page_names_to_funcs = {
    "—": intro,
    "Conveert XLSX V.1": convert,
    "Conveert XLSX V2": convert_2,
}

demo_name = st.sidebar.selectbox("Choose DataWrangler Version", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()