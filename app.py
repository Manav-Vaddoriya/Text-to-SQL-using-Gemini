from dotenv import load_dotenv
load_dotenv()#loads all the environment variables
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

# configure gemini key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to generate response according to the prompt
def generating_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# function to retrieve the information from Student.db
def sql_query(sql,db):
    conn=sqlite3.connect(db)
    curr=conn.cursor()
    curr.execute(sql)
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# defining prompt --> most important step
prompt=[
    """
    You are in expert in english text to SQL query!
    the SQL Database has the columns = NAME,CLASS,SECTION

    For example 1 - How many entries of records are present?,the 
    corresponding SQL command will be SELECT COUNT(*) FROM STUDENT;

    For example 2 - Display all the records in the database, the
    corresponding SQL command will be SELECT * FROM STUDENT;

    Also SQL code should not have ''' in beginining or end and 
    SQL word in output
    
    """
]

# streamlit app setup
st.set_page_config(page_title="retriever of records")
st.header("Gemini App to retrieve data using SQL")

question = st.text_input("Input: ",key='input')

submit=st.button('Ask the question')

# after clicking button
if submit:
    sql_response=generating_response(question,prompt)
    response=sql_query(sql_response,'Student.db')
    st.subheader("The Response is...")
    for row in response:
        st.header(row)

