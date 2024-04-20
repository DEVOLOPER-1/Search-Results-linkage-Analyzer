#pip install google-search-results
from serpapi import GoogleSearch

User_Query = input("Enter your query: ")
while(User_Query == ""):
    User_Query = input("Invalid !!  Enter your query: ")

params = {
    "engine": "google",
    "q": User_Query ,
    "api_key": "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
#print(organic_results)
for num , single_result in enumerate(organic_results):
    print(f"Result {num+1}: {single_result["title"]} , Position {single_result["position"]} ")
    print("____________________________________________________________")