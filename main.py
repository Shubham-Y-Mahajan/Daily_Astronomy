import requests
import streamlit as st


api_key="ERwZSMAurQzBbSle6gEhkxRkMfaXTei1CqpYPpuY"
url="https://api.nasa.gov/planetary/apod?api_key=ERwZSMAurQzBbSle6gEhkxRkMfaXTei1CqpYPpuY"

request=requests.get(url)

Content=request.json()

debug=" "

img_url=Content["url"]
response=requests.get(img_url)

with open("image.jpg","wb") as file:
    file.write(response.content)

description=Content["explanation"]
date=Content["date"]
title=Content["title"]

st.title(title + " - " + date)

st.image("image.jpg")

st.info(description)










