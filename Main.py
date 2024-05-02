# pip install google-search-results
from serpapi import GoogleSearch
import json
import statistics
import networkx as nx
import matplotlib.pyplot as plt
import os  # I imported this library to check in future for a file that contain api key if it's not found the user will enter api key and saved in running dir and in next runtime the script will extract token from saved file in same directory
from networkx.algorithms.community.centrality import girvan_newman
import numpy as np
import PySimpleGUI as sg


# I should make a condition to force the user to enter 3 words at least

# All the stuff inside your window.
layout = [
    [sg.Text("Enter your Query", background_color="black", text_color="white")],
    [sg.InputText()],
    [sg.Text("Enter SERP API key", background_color="black", text_color="white")],
    [sg.InputText()],
    [
        sg.Button("Display Results in Dashboard", button_color="black"),
        sg.Button("Cancel", button_color="black"),
    ],
]

# Create the Window
sg.theme("DarkBlack")
window = sg.Window(
    "Search Results linkage Analyzer",
    layout,
    icon=r"C:\Users\moham\OneDrive\Desktop\DAQ-103 Project\GUI Resources\icons8-bar-chart-100.ico",
    resizable=True,
)

# Event Loop to process "events" and get the "values" of the inputs

event, values = window.read()

# if user closes window or clicks cancel
if event == sg.WIN_CLOSED or event == "Cancel":
    window.close()

print("Hello", values[1], "!")


serp_api_sample = "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e"

User_Query = values[0]
User_Api = values[1]
print(User_Query, User_Api)
while (
    User_Query == " "
    or User_Query is None
    or User_Query == ""
    or User_Query == "   "
    and event != "Cancel"
):
    User_Query = sg.popup_get_text(
        "Invalid Entry!! Please Enter Your Query",
        title="Invalid Query Entry",
        icon=r"C:\Users\moham\OneDrive\Desktop\DAQ-103 Project\GUI Resources\icons8-bar-chart-100.ico",
    )
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        window.close()
        break
while (len(User_Api) != len(serp_api_sample)) and event != "Cancel":
    User_Api = sg.popup_get_text(
        "Invalid Entry!! Please Enter Your API Key",
        title="Invalid SERP API Key Entry",
        icon=r"C:\Users\moham\OneDrive\Desktop\DAQ-103 Project\GUI Resources\icons8-bar-chart-100.ico",
    )
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        window.close()
        break

params = {"engine": "google", "q": User_Query, "api_key": User_Api}


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

# Applying multiple of inverse of position value to relevancy value to make it more relevant to priority results
for key, value in positions_dict.items():
    relevancy_valued_dict_2[key] *= 1 / value

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
    if item > (
        Treshold * 0.5
    ):  # I have multiplied to apply more nodes into network map
        nodes_of_relevance_network.append(key)

# Making Edges and appending them 2 edges_of_relevance_network
for single_node in nodes_of_relevance_network:
    for other_node in nodes_of_relevance_network:
        if single_node != other_node:
            edges_of_relevance_network.append((single_node, other_node))

# Un-working logic code as I wanted to make it dynamic and display it in streamlit
# network_graph_dict = {}
# #Making Nodes and edges dictionary for network graph
# for single_node , single_edge in zip(nodes_of_relevance_network,edges_of_relevance_network):
#     if single_node not in network_graph_dict:
#         network_graph_dict[single_node] = single_edge

# #Converting it 2 json 2convert it into a dynamic network map
# with open("network_graph_dict.json", "w") as f:
#     f.write(json.dumps(network_graph_dict, indent=4))


# Making a relevancy json file of most relevant results with their links
# 2 Display it in streamlit


relevant_results_with_links = {}
for key in relevancy_valued_dict_2.keys():
    for single_result in organic_results:
        if key == single_result["title"]:
            relevant_results_with_links[key] = single_result["link"]


with open("relevant_results_with_links.json", "w") as f:
    f.write(json.dumps(relevant_results_with_links, indent=4))


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
Girvan_Newman = girvan_newman(G, most_valuable_edge=None)
plt.title("Community Clustering by Girvan_Newman")
plt.savefig("Girvan_Newman.jpeg", format="JPEG", bbox_inches="tight", dpi=1900)


# Heat Mapping

x_axis_int_values = [num for num in range(len(relevancy_valued_dict_2.keys()))]
y_axis_values = [y for y in relevancy_valued_dict_2.values()]
print(x_axis_int_values)
x_axis_string_values = [str(key) for key in relevancy_valued_dict_2.keys()]


combined_Matrix = np.array([x_axis_int_values, y_axis_values]).T

fig = plt.figure("Heat Map of Relevancy Values")
ax = fig.add_subplot()
cat = ax.matshow(
    combined_Matrix, interpolation="bicubic"
)  # As I have tested interpolation  = nearest or bilinear or bicubic I saw the change in the gradiency of colors on heat map asit affects how colors are smoothed together
fig.colorbar(cat)
# ax.set_xticks(np.arange(len(x_axis_int_values)))
# ax.set_yticks(np.arange(len(y_axis_values)))
ax.set_xticklabels(x_axis_string_values, rotation=90, fontsize="x-small")
ax.set_yticklabels(y_axis_values, fontsize="x-small")
plt.savefig("Heatmap.jpeg", format="JPEG", bbox_inches="tight", dpi=1900)


# Making 3d graph map


# A layout is an algorithm to position nodes in a graph
#  #makes a 3D graph
# Layouts returns a dictionary , with each element
# being an array  of the form (node, [x, y, z]) in 3D space

# displaying 3D graph
fig2 = plt.figure()
ax2 = fig2.add_subplot(projection="3d")

# returns a dictionary of positions keyed by each node and the value of each key is [x,y,z]
x_y_z_position = nx.random_layout(G, dim=3)  # How does random layout work?

# converting each dictionary value into 1x3 array and appending it to a list
xyz = [list(i) for i in x_y_z_position.values()]  # output = [[x,y,z] , etc.]


##################Not working code  as i used it in ax.scatter(x = X , y = Y , z = Z)
# X = []
# Y = []
# Z = []
# print(xyz)
# for num_of_array , array in enumerate(xyz):
#     X.append(array[num_of_array][0])
#     Y.append(array[num_of_array][1])
#     Z.append(array[num_of_array][2])


# displaying 3D graph
# print(len(xyz))
# if len(xyz) > 0:
ax2.scatter(
    *zip(*xyz),
    c="darkred",  # color of marker
    s=50,  # size of marker
    marker="x",  # shape of marker
)

ax2.plot(*zip(*xyz), c="darkred")
ax2.title.set_text("3D Network Map Graph")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("Z")
# saving the 3D figure

# print("xyz is empty as the results description are not strongly relevant")
plt.savefig("3D Graph.jpeg", format="JPEG", bbox_inches="tight", dpi=1900)


# Launching Dashboard
if event == "Display Results in Dashboard":
    window.close()
    os.system('cmd /c "streamlit run Parent_DashBoard.py"')
