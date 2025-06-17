import os
from fpdf import FPDF
from PyPDF2 import PdfReader
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

import streamlit as st

# Load local .env file if it exists (for local dev)
load_dotenv()

# Helper function to fetch secrets
def get_secret(key):
    return os.getenv(key) or st.secrets.get(key)

api_key = get_secret("GOOGLE_API_KEY")


genai.configure(api_key)
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')


##extract the contents of pdf
def Extractpdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

##function to get ai response
def Response(input_text, pdf_content, prompt):
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text