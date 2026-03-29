from data_fetch import dataFetch
import streamlit as st



st.title("Welcome to AnimeR!!" )
#st.write(dataFetch())
st.button("Search" )

st.text_input(placeholder="Search",label="search" ,)
st.header("Popullar anime")
st.badge(label="badge")
form_value = {
    "name" : None,
}
st.subheader("test")
with st.form(key="key"):
    
   form_value["name"]= st.text_input("Enter your name:")
   age = st.number_input("Enter your age:")
   gender = st.selectbox("Gender:", ["Made","Female"])
   date_birth = st.date_input("Date of birth:")


   subButton = st.form_submit_button(label="Submit")
   if subButton :
     if not (age and form_value["name"]):
          st.warning("please fill all the values !")
     else :
        st.success("display data")
        for key , value in form_value.items():               
         st.write(f"{key}: {value}")


# Session_State

if "counter" not in st.session_state :
   st.session_state.counter = 0
st.write(f"Counter Value {st.session_state.counter}")   
if st.button("Increent counter!"):
 st.session_state.counter += 1
 st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Rest"):
   st.session_state.counter = 0
   st.write(f"Counter rested to {st.session_state.counter}" )



