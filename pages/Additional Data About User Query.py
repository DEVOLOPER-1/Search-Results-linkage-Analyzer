import streamlit as st
import cv2
import json

# Page configuration
st.header(
    "Welcome to :green[Search-Results-linkage-Analyzer]  :wave: (Dont't forget to reach out to us :smile:)",
    divider="rainbow",
)
st.subheader("Some Additional Data About Your Query :point_down:")
st.balloons()

# file import
with open("Additional_User_Query_Data.json") as f:
    data = json.load(f)
knowledge_graph_image = cv2.imread("Additional_User_Query_Image.jpeg")
true_image = cv2.cvtColor(knowledge_graph_image, cv2.COLOR_BGR2RGB)
Data_Column, Image_Column = st.columns(2)

with st.container(border=True):
    Data_Column.write("")
    Image_Column.write("")

with Data_Column:
    with st.container(border=True):
        st.title("Additional Data :blue[About] Your Query")
        st.subheader("If you :violet[Didn't] find any :red[Info] :red[here] Try to scrap it by yourself :red[through] the provided links in the another page") 

        st.table(data)

with Image_Column:
    with st.container(border=True):
        st.image(true_image)
