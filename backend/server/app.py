<<<<<<< Updated upstream
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

def get_topics(university: str, course: str):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            f"What topics does the course {course} from the school {university} cover?",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        
        )

        print(response.text)

        return {"topics": response.text}
    except Exception as e:
        return {"error": str(e)}

@app.post("/flashcards/")
async def get_flashcards(university: str, course: str):
    topics = get_topics(university, course)

    try:
        # Initialize Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the prompt to the model
        response = model.generate_content(
<<<<<<< HEAD
<<<<<<< HEAD
            f"Based on the topics {topics} from the course {course} at this school {university}, can you quiz me on the topics provided? Make sure the University is a Valid University",
=======
            f"Based on the topics {topics} from the course {course} at this school {university}, can you quiz me on the topics provided?",
>>>>>>> 56af586 (WIP, got flashcards API to work)
=======
            f"Based on the topics {topics} from the course {course} at this school {university}, can you quiz me on the topics provided? Make sure the University is a Valid University",
>>>>>>> 6a7182b (test)
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"  # Keep the response type to JSON
            )
        )
        
        return Response(content=response.text, media_type="application/json")
    
    except Exception as e:
        return {"error": str(e)}

@app.post("/gemini-testing/")
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
