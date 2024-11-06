import streamlit as st
import os
from profilers.linkml import LinkMLProfiler
from profilers.ydata import YDataProfiler
from profilers.whiterabbit import WhiteRabbitProfiler, download_white_rabbit, WHITE_RABBIT_PATH
import streamlit.components.v1 as components  # for displaying HTML content

# Ensure that the directory exists
temp_dir = "tempDir"
os.makedirs(temp_dir, exist_ok=True)

# Placeholder transformation functions
def transform_linkml(file_content):
    # Implement your transformation logic here
    return "LinkML transformation result"

def transform_whiterabbit(file_content):
    # Implement your transformation logic here
    return "WhiteRabbit transformation result"

def transform_ydata(file_content):
    # Implement your transformation logic here
    return "YData transformation result"

# Function to save the transformed string as a file and provide a download link
def save_and_download(transformed_content, filename, mode, new_ext=None):
    base, ext = os.path.splitext(filename)
    download_filename = f"{base}_{mode.lower()}.{new_ext or ext}"
    st.download_button(
        label="Download transformed file",
        data=transformed_content,
        file_name=download_filename,
        mime="text/plain"  # adjust mime type according to file type
    )

# Streamlit app structure
st.title("Data profiler")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=['txt', 'csv', 'json', 'tsv'])  # Adjust the file types as needed

# Transformation mode selector
transformation_mode = st.selectbox(
    "Choose the transformation mode",
    ("LinkML", "WhiteRabbit", "Ydata")
)

# Generate transformation on button click
if uploaded_file is not None:
    if st.button("Generate Transformation"):
        # Read file content
        # file_content = uploaded_file.read().decode("utf-8")

        # Call the corresponding transformation function
        if transformation_mode == "LinkML":
            profiler = LinkMLProfiler(uploaded_file)
            transformed_content = profiler.profile()

        elif transformation_mode == "WhiteRabbit":
            if not os.path.exists(WHITE_RABBIT_PATH):
                st.write("Downloading WhiteRabbit...")
                download_white_rabbit()
                st.write("WhiteRabbit downloaded and ready.")
            profiler = WhiteRabbitProfiler(uploaded_file)
            transformed_content = transform_whiterabbit(uploaded_file)
        elif transformation_mode == "Ydata":

            profiler = YDataProfiler(uploaded_file)
            transformed_content = profiler.profile()


            # Embed HTML directly in the Streamlit app using an iframe
            components.html(transformed_content, height=600, scrolling=True)            

        # Allow the user to download the transformed file
        save_and_download(transformed_content, uploaded_file.name, transformation_mode, new_ext='html')
