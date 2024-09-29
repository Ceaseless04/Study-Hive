from fastapi import FastAPI
import mysql.connector
import os
import pymysql
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Database connection setup
def get_db_connection():
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=10,
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb", 
        host=os.environ['host'],
        password=os.environ['password'],
        port=17184,
        user=os.environ['user'],
        write_timeout=10,
    )
    return connection


#Insert
def insert_user(username, email, password):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, email, password))
        connection.commit()
    finally:
        connection.close()
        
def insert_class(class_name, university_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # First, find the university_id from the universities table
            sql_university = "SELECT university_id FROM universities WHERE university_name = %s LIMIT 1"
            cursor.execute(sql_university, (university_name,))
            university = cursor.fetchone()

            if university:
                university_id = university['university_id']
                # Now insert the class
                sql_class = "INSERT INTO classes (class_name, university_id) VALUES (%s, %s)"
                cursor.execute(sql_class, (class_name, university_id))
                connection.commit()
            else:
                print(f"University '{university_name}' not found.")
    finally:
        connection.close()
        
def insert_profile(username, bio, university_name, class_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Get user_id
            sql_user = "SELECT user_id FROM users WHERE username = %s LIMIT 1"
            cursor.execute(sql_user, (username,))
            user = cursor.fetchone()

            # Get university_id
            sql_university = "SELECT university_id FROM universities WHERE university_name = %s LIMIT 1"
            cursor.execute(sql_university, (university_name,))
            university = cursor.fetchone()

            # Get class_id
            sql_class = "SELECT class_id FROM classes WHERE class_name = %s LIMIT 1"
            cursor.execute(sql_class, (class_name,))
            class_ = cursor.fetchone()

            if user and university and class_:
                sql_profile = """INSERT INTO profiles (user_id, bio, university_id, class_id) 
                                 VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql_profile, (user['user_id'], bio, university['university_id'], class_['class_id']))
                connection.commit()
            else:
                print(f"Error: Could not find the necessary user, university, or class.")
    finally:
        connection.close()
        

def insert_profile(username, bio, university_name, class_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Get user_id
            sql_user = "SELECT user_id FROM users WHERE username = %s LIMIT 1"
            cursor.execute(sql_user, (username,))
            user = cursor.fetchone()

            # Get university_id
            sql_university = "SELECT university_id FROM universities WHERE university_name = %s LIMIT 1"
            cursor.execute(sql_university, (university_name,))
            university = cursor.fetchone()

            # Get class_id
            sql_class = "SELECT class_id FROM classes WHERE class_name = %s LIMIT 1"
            cursor.execute(sql_class, (class_name,))
            class_ = cursor.fetchone()

            if user and university and class_:
                sql_profile = """INSERT INTO profiles (user_id, bio, university_id, class_id) 
                                 VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql_profile, (user['user_id'], bio, university['university_id'], class_['class_id']))
                connection.commit()
            else:
                print(f"Error: Could not find the necessary user, university, or class.")
    finally:
        connection.close()


def insert_topic(topic_name, class_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Get class_id
            sql_class = "SELECT class_id FROM classes WHERE class_name = %s LIMIT 1"
            cursor.execute(sql_class, (class_name,))
            class_ = cursor.fetchone()

            if class_:
                sql_topic = "INSERT INTO topics (topic_name, class_id) VALUES (%s, %s)"
                cursor.execute(sql_topic, (topic_name, class_['class_id']))
                connection.commit()
            else:
                print(f"Class '{class_name}' not found.")
    finally:
        connection.close()
        

def insert_flashcard(question, answer, topic_name, username):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Get topic_id
            sql_topic = "SELECT topic_id FROM topics WHERE topic_name = %s LIMIT 1"
            cursor.execute(sql_topic, (topic_name,))
            topic = cursor.fetchone()

            # Get user_id
            sql_user = "SELECT user_id FROM users WHERE username = %s LIMIT 1"
            cursor.execute(sql_user, (username,))
            user = cursor.fetchone()

            if topic and user:
                sql_flashcard = """INSERT INTO flashcards (question, answer, topic_id, user_id)
                                   VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql_flashcard, (question, answer, topic['topic_id'], user['user_id']))
                connection.commit()
            else:
                print(f"Error: Could not find the necessary topic or user.")
    finally:
        connection.close()
        
''' # Testing inputs:
import random
import string

# Random value generation
def random_string(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_email():
    domains = ['example.com', 'test.com', 'mail.com']
    return f"{random_string()}@{random.choice(domains)}"

def random_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(length))

# Random test variables
username = random_string()
email = random_email()
password = random_password()
university_name = "Test University"
class_name = random_string() + " Class"
bio = "This is a randomly generated bio."
topic_name = random_string() + " Topic"
question = "What is " + random_string() + "?"
answer = "Random answer: " + random_string()

insert_user(username, email, password)
insert_class(class_name, university_name)
insert_profile(username, bio, university_name, class_name)
insert_topic(topic_name, class_name)
insert_flashcard(question, answer, topic_name, username)

'''



#Output
def get_user_by_username(username):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()  # Fetch only the specific user
            return user
    finally:
        connection.close() 
        
        
def get_user_profile(username):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT u.username, u.email, p.bio, un.university_name, c.class_name
            FROM users u
            JOIN profiles p ON u.user_id = p.user_id
            JOIN universities un ON p.university_id = un.university_id
            JOIN classes c ON p.class_id = c.class_id
            WHERE u.username = %s
            """
            cursor.execute(sql, (username,))
            profile = cursor.fetchone()  # Fetch the profile of a specific user
            return profile
    finally:
        connection.close()
        
def get_all_classes():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT c.class_name, un.university_name
            FROM classes c
            JOIN universities un ON c.university_id = un.university_id
            """
            cursor.execute(sql)
            classes = cursor.fetchall()  # Fetch all classes
            return classes
    finally:
        connection.close()
        
        
def get_topics_for_class(class_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT t.topic_name
            FROM topics t
            JOIN classes c ON t.class_id = c.class_id
            WHERE c.class_name = %s
            """
            cursor.execute(sql, (class_name,))
            topics = cursor.fetchall()  # Fetch all topics for the class
            return topics
    finally:
        connection.close()
        
def get_flashcards_for_topic(topic_name):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """
            SELECT f.question, f.answer
            FROM flashcards f
            JOIN topics t ON f.topic_id = t.topic_id
            WHERE t.topic_name = %s
            """
            cursor.execute(sql, (topic_name,))
            flashcards = cursor.fetchall()  # Fetch all flashcards for the topic
            return flashcards
    finally:
        connection.close()
        


@app.get("/user/{username}")
def show_user(username: str):
    user = get_user_by_username(username)
    return {"user": user}




