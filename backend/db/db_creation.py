import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

# Database connection setup
timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host=os.environ['host'],
    password=os.environ['password'],
    read_timeout=timeout,
    port=17184,
    user=os.environ['user'],
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()


    # Create the 'users' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """)

    # Create the 'profiles' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        profile_id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        bio VARCHAR(500),
        university_id INT,
        class_id INT,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (university_id) REFERENCES universities(university_id),
        FOREIGN KEY (class_id) REFERENCES classes(class_id)
    );
    """)

    # Create the 'classes' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        class_id INT PRIMARY KEY AUTO_INCREMENT,
        class_name VARCHAR(255) NOT NULL,
        university_id INT,
        FOREIGN KEY (university_id) REFERENCES universities(university_id)
    );
    """)

    # Create the 'topics' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        topic_id INT PRIMARY KEY AUTO_INCREMENT,
        topic_name VARCHAR(255) NOT NULL,
        class_id INT,
        FOREIGN KEY (class_id) REFERENCES classes(class_id)
    );
    """)



    # Create the 'flashcards' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flashcards (
        flashcard_id INT PRIMARY KEY AUTO_INCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        topic_id INT,
        user_id INT,
        FOREIGN KEY (topic_id) REFERENCES topics(topic_id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
    );
    """)
    
    #fix mistake with universities -> universities_user
    
    """
    -- Step 1: Drop the old foreign key in 'profiles'
ALTER TABLE profiles
DROP FOREIGN KEY profiles_ibfk_2;

-- Step 2: Drop the old foreign key in 'classes'
ALTER TABLE classes
DROP FOREIGN KEY classes_ibfk_1;

-- Step 3: Add new foreign key to 'universities_user' in 'profiles'
ALTER TABLE profiles
ADD CONSTRAINT fk_profiles_universities_user FOREIGN KEY (university_id)
REFERENCES universities_user(university_id);

-- Step 4: Add new foreign key to 'universities_user' in 'classes'
ALTER TABLE classes
ADD CONSTRAINT fk_classes_universities_user FOREIGN KEY (university_id)
REFERENCES universities_user(university_id);
    
    """

    connection.commit()
    print("Tables created successfully.")

finally:
    connection.close()