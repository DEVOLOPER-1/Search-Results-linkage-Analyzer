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

with open("degree_centrality_of_network.json") as f:
    centrality_data = json.load(f)

Network_Graph_detected_cluster = cv2.imread("Girvan_Newman.jpeg")



website_title_with_position_df = pd.DataFrame.from_dict(data, orient="index")
# table = st.table(website_title_with_position_df) Just for testing purpose and it makes a print function
website_title_with_relevancy_values_df = pd.DataFrame.from_dict(data_2, orient="index")

Degree_centrality_values_df = pd.DataFrame.from_dict(centrality_data, orient="index")


st.title("According to your query here are the :green[results] :point_down:")

# Tabs Objects contains the upcoming  in main Dash Board


#Graphs_tab , Charts_tab = st.tabs(["Charts", "Graphs"]) #Not Working

# Column Objects in the main Dash Board

#Distributing Columns in 2 rows in the DashBoard
Priority, Relevancy,Degree_centrality = st.columns(3, gap="large")
Network_Graph , Girvan_new_man = st.columns(2, gap="large")
with st.container(border=True):
    Priority.write("")
    Relevancy.write("")
    Degree_centrality.write("")
with st.container(border=True):
    Network_Graph.write("")
    Girvan_new_man.write("")



# The container of each column


# Priority Bar Chart container
# with Charts_tab:
with Priority:
    with st.container(border=True):
        st.title("Results :blue[Priority] Chart")
        st.subheader(":red[Lower] values :arrow_forward: Higher :green[priority]")
        st.bar_chart(
            data=website_title_with_position_df,
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
# with Charts_tab:
with Relevancy:
    with st.container(border=True):
        st.title("Results :blue[Relevancy] Chart")
        st.subheader(":violet[Higher] values :arrow_forward: Higher :green[Relevancy]")
        st.bar_chart(
            data=website_title_with_relevancy_values_df,
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
        st.subheader(":violet[Some] nodes have been :arrow_forward: :red[Eliminated]")
        st.image(Relevancy_Network_Map)
        with st.expander(
            "See explanation"
        ):
            st.write("The Network Graph is an interactive graph that" 
                    "shows the relationships between the websites"
                    "and some websites are eliminated by comparing"
                    "the value of each node with a treshold values. ")
            
            
            
with Degree_centrality:
    with st.container(border=True):
        st.title(":blue[Degree Centrality] Chart")
        st.subheader(":red[Higher] values :arrow_forward: Higher :green[Centrality]")
        st.line_chart(
            data=Degree_centrality_values_df,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation"
        ):  # The string Data in st.write() is maintained like mark down
            st.write("The Degree Centrality of each website is calculated" 
                    "according to the by counting the number of connections" 
                    "each website has.  Also you should realize that they are" 
                    "all equal as the treshold have removed some lower relative results "
                    "and all  websites are relevant to each other. "
            )





with Girvan_new_man:
    with st.container(border=True):
        st.title(":blue[Clustered] Community Graph")
        st.subheader("It's as same as the Network Graph")
        st.image(Network_Graph_detected_cluster)
        with st.expander(
            "Why do the cluster is the same as the Network Graph ?\n" "See explanation :point_down:"
        ):
            st.write("How Does Girvan Newman work ?\n" 
                    "The idea was to find which edges in a network occur most frequently between " 
                    "other pairs of nodes by finding edges betweenness centrality."
                    "The edges joining communities are then expected to have a high edge betweenness."
                    "The underlying community structure of the network will be much more fine-grained once " 
                    "the edges with the highest betweenness are eliminated which means that communities will "
                    "be much easier to spot.")

#Launching Dashboard

