import streamlit as st
from PIL import Image

st.title('Funding trends visualizer')

image_1 = Image.open('assets/vis-1.png')
image_2 = Image.open('assets/vis-2.png')
image_3 = Image.open('assets/vis-3.png')
image_4 = Image.open('assets/vis-4.png')

st.caption('\* The visulisation above utilizes the startups data from 2019-2021')

st.header('Major Startup Sectors')
st.text('Top 20 domain-based startups that grew successfully')
st.image(image_1)

st.header('Major Startup Locations')
st.text('Locations where startups favoured setting up their offices')
st.image(image_2)

st.header('Startup sector funded more')
st.text('Startup entrepreneurs who caught the attention of investors')
st.image(image_3)

st.header('Prime startup location')
st.text('Support for startups based on location')
st.image(image_4)
