import streamlit as st
import pdfplumber

# Define the function first
def generate_mcq_from_pdf(file):
    questions = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.splitlines()
                for line in lines:
                    if line.strip():  # Only consider non-empty lines
                        questions.append(line.strip())  # Replace with actual question extraction logic
    return questions

# Title of the web app
st.title("MCQ Generator from PDF")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file is not None:
    # Process the PDF file
    questions = generate_mcq_from_pdf(uploaded_file)
    
    # Display the generated MCQs
    if questions:
        st.header("Generated MCQs")
        for idx, question in enumerate(questions, start=1):
            st.write(f"{idx}. {question}")
