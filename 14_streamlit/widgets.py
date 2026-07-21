import streamlit as st
import pandas as pd

# setting the title
st.title("Streamlit text input")

# taking input
name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}")
    
# creating slider
age = st.slider("Select your age: ", 0,100,25)  # min, max, starting_point(default)
st.write(f"You are {age} years old")

# selectbox
options = ['Philosophy', 'Psychology', 'Yoga', 'STEM']
choice = st.selectbox("Choose your favourite stream", options)

st.write(f"{choice}...WOW!! Nice Choice.")
    
# upload button
uploaded = st.file_uploader("Choose a csv file", type='csv')
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df)