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
query = "SELECT DISTINCT Bus_Type FROM BUSDETAILS WHERE state = %s and routename = %s"
mycursor.execute(query,(State,route,))
bustype = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE BUSTYPE")
bus_type = st.sidebar.selectbox('bustype',options=bustype)
query = "SELECT DISTINCT Star_Rating from BUSDETAILS WHERE state = %s and routename = %s and Bus_Type = %s ORDER BY Star_Rating DESC" 
mycursor.execute(query,(State,route,bus_type,))
star_rating = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE STAR RATINGS")
star_ratings = st.sidebar.selectbox('star_rating',options=star_rating)
query = "SELECT DISTINCT Seat_Availability from BUSDETAILS WHERE state = %s and routename = %s and Bus_Type = %s and ROUND(Star_Rating, 1) = %s ORDER BY Seat_Availability DESC"
mycursor.execute(query,(State,route,bus_type,star_ratings,))
seats = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE SEAT")
seat = st.sidebar.selectbox('Seats',options=seats)
query = "SELECT DISTINCT Price from BUSDETAILS WHERE state = %s and routename = %s and Bus_Type = %s and ROUND(Star_Rating, 1) = %s and Seat_Availability=%s ORDER BY Price DESC"
mycursor.execute(query,(State,route,bus_type,star_ratings,seat,)) 
price = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE PRICE")
Price = st.sidebar.selectbox('price',options=price)
query = "SELECT DISTINCT Departing_Time from BUSDETAILS WHERE state = %s and routename = %s and Bus_Type = %s and ROUND(Star_Rating, 1) = %s and Seat_Availability=%s and Price=%s"
mycursor.execute(query,(State,route,bus_type,star_ratings,seat,Price))
dep_time = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE DEPARTING TIME")
Dep_t = st.sidebar.selectbox("departing time",options=dep_time)
query = "SELECT DISTINCT Duration from BUSDETAILS WHERE state = %s and routename = %s and Bus_Type = %s and ROUND(Star_Rating, 1) = %s and Seat_Availability=%s and Price=%s and Departing_Time = %s"
mycursor.execute(query,(State,route,bus_type,star_ratings,seat,Price,Dep_t))
Dur = [row[0] for row in mycursor.fetchall()]
st.sidebar.header("SELECT THE DURATION")
duration = st.sidebar.selectbox("duration",options=Dur)
button = st.sidebar.button('SHOW BUSES')
if button:
    query = "SELECT * FROM BUSDETAILS  WHERE state = %s AND routename = %s AND Bus_Type = %s AND ROUND(Star_Rating, 1) = %s AND Seat_Availability=%s and Price =%s and Departing_Time = %s and Duration = %s ORDER BY Star_Rating DESC "
    mycursor.execute(query,(State,route,bus_type,star_ratings,seat,Price,Dep_t,duration,))
    column_names = [col[0] for col in mycursor.description]
    data = mycursor.fetchall()
    df = pd.DataFrame(data,columns=column_names)
    st.dataframe(df)


