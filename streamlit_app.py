import streamlit as st
import wget


st.title("My Streamlit App!")

with st.form("app_form"):
  status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))
  

  submitted = st.form_submit_button("Submit")
  if submitted:
    st.write("You pressed submit!")
    st.image(wget.download("https://http.cat/" + status_code))
