
import streamlit as st
from summarizer import summarize_text

# streamlit UI set up
st.title("Clinical Notes Summarizer")
st.write("Enter your notes below and click on 'Summarize' to get a summarized version of the text.")

# file upload
uploaded_file = st.file_uploader("Choose a text file", type =["txt"])

# input text area for notes
note = st.text_area("Or Enter Your Notes", height=200)

# summarize button
if st.button("Summarize"):
    if uploaded_file is not None:
        # read and summarize txt file
        content = uploaded_file.read().decode("utf-8")
        summary = summarize_text(content)
        st.subheader("Summary:")
        st.write(summary)
    elif note.strip():
        # call summarization function
        summary = summarize_text(note)
        st.subheader("Summary: ")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")

