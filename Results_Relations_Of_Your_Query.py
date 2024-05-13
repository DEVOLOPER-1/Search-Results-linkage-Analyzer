# pip install streamlit-option-menu
import streamlit as st
import pandas as pd
import cv2
import json
import plotly.express as px

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


st.balloons()


st.header(
    "Welcome to :green[Search-Results-linkage-Analyzer]  :wave: (Dont't forget to reach out to us :smile:)",
    divider="rainbow",
)


# file Import

with open("website_title_with_position.json") as f:
    data = json.load(f)

with open("website_title_with_relevancy_values_2.json") as f:
    data_2 = json.load(f)


with open("filtered_relevancy_valued_dict_2.json") as f:
    filtered_data = json.load(f)
filtered_relevancy_valued_dict_2_df = pd.DataFrame.from_dict(
    filtered_data, orient="index"
)

with open("all_results_links_dict.json") as f:
    data_3 = json.load(f)
organic_results_df = pd.DataFrame.from_dict(data_3, orient="index")

Relevancy_Network_Map = cv2.imread("Network Graph.jpeg")
Relevancy_Network_Map = cv2.cvtColor(Relevancy_Network_Map, cv2.COLOR_BGR2RGB)
with open("degree_centrality_of_network.json") as f:
    centrality_data = json.load(f)

Network_Graph_detected_cluster = cv2.imread("Girvan_Newman.jpeg")
Network_Graph_detected_cluster = cv2.cvtColor(
    Network_Graph_detected_cluster, cv2.COLOR_BGR2RGB
)
with open("betweenness_centrality_of_network.json") as f:
    betweenness_data = json.load(f)


with open("relevant_results_with_links.json") as f:
    relevant_results_with_links_data = json.load(f)

with open("filtered_relevancy_valued_dict_2_links.json") as f:
    filtered_relevancy_valued_dict_2_links_data = json.load(f)
filtered_relevancy_valued_dict_2_links_data_df = pd.DataFrame.from_dict(
    filtered_relevancy_valued_dict_2_links_data, orient="index"
)
ThreeD_Network_Map_Graph = cv2.imread("3D Graph.jpeg")
ThreeD_Network_Map_Graph = cv2.cvtColor(ThreeD_Network_Map_Graph, cv2.COLOR_BGR2RGB)

# Relevancy_heatmap_Graph_Data = cv2.imread("Heatmap.jpeg")
# Relevancy_heatmap_Graph_Data = cv2.cvtColor(
#     Relevancy_heatmap_Graph_Data, cv2.COLOR_BGR2RGB
# )
website_title_with_position_df = pd.DataFrame.from_dict(data, orient="index")
# table = st.table(website_title_with_position_df) Just for testing purpose and it makes a print function
website_title_with_relevancy_values_df = pd.DataFrame.from_dict(data_2, orient="index")

Degree_centrality_values_df = pd.DataFrame.from_dict(centrality_data, orient="index")

Betweenness_centrality_values_df = pd.DataFrame.from_dict(
    betweenness_data, orient="index"
)

relevant_results_with_links_data_df = pd.DataFrame.from_dict(
    relevant_results_with_links_data, orient="index"
)

st.title("According to your query here are the :green[results] :point_down:")

# Tabs Objects contains the upcoming  in main Dash Board


# Graphs_tab , Charts_tab = st.tabs(["Charts", "Graphs"]) #Not Working

# Column Objects in the main Dash Board

# Distributing Columns in 2 rows in the DashBoard
Priority, Relevancy, Degree_centrality, Betweenness_centrality = st.columns(
    4, gap="small"
)
Network_Graph, Girvan_new_man, ThreeD_Network_Map, Relevancy_heatmap = st.columns(
    4, gap="small"
)
with st.container(border=True):
    Priority.write("")
    Relevancy.write("")
    Degree_centrality.write("")
    Betweenness_centrality.write("")
with st.container(border=True):
    Network_Graph.write("")
    Girvan_new_man.write("")
    ThreeD_Network_Map.write("")
    Relevancy_heatmap.write("")

# The container of each column


