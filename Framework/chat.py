import streamlit as st
import PyPDF2
import openai

# Set your OpenAI API key here
openai.api_key = "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"

# Streamlit app header
st.title("Ask PDF")

# File upload
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # PDF to text conversion
    with st.spinner("Extracting text from PDF..."):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        pdf_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

    st.success("Text extracted from PDF.")

    # Text input
    user_input = st.text_input("Ask a question based on the PDF content:")

    if st.button("Get Answer"):
        if user_input:
            # Prepare the question for the LangChain LLM
            question = f"Document: {pdf_text}\nQuestion: {user_input}\nAnswer:"

            # Use the LangChain LLM to answer the question
            with st.spinner("Generating answer..."):
                response = openai.Completion.create(
                    engine="text-davinci-002",  # Use the LangChain LLM engine
                    prompt=question,
                    max_tokens=100,
                    n=1,
                    stop=None,
                    temperature=0.7,
                )

            answer = response.choices[0].text.strip()
            st.write("Answer:")
            st.write(answer)
        else:
            st.warning("Please enter a question.")

# Display a link to the OpenAI API documentation
# st.markdown("[OpenAI API Documentation](https://platform.openai.com/docs/api-reference/completions/create)")
