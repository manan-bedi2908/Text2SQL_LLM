from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
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
    \nExample 2 - How 
    many students study in DS Class,
    the SQL command will be something like this 
    SELECT COUNT(*) from STUDENT
    WHERE CLASS = "DS";
    also the SQL query should not have ``` in beginning or end 
    and sql word in the output.
    """
]

st.set_page_config(page_title='Text 2 SQL Generator')
st.header('Text2SQL Generator')

question = st.text_input('Input: ', key='input')
submit = st.button('Ask the question')

if submit:
    response = get_gemini_response(question, prompt)
    response = read_sql_query(response, "student.db")
    st.subheader('The Response is: ')
    for row in response:
        st.write(row)









