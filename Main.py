# pip install google-search-results
from serpapi import GoogleSearch
import json

User_Query = input("Enter your query: ")
while User_Query == "" or User_Query is None:
    User_Query = input("Invalid !!  Enter your query: ")

params = {
    "engine": "google",
    "q": User_Query,
    "api_key": "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e",
}


search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]

organic_specific_results = {}
positions = []
titles = []


# Primitive Display for Results
for num, single_result in enumerate(organic_results):
    print(
        f"Result {num+1}: {single_result["title"]} , Position {single_result["position"]} "
    )
    print("____________________________________________________________")

# Appending specified results to an empty lists
for single_result in organic_results:
    titles.append(single_result["title"])
    positions.append(single_result["position"])

# Assigning the list of needed only results values  in the dictionary for json load
organic_specific_results["Website_Name"] = titles
organic_specific_results["Position_Priority"] = positions

print(organic_specific_results)

# Converting organic_specific_results dictionary into json
json_object = json.dumps(
    organic_specific_results, indent=4
)  # I found that the indent value is to better read the output if printed
print(json_object)