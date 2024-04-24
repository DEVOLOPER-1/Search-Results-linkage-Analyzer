# pip install google-search-results
from serpapi import GoogleSearch
import json
import statistics
import networkx as nx
import matplotlib.pyplot as plt
import os  # I imported this library to check in future for a file that contain api key if it's not found the user will enter api key and saved in running dir and in next runtime the script will extract token from saved file in same directory
from networkx.algorithms.community.centrality import girvan_newman

#I should make a condition to force the user to enter 3 words at least
# Create an instance of the class
User_Query = input("Enter your query: ")
while (
    User_Query == " " or User_Query is None or User_Query == "" or User_Query == "   "
):
    User_Query = input("Invalid !!  Enter your query: ")

params = {
    "engine": "google",
    "q": User_Query,
    "api_key": "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e",
}


search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(f"{organic_results}\n\n\n\n\n\n\n")


organic_results = results["organic_results"]

# Primitive Display for Results
for num, single_result in enumerate(organic_results):
    print(
        f"Result {num+1}: {single_result["title"]} , Position {single_result["position"]} "
    )
    print("____________________________________________________________")


# Making a list of all words in snippets to re-compare it with each value of snippet dict
the_all_words_of_tuples_of_snippets = []
for snippet in organic_results:
    for word_in_no_tuple in snippet["snippet"].lower().split(","):
        the_all_words_of_tuples_of_snippets.append(word_in_no_tuple)


# Making a dictionary with key as title and value as snippets
snippets_dict = {}
temp_list = []

for single_snippet in organic_results:
    key = single_snippet["title"]
    item_tuple = single_snippet["snippet"].lower().split(",")
    if key not in snippets_dict:
        snippets_dict[key] = item_tuple

    if key in snippets_dict:
        temp_list.extend(
            item_tuple
        )  # As I understand extend is for appending items with no making of iterations
        snippets_dict[key].extend(temp_list)

positions_dict = {}

for single_Position in organic_results:
    key = single_Position["title"]
    int_item = single_Position["position"]
    if key not in positions_dict:
        positions_dict[key] = int_item
        
# Converting positions dictionary into json
website_title_with_position = json.dumps(
    positions_dict, indent=4
)  # I found that the indent value is to better read the output if printed

# write the JSON string to a file
with open("website_title_with_position.json", "w") as f:
    f.write(website_title_with_position)
    print("Done")


x = 0
relevancy = 0
relevancy_values = []
relevancy_valued_dict = {}


#############################This Part should be revised###########################################################

# The process of comparison of each value of key with all values of other key
# And making a new dic with relevancy values by numbers

# for key_of_dict, tuple_value in snippets_dict.items():
#     for word in tuple_value:
#         for single_snippet in the_all_words_of_tuples_of_snippets:
#             if word == single_snippet:
#                 x += 1
#     relevancy = x - len(tuple_value)
#     relevancy_values.append(relevancy)
#     if key_of_dict not in relevancy_valued_dict:
#         if relevancy == 0:
#             relevancy_valued_dict[key_of_dict] = relevancy + 1
#         else:
#             relevancy_valued_dict[key_of_dict] = relevancy

# print(f"{relevancy_values}\n\n\n")
# print(relevancy_valued_dict)
# print("\n_____________________________________")
# print(relevancy_valued_dict.keys())
# print(snippets_dict.keys())
# for i in organic_results:
#     print("\n_____________________________________")
#     print((i["title"]))

###################################################################################

# # Converting organic_specific_results dictionary into json
# website_title_with_relevancy_values = json.dumps(
#     relevancy_valued_dict, indent=4
# )  # I found that the indent value is to better read the output if printed

# # write the JSON string to a file
# with open("website_title_with_relevancy_values.json", "w") as f:
#     f.write(website_title_with_relevancy_values)
#     print("Done")

