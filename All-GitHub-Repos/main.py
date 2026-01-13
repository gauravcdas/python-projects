# To install github --> uv add PyGithub
#To add PIl --> uv add pillow
import streamlit as st
import requests as rq
from github import Github
from PIL import Image
import pandas as pd

col1,col2,col3=st.columns([2,2,2])
with col2:
    img = Image.open("git.jpg")
    st.image(img,caption="Get all the repositories")

username = st.text_input("Enter a repository name")

if st.button("Get All"):
    if username =="":
        st.warning("Please enter a repository name")
    else:
        l=[]
        url = f"https://api.github.com/users/{username}"
        user_data = rq.get(url).json()
        print(user_data)
        if not user_data:
            st.text('Repositories not found')
        else:
            df = pd.DataFrame([user_data])
            st.dataframe(df)
            print(df)
            if not df.empty:
                col1,col2,col3=st.columns([2,2,2])
                with col2:
                    df_csv = df.to_csv()
                    st.download_button(
                        label="Download the repositories",
                        data=df_csv,
                        file_name="repositories.csv",
                    )

