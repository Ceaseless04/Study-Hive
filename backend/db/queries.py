import mysql.connector
import os

# Define the database connection
def get_db_connection():
    return mysql.connector.connect(
        host='mysql-5be2d08-studi-hive-db1.g.aivencloud.com',
        port=17184,
        user=os.environ('user'),
        password=os.environ('password'),
        database='defaultdb'  # Start with the default database or 'Study_hive_db' if it already exists
    )
    

# Establish the connection
connection = get_db_connection()
cursor = connection.cursor()

# Create the Study_hive_db database
cursor.execute("CREATE DATABASE IF NOT EXISTS defaultdb")

# Select the new database
cursor.execute("USE defaultdb")

# Create the universities table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS universities (
        university_id INT AUTO_INCREMENT PRIMARY KEY,
        university_name VARCHAR(255) NOT NULL
    )
""")

# Create the courses table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INT AUTO_INCREMENT PRIMARY KEY,
        course_name VARCHAR(255) NOT NULL,
        university_id INT,
        FOREIGN KEY (university_id) REFERENCES universities(university_id) ON DELETE CASCADE
    )
""")

# Create the topics table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        topic_id INT AUTO_INCREMENT PRIMARY KEY,
        topic_name VARCHAR(255) NOT NULL,
        course_id INT,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
    )
""")

# Create the flashcards table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        flashcard_id INT AUTO_INCREMENT PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        topic_id INT,
        FOREIGN KEY (topic_id) REFERENCES topics(topic_id) ON DELETE CASCADE
    )
""")


# Close the cursor and connection
cursor.close()
connection.close()

