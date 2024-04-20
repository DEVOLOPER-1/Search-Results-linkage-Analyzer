#pip install google-search-results
from serpapi import GoogleSearch
import json

User_Query = input("Enter your query: ")
while(User_Query == "" or User_Query is None):
    User_Query = input("Invalid !!  Enter your query: ")

params = {
    "engine": "google",
    "q": User_Query ,
    "api_key": "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e" ,
}


search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]

organic_specific_results = {}
positions = []
titles = []
#print(organic_results)
for num , single_result in enumerate(organic_results):
    print(f"Result {num+1}: {single_result["title"]} , Position {single_result["position"]} ")
    print("____________________________________________________________")

for single_result in organic_results:
    titles.append(single_result["title"])
    positions.append(single_result["position"])
    

organic_specific_results["Website_Name"] = titles
organic_specific_results["Position_Priority"] = positions

#parse_organic_results = json.loads()
print(organic_specific_results)