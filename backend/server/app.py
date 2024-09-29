import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
import requests

from backend.db.queries import get_db_connection


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
@app.post("/insert-universities/")
def insert_universities():
    universities = fetch_us_universities()  # Fetch universities from the API

    # Get the database connection using the existing connection logic
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        insert_query = "INSERT INTO universities (university_name) VALUES (%s)"
        for university in universities:
            university_name = university["name"]
            cursor.execute(insert_query, (university_name,))  # Insert university name

        connection.commit()  # Commit the transaction
    except Exception as e:
        connection.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail=f"Error inserting universities: {str(e)}")
    finally:
        cursor.close()
        connection.close()  # Close the connection after completion

    return {"message": "Universities inserted successfully!"}

