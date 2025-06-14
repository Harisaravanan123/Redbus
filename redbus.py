import sqlalchemy
import mysql.connector
import base64
import pandas as pd
import streamlit as st 
st.set_page_config(page_title="Redbus",page_icon=":bus:",layout="centered")
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg("C:/Users/nambi/Downloads/58912b2e3ad6a279347eebb47751a9c1.jpg")

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #9899AA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:maroon;'>Red bus</h1>", unsafe_allow_html=True)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="redbus"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT DISTINCT state from BUSDETAILS")
state = [row[0] for row in mycursor.fetchall()]


st.sidebar.header('SELECT THE STATE')
State = st.sidebar.selectbox('State',options=state)
query = "SELECT DISTINCT routename from BUSDETAILS WHERE state = %s"
mycursor.execute(query,(State,))
Route = [row[0] for row in mycursor.fetchall()]
st.sidebar.header('SELECT THE ROUTE')
route = st.sidebar.selectbox('routes',options=Route) 
button = st.sidebar.button('SHOW BUSES')   
if button:
    query = "SELECT routelink,Bus_Name,Bus_Type,Departing_Time,Duration,Reaching_Time,Star_Rating,Price,Seat_Availability from BUSDETAILS  WHERE routename = %s ORDER BY Star_Rating DESC"
    mycursor.execute(query,(route,))
    column_names = [col[0] for col in mycursor.description]
    data = mycursor.fetchall()
    df = pd.DataFrame(data,columns=column_names)
    st.dataframe(df)


