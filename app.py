from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

prompt = [
    """
    You are an expert in converting English questions to SQL queries.
    The SQL database has the name STUDENT and has the following columns:
    NAME, CLASS, SECTION \n\nFor example, \nExample 1 - How 
    many entries of records are present?,
    the SQL command will be something like this 
    SELECT COUNT(*) from STUDENT;
    also the SQL query should not have ''' in beginning or end 
    and sql word in the output.
    """
]