import os
import typing
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI, Response

app = FastAPI()

load_dotenv()

genai.configure(api_key=os.environ["Gemini_Key"])

class FlashCards(typing.TypedDict):
    question: str
    answer: str

@app.post("/flashcards/")
async def get_gemini_result(prompt: str):
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the prompt to the model
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"  # Keep the response type to JSON
            )
        )
        
        return Response(content=response.text, media_type="application/json")
    
    except Exception as e:
        return {"error": str(e)}
    

@app.post("/topics")
async def get_topics(university: str, course: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            f"What topics does the course {course} from the school {university} cover?",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        
        )

        return Response(content=response.text, media_type="application/json")
    except Exception as e:
        return {"error": str(e)}