import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# ---------------Method 1: Copy the JSON file link in the code-------------------------


url=requests.get("https://assets4.lottiefiles.com/packages/lf20_U6OKyytl3f.json")
url_json=dict()
if url.status_code==200:
    url_json=url.json()
else:
    print("error in the url")
st.title("Adding Lottie Animation in Streamlit WebApp")
st_lottie(url_json,
          reverse=True,
          # height and width of animation
          height=400,  
          width=400,
          # speed of animation
          speed=1,  
          # means the animation will run forever like a gif, and not as a still image
          loop=True,  
          # quality of elements used in the animation, other values are "low" and "medium"
          quality='high')

#Method 2: Download the JSON file and import it into our code

path ="C:\\Users\\DELL\\OneDrive\\Desktop\\lottie_animation\\143202-snake.json"
with open(path,"r") as file:
    url = json.load(file)

st.title("Adding Lottie Animation in Streamlit WebApp")

st_lottie(url,
	reverse=True,
	height=400,
	width=400,
	speed=1,
	loop=True,
	quality='high'
)
