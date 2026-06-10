from dotenv import load_dotenv
import os

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

load_dotenv()

endpoint = os.getenv("AZURE_AI_ENDPOINT")
key = os.getenv("AZURE_AI_KEY")

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

documents = [
    """
    Patient diagnosed with Type 2 Diabetes and Hypertension.
    Prescribed Metformin and Amlodipine.
    Follow-up after 3 months.
    """
]

response = client.recognize_entities(documents)

for doc in response:
    for entity in doc.entities:
        print(entity.text, "-", entity.category)