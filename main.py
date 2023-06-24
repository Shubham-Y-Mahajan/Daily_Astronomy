import requests
import streamlit as st


api_key="ERwZSMAurQzBbSle6gEhkxRkMfaXTei1CqpYPpuY"
url="https://api.nasa.gov/planetary/apod?api_key=ERwZSMAurQzBbSle6gEhkxRkMfaXTei1CqpYPpuY"

#make request for api
request=requests.get(url)

#Get a dictionary with data
Content=request.json()

debug=" "

# To extract anything other than text from the api (like images) we will have to perform the below tasks
img_url=Content["url"] # the url of image within the api
response=requests.get(img_url)

# here response.text won't work as an image is neither a text nor a json disctionary
#we will have to use  .content attribute

# response.content will be a binary text which will then be written in a file
# that binary data once written in a file will be seen as an image

with open("image.jpg","wb") as file: #wb means write binary
    file.write(response.content)

#now image.jpg will have the image in it

#Extracting rest of the content ftom api
description=Content["explanation"]
date=Content["date"]
title=Content["title"]

#Drafting the web page
#st.set_page_config(layout="wide")
st.title(title + " - " + date)


#col1,col2=st.columns(2)

#with col1:
st.image("image.jpg")
#with col2:
st.info(description)










