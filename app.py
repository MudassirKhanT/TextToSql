from dotenv import load_dotenv
load_dotenv() ## Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## condigure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to Load Google Gemini Model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from the sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cursor=conn.cursor()
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name ST has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example, \nExample 1 - How many entries of records are present?,
    \nExample 2 - Tellme all the students studying in 10th class?,
    the SQL command will be something like this SELECT * FROM ST WHERE CLASS="10th";
    also the SQL code should not have ``` in the beginning or end and sql word in the output
    """
]

## Streamlit App

st.set_page_config(page_title="I can retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input:",key="input")

submit=st.button("Ask the question")

## if submit is clicked 
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"st.db")
    st.subheader("The response is:")
    for row in data:
        print(row)
        st.header(row)