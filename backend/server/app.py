import os

from backend.db.user_verification import authenticate_user
from fastapi import FastAPI, HTTPException, Query
from dotenv import load_dotenv
import requests
import typing
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
#from backend.db.queries import get_db_connection


app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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

@app.get("/flashcards/")
async def get_flashcards(university: str, course: str):
    topics = get_topics(university, course)

    try:
        # Initialize Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Send the prompt to the model
        response = model.generate_content(
            f"Based on the topics {topics} from the course {course} at this school {university}, can you quiz me on the topics provided?",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"  # Keep the response type to JSON
            )
        )
        
        return Response(content=response.text, media_type='application/json')
    
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
    
    
# Login endpoint
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Login successful", "username": user["username"]}
    

# Function to fetch universities from the Universities API
def fetch_us_universities():
    try:
        response = requests.get("http://universities.hipolabs.com/search?country=United+States")
        response.raise_for_status()  # Raise an error if the request fails
        universities = response.json()
        return universities
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching universities: {str(e)}")

# Endpoint to insert universities from API to MySQL
# @app.post("/insert-universities/")
# def insert_universities():
#     response = requests.get("http://universities.hipolabs.com/search?country=United+States")
#     response.raise_for_status()  # Raise an error if the request fails
#     universities = response.json()

#     # Get the database connection using the existing connection logic
#     connection = get_db_connection()
#     cursor = connection.cursor()

#     try:
#         # insert_query = "INSERT INTO universities (university_name) VALUES (%s)"
#         for university in universities:
#             university_name = university["name"]
#             cursor.execute((university_name))  # Insert university name

#         connection.commit()  # Commit the transaction
#     except Exception as e:
#         connection.rollback()  # Rollback in case of error
#         raise HTTPException(status_code=500, detail=f"Error inserting universities: {str(e)}")
#     finally:
#         cursor.close()
#         connection.close()  # Close the connection after completion

#     return {"message": "Universities inserted successfully!"}

