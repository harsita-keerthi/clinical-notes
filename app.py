import streamlit as st  # streamlit for web application
from summarizer import summarize_text  # import summarize_text function from summarizer.py

# streamlit UI set up
st.title("Clinical Notes Summarizer")
st.write("Enter your notes below and click on 'Summarize' to get a summarized version of the text.")

# file upload
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

# input text area for notes
note = st.text_area("Or Enter Your Notes", height=200)

# summarize button
if st.button("Summarize"):
    try:
        if uploaded_file is not None:
            # read and summarize txt file
            try:
                content = uploaded_file.read().decode("utf-8")
            except UnicodeDecodeError:
                st.error("Error decoding the file. Please make sure it's a valid text file.")
                content = None

            if content:
                try:
                    summary = summarize_text(content)
                    st.subheader("Summary:")
                    st.write(summary)
                except Exception as e:
                    st.error(f"An error occurred during summarization: {e}")
        elif note.strip():
            # call summarization function
            try:
                summary = summarize_text(note)
                st.subheader("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"An error occurred during summarization: {e}")
        else:
            st.warning("Please enter some text to summarize.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
