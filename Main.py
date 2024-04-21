# pip install google-search-results
from serpapi import GoogleSearch
import json

User_Query = input("Enter your query: ")
while User_Query == " " or User_Query is None or User_Query == "":
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


x = 0
relevancy = 0
relevancy_values = []
relevancy_valued_dict = {}

# print(the_all_words_of_tuples_of_snippets)


# The process of comparison of each value of key with all values of other key
# And making a new dic with relevancy values by numbers

for key_of_dict, tuple_value in snippets_dict.items():
    for word in tuple_value:
        for single_snippet in the_all_words_of_tuples_of_snippets:
            if word == single_snippet:
                x += 1
    relevancy = x - len(tuple_value)
    relevancy_values.append(relevancy)
    if key_of_dict not in relevancy_valued_dict:
        if relevancy == 0:
            relevancy_valued_dict[key_of_dict] = relevancy + 1
        else:
            relevancy_valued_dict[key_of_dict] = relevancy

print(f"{relevancy_values}\n\n\n")
print(relevancy_valued_dict)
print("\n_____________________________________")
print(relevancy_valued_dict.keys())
print(snippets_dict.keys())
for i in organic_results:
    print("\n_____________________________________")
    print((i["title"]))


# Converting organic_specific_results dictionary into json
website_title_with_position = json.dumps(
    positions_dict, indent=4
)  # I found that the indent value is to better read the output if printed

# write the JSON string to a file
with open("website_title_with_position.json", "w") as f:
    f.write(website_title_with_position)
    print("Done")


# Converting organic_specific_results dictionary into json
website_title_with_relevancy_values = json.dumps(
    relevancy_valued_dict, indent=4
)  # I found that the indent value is to better read the output if printed

# write the JSON string to a file
with open("website_title_with_relevancy_values.json", "w") as f:
    f.write(website_title_with_relevancy_values)
    print("Done")