###################################################################################
Total_TF = 0
TF_Values_tuple = []
relevancy_valued_dict_2 = {}
# Calculating TF
for single_snippet_tuple in snippets_dict.values():
    Total_TF = 0
    for single_statement in single_snippet_tuple:
        TF = round(
            (
                the_all_words_of_tuples_of_snippets.count((single_statement.lower()))
                / len(the_all_words_of_tuples_of_snippets)
            ),
            1,
        )
        Total_TF += TF  # Approximation of TF
    TF_Values_tuple.append(Total_TF)
print(the_all_words_of_tuples_of_snippets)

num_of_index = 0
for key, value in snippets_dict.items():  # we can put either .keys() or .items()
    temp_key = key
    
    if temp_key not in relevancy_valued_dict_2:
        relevancy_valued_dict_2[temp_key] = TF_Values_tuple[num_of_index]

    if temp_key in relevancy_valued_dict_2:
        relevancy_valued_dict_2[temp_key] += TF_Values_tuple[num_of_index]

    num_of_index += 1

#Applying multiple of inverse of position value to relevancy value to make it more relevant to priority results
for key, value in positions_dict.items():
    relevancy_valued_dict_2[key]*= (1/value)
    
print(relevancy_valued_dict_2)    
#######################################################
print(relevancy_valued_dict_2)    
# Converting organic_specific_results dictionary into json
website_title_with_relevancy_values_2 = json.dumps(
    relevancy_valued_dict_2, indent=4
)  # I found that the indent value is to better read the output if printed

# write the JSON string to a file
with open("website_title_with_relevancy_values_2.json", "w") as f:
    f.write(website_title_with_relevancy_values_2)
    print("Done")


print(len(TF_Values_tuple))


TF_Values_tuple_Mean = statistics.mean(TF_Values_tuple)
Treshold = TF_Values_tuple_Mean
print(Treshold)

# Making Network map
nodes_of_relevance_network = []
edges_of_relevance_network = []



for key, item in relevancy_valued_dict_2.items():
    if item > (Treshold * 0.5): #I have multiplied to apply more nodes into network map
        nodes_of_relevance_network.append(key)
        for other_key, other_item in relevancy_valued_dict_2.items():
            if other_item < Treshold:
                continue
            if key != other_key or other_key != key:
                edges_of_relevance_network.append((key, other_key))  


# Un-working logic code as I wanted to make it dynamic and display it in streamlit
# network_graph_dict = {}
# #Making Nodes and edges dictionary for network graph
# for single_node , single_edge in zip(nodes_of_relevance_network,edges_of_relevance_network):
#     if single_node not in network_graph_dict:
#         network_graph_dict[single_node] = single_edge

# #Converting it 2 json 2convert it into a dynamic network map
# with open("network_graph_dict.json", "w") as f:
#     f.write(json.dumps(network_graph_dict, indent=4))


G = nx.Graph()

G.add_nodes_from(nodes_of_relevance_network)
G.add_edges_from(edges_of_relevance_network)
plt.title("Relevant Nodes Graph")
nx.draw(
    G,
    with_labels=True,
    node_shape="o",
    node_color="white",
    node_size=2000,
    font_color="black",
    width=5,
    style="solid",
    edge_color="darkred",
    font_size=10,
)


plt.axis("off")
# plt.show()
plt.savefig("Network Graph.jpeg", format="JPEG", bbox_inches="tight", dpi=1900)


# Calculating Degree Centrality
degree_centrality = nx.degree_centrality(G)

# print(degree_centrality)
with open("degree_centrality_of_network.json", "w") as f:
    f.write(json.dumps(degree_centrality, indent=4))


# Calculating Betweenness centrality 
betweenness_centrality = nx.betweenness_centrality(G)
with open("betweenness_centrality_of_network.json", "w") as f:
    f.write(json.dumps(betweenness_centrality, indent=4))


# Calculating Community clustering by Girvan_Newman
Girvan_Newman = girvan_newman(G , most_valuable_edge = None)
plt.savefig("Girvan_Newman.jpeg", format="JPEG", bbox_inches="tight", dpi=1900)


#Heat Mapping











# Launching Dashboard
os.system('cmd /c "streamlit run Parent_DashBoard.py"')
