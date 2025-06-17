import os
from fpdf import FPDF
from PyPDF2 import PdfReader
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
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