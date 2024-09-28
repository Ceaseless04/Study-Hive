from fastapi import FastAPI, HTTPException
import requests
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = FastAPI()

load_dotenv()

genai.configure(api_key=os.environ["API_KEY"])

@app.post("/gemini-prompt/")
async def get_gemini_result(prompt: str):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# To run the app, use: