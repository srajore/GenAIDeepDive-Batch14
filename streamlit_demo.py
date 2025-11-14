import streamlit as st


st.title("Hello World")

st.header("This is a header")

st.write("This is a text")

st.button("Submit")

all_users = ["Alice", "Bob", "Charly"]

with st.container(border=True):
    users = st.multiselect("Uss", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
