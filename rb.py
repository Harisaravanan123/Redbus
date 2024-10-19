import streamlit as st
import pandas as pd
choose=st.sidebar.radio(label="choose an option",options=('image','video'))
if choose=='image':
    st.image("C:/Users/nambi/Downloads/redbus logo.png",width=460)
if choose=='video':
    st.video("https://youtu.be/kdSqTsAeNxo?si=H0so9lIEZWK6kwoA")
st.sidebar.markdown("[redbus](https://www.redbus.in/)") 
st.title("redbus")    
st.subheader("state transport corporation buses")
uploaded_file=st.file_uploader("upload the redbus_csv file",type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv("E:/projects/redbusproject/redbus.csv")
    st.write(df)
#for filtering the routename:
if 'routename' in df.columns:
    routes=df['routename'].unique()
    selected_route_names=st.multiselect("select the routename",options=routes)
    if selected_route_names:
        df[df['routename'].isin (selected_route_names)]
#for filtering the busname:
if 'Bus_Name' in df.columns:
    buses=df['Bus_Name'].unique()
    selected_bus_name=st.multiselect("select the bus",options=buses) 
    if selected_bus_name:
        df[df['Bus_Name'].isin(selected_bus_name)]
if 'Bus_Type' in df.columns:
    bustype=df['Bus_Type'].unique() 
    selected_bus_type=st.multiselect('select the bustype',options=bustype)
    if selected_bus_type:
        df[df['Bus_Type'].isin(selected_bus_type)]
#for filtering the star_rating
if "Star_Rating" in df.columns:
        min_rating,max_rating=st.slider(
       "select the rating",
        min_value=0.0,
        max_value=5.0,
        value=(0.0,5.0),
        step=0.1
) 
df[(df["Star_Rating"]>=min_rating)&(df["Star_Rating"]<=max_rating)]
if "Price"  in df.columns:
     min_price,max_price=st.slider(
         "select the price_range",
         min_value=0,
         max_value=int(df["Price"].max()),
         value=(0,int(df["Price"].max())),
         step=1
     )
df[(df["Price"]>=min_price)&(df["Price"]<=max_price)]              

    