# Priority Bar Chart container
# with Charts_tab:
with Priority:
    with st.container(border=True):
        st.title("Results :red[Priority] Chart")
        st.subheader(":red[Lower] values :arrow_forward: Higher :green[priority]")
        st.bar_chart(
            data=website_title_with_position_df,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation :point_down:"
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
        st.title("Results :red[Relevancy] Chart")
        st.subheader(":red[Higher] values :arrow_forward: Higher :green[Relevancy]")
        st.bar_chart(
            data=website_title_with_relevancy_values_df,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation :point_down:"
        ):  # The string Data in st.write() is maintained like mark down
            st.write(
                "The calculation of relevancy for each result is done by the following : "
                "each result  has a snippet tuple so the words of each tuple are counted in "
                "the whole snippets words and then divided over the number of all words of snippets "
                "this algorithm is applied according TF rule and then the TF for words"
                "in the same snippet is summed to make a dictionary at he end from websites names as keys : Relevancy as value ."
                "and then the final value of TF is multiplied by the reciprocal of value of position to make values more logical ."
            )

with Network_Graph:
    with st.container(border=True):
        st.title(":blue[Relevancy]" "  Network  " "Graph")
        st.subheader(":violet[Some] nodes have been :arrow_forward: :red[Eliminated]")
        st.image(Relevancy_Network_Map)
        with st.expander("See explanation :point_down:"):
            st.write(
                "The Network Graph is an interactive graph that"
                "shows the relationships between the websites"
                "and some websites are eliminated by comparing"
                "the value of each node with a treshold values. "
            )


with Degree_centrality:
    with st.container(border=True):
        st.title(":blue[Degree Centrality] Chart")
        st.subheader(":red[Higher] values :arrow_forward: Higher :green[Centrality]")
        st.area_chart(
            data=Degree_centrality_values_df,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation :point_down:"
        ):  # The string Data in st.write() is maintained like mark down
            st.write(
                "The Degree Centrality of each website is calculated "
                "by counting the number of connections "
                "each website has in the network map.  Also you should realize that they are "
                "all equal as the treshold have removed some lower relative results "
                "and all  websites are relevant to each other. "
            )


with Betweenness_centrality:
    with st.container(border=True):
        st.title(":blue[Betweenness Centrality] Chart")
        st.subheader(":red[Higher] values :arrow_forward: Higher :green[Centrality]")
        st.area_chart(
            data=Betweenness_centrality_values_df,
            use_container_width=True,
            color="#4F6F52",
        )
        with st.expander(
            "See explanation :point_down:"
        ):  # The string Data in st.write() is maintained like mark down
            st.write(
                "Betweenness centrality measures a node's importance in a network by counting "
                "how many shortest paths between other nodes pass through it. "
                "Imagine traffic flowing through a city - a central bridge would "
                "have high betweenness centrality because many routes use it. "
            )


with Girvan_new_man:
    with st.container(border=True):
        st.title(":blue[Clustered] Community Graph")
        st.subheader("It's :violet[as same as] the Network Graph")
        st.image(Network_Graph_detected_cluster)
        with st.expander(
            "Why do the cluster is the same as the Network Graph ?\n"
            "See explanation :point_down:"
        ):
            st.write(
                "How Does Girvan Newman work ?\n"
                "The idea was to find which edges in a network occur most frequently between "
                "other pairs of nodes by finding edges betweenness centrality."
                "The edges joining communities are then expected to have a high edge betweenness."
                "The underlying community structure of the network will be much more fine-grained once "
                "the edges with the highest betweenness are eliminated which means that communities will "
                "be much easier to spot."
            )

with ThreeD_Network_Map:
    with st.container(border=True):
        st.title(":blue[3D] Network Map")
        st.subheader(":violet[Based on] Relevancy Network Graph")
        st.image(ThreeD_Network_Map_Graph)
        with st.expander("See explanation :point_down:"):
            st.write(
                "For every node, a position is generated randomly by choosing each of dim "
                "coordinates uniformly at random on the interval [0.0, 1.0). "
            )


with Relevancy_heatmap:
    with st.container(border=True):
        st.title(":blue[Relevancy] Heat Map")
        st.subheader(":violet[Based on] the :red[Most] Relevancy Values")
        fig_1 = px.density_heatmap(
            filtered_relevancy_valued_dict_2_df,
            text_auto=False,
            orientation="h",
            x=filtered_relevancy_valued_dict_2_df.index,
            color_continuous_scale="reds",
        )
        fig_2 = px.imshow(
            filtered_relevancy_valued_dict_2_df,
            text_auto=True,
            color_continuous_scale="reds",
        )
    tab1, tab2 = st.tabs(["Adjacency Matrix", "Relevance Values Vector"])
    with tab1:
        st.plotly_chart(fig_1, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig_2, theme="streamlit", use_container_width=True)

        with st.expander("See explanation :point_down:"):
            st.write(
                "The Relevancy Heat Map shows the most relevant "
                "results according to the other results. You will "
                "realize that as you are reaching the greater value of relevancy "
                "the color of the result in heat map will be more denser . "
            )


with st.container(border=True):
    st.title(":blue[Relevant Results] Links")
    st.subheader(":violet[Based on] the :red[most High] Relevancy Values")
    st.dataframe(filtered_relevancy_valued_dict_2_links_data_df)

with st.container(border=True):
    st.title(":blue[All Results] Links")
    st.subheader(":violet[Based on] :red[Google] Relevant Results")
    st.dataframe(organic_results_df)
