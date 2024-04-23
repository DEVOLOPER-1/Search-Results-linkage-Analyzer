import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import cv2
import json

# Page configuration
st.set_page_config(
    page_title="Search-Results-linkage-Analyzer",
    page_icon="📊",
    layout="wide",  # To Use the entire screen as we want
    initial_sidebar_state="auto",
    menu_items={
        "About": "https://www.linkedin.com/in/youssef-mohammad-9341a71a7",
        "Get help": "https://github.com/DEVOLOPER-1",
    },
)

st.header(
    "Welcome to :green[Search-Results-linkage-Analyzer]  :wave:", divider="rainbow"
)


# file Import

with open("website_title_with_position.json") as f:
    data = json.load(f)

with open("website_title_with_relevancy_values_2.json") as f:
    data_2 = json.load(f)
    
Relevancy_Network_Map = cv2.imread("Network Graph.jpeg")    

website_title_with_position_df = pd.DataFrame.from_dict(data, orient="index")
# table = st.table(website_title_with_position_df) Just for testing purpose and it makes a print function
website_title_with_relevancy_values_df = pd.DataFrame.from_dict(data_2, orient="index")

st.title("According to your query there are the :green[results] :point_down:")

# Column Objects in the main Dash Board

Priority, Relevancy, Network_Graph = st.columns(3)

# The container of each column


# Priority Bar Chart container
with Priority:
    with st.container(border=True):
        st.title("Results :blue[Priority] Chart")
        st.subheader(":red[Lower] values :arrow_forward: Higher :green[priority]")
        st.bar_chart(
            data=website_title_with_position_df,
            width=0,
            height=0,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation"
        ):  # The string Data in st.write() is maintained like mark down
            st.write(
                "The Position of websites (Priority) in the SERP is determined by Google's complex algorithm,"
                "which takes into account hundreds of different ranking factors or signals,"
                "including the relevance, authority and trustworthiness of the website."
            )


# Relevancy Bar Chart container
with Relevancy:
    with st.container(border=True):
        st.title("Results :blue[Relevancy] Chart")
        st.subheader(":violet[Higher] values :arrow_forward: Higher :green[Relevancy]")
        st.bar_chart(
            data=website_title_with_relevancy_values_df,
            width=0,
            height=0,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation"
        ):  # The string Data in st.write() is maintained like mark down
            st.write(
                "The calculation of relevancy for each result is done by the following : "
                "each result  has a snippet tuple so the words of each tuple are counted in "
                "the whole snippets words and then divided over the number of all words of snippets "
                "this algorithm is applied according TF rule and then the TF for words"
                "in the same snippet is summed to make a dictionary at he end from websites names as keys : Relevancy as value ."
            )
            
            
with Network_Graph:
    with st.container(border=True):
        st.title("Network Graph")
        st.subheader(":violet[Some] nodes have been :red[Eliminated]")
        st.image(Relevancy_Network_Map)
        with st.expander(
            "See explanation"
        ):
            st.write("The Network Graph is an interactive graph that shows the relationships between the websites. ")
