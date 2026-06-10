import streamlit as st
import pdfplumber
from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Load environment variables
load_dotenv()

# Azure credentials
endpoint = os.getenv("AZURE_AI_ENDPOINT")
key = os.getenv("AZURE_AI_KEY")

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

st.title("🏥 Medical Report Summarizer")

uploaded_file = st.file_uploader(
    "Upload Medical Report PDF",
    type=["pdf"]
)

if uploaded_file:

    # Extract text from PDF
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    st.subheader("📄 Extracted Report")
    st.text_area("Report Content", text, height=250)

    # Azure Entity Extraction
    documents = [text[:5000]]

    try:
        response = client.recognize_entities(documents)

        entities = []

        for doc in response:
            for entity in doc.entities:
                entities.append(
                    f"• {entity.text} ({entity.category})"
                )

        st.subheader("🩺 Extracted Medical Information")

        if entities:
            st.text_area(
                "Entities",
                "\n".join(entities),
                height=250
            )
        else:
            st.warning("No entities found.")

    except Exception as e:
        st.error(f"Error: {e}")