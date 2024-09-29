import pymysql
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()



# Load the CSV file
file_path = './us_universities.csv'
universities_df = pd.read_csv(file_path)

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

def insert_universities_from_csv():
    try:
        cursor = connection.cursor()
        
        for index, row in universities_df.iterrows():
            university_name = row['name']
            
            print(f"Inserting: {university_name}")  # Print the name to debug
            cursor.execute("""
            INSERT IGNORE INTO universities (university_name) 
            VALUES (%s);
            """, (university_name,))
        
        connection.commit()
        print("Universities inserted successfully.")
    
    finally:
        connection.close()

insert_universities_from_csv()