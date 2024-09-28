from fastapi import FastAPI, HTTPException
import requests
from dotenv import load_dotenv
import os
import google.generativeai as genai

app = FastAPI()

load_dotenv()

genai.configure(api_key=os.environ["Gemini_Key"])

@app.post("/gemini-prompt/")
async def get_gemini_result(prompt: str):
    try:
        # Initialize Gemini model (replace with your model details)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the prompt to the model
        response = model.generate_content(prompt)
        
        # Extract the text from the response
        generated_text = response.text
        
        # Split the text into an array of words
        words_array = generated_text.split()
        
        # Return an object with the array of words
        return {"words": words_array}
    
    except Exception as e:
        return {"error": str(e)}

# To run the app, use: