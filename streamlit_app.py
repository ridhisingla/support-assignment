import streamlit as st
import wget
import requests
  
def main():
    st.title("My Streamlit App!")
    session = requests.Session()
    with st.form("my_form"):
        status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://http.cat/{status_code}")
            if data:
                st.image(data['download_url'], caption=f"Author: {data['author']}")
            else:
                st.error("Error")
