import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
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

st.header("Welcome to :green[Search-Results-linkage-Analyzer]  :wave:", divider="rainbow")


# file Import

with open("website_title_with_position.json") as f:
    data = json.load(f)  

with open("website_title_with_relevancy_values_2.json") as f:  
    data_2 = json.load(f)

website_title_with_position_df = pd.DataFrame.from_dict(data, orient="index")
# table = st.table(website_title_with_position_df) Just for testing purpose and it makes a print function
website_title_with_relevancy_values_df =pd.DataFrame.from_dict(data_2, orient="index")

st.title("According to your query there are the :green[results] :point_down:")

#Column Objects in the main Dash Board

Priority , Relevancy , Network_Graph = st.columns(3)

#The container of each column
#Priority Bar Chart container
with Priority:
    with st.container(border=True):
        st.title("Results :blue[Priority] Bar Chart")
        st.subheader(":red[Lower] values :arrow_forward: Higher :green[priority]")
        st.bar_chart(
            data=website_title_with_position_df, 
            width=0, 
            height=0, 
            use_container_width=True,
            color = "#4F6F52"
        )
