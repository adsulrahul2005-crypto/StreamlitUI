import streamlit as st

st.title("My Website")

st.subheader("Website is going to be used for Machine Learning")

st.markdown("Just going for **SQL**")  # ** ** makes text bold

st.write("This is normal Text")

if st.button("Run Prediction"):
    st.write("Working on Prediction")

if st.button("View Chart"):
    st.write("Bar Plot is here")

Name = st.text_input("Enter your Name:")
st.write(Name)

Age = st.number_input("Enter the Age:")
st.write(Age)

rating = st.slider("Rate this app" , 1,5)
st.write(rating)

City = st.selectbox(
    "choose city",
    ['Pune',"Mumbai","Nashik"]
)
st.write(City)

agree = st.checkbox("I Agree")
st.write(agree)

st.success("Login Successful")


import streamlit as st
st.error("Wrong Password")

st.warning("please Enter All Details")