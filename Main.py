# pip install google-search-results
from serpapi import GoogleSearch
import json

User_Query = input("Enter your query: ")
while User_Query == " " or User_Query is None:
    User_Query = input("Invalid !!  Enter your query: ")

#params = {
    #"engine": "google",
    #"q": User_Query,
    #"api_key": "714b25eb147b43b3885fabb755c6a3682a48533965aaa15ed6b2a8492aff3a8e",
#}


#search = GoogleSearch(params)
#results = search.get_dict()
#organic_results = results["organic_results"]
#print(f"{organic_results}\n\n\n\n\n\n\n")
#organic_specific_results = {}
#positions = []
#titles = []
organic_results = [{'position': 1, 'title': 'Google', 'link': 'https://www.google.com/', 'redirect_link': 'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.google.com/&ved=2ahUKEwj8hcbXq9KFAxVV4ckDHd2UDAEQFnoECAYQAQ', 'displayed_link': 'https://www.google.com', 'favicon': 'https://serpapi.com/searches/662484c518ca86b75f96a2ac/images/5de156c0b2334c8f4dced513da6bc8772a367b858c53d9c777d7bfb2d563ae90.png', 'snippet': "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...", 'snippet_highlighted_words': ['Google'], 'sitelinks': {'expanded': [{'title': 'Images', 'link': 'https://images.google.com/', 'snippet': 'Google Images. The most comprehensive image search ...'}, {'title': 'News', 'link': 'https://news.google.com/', 'snippet': 'Comprehensive up-to-date news coverage, aggregated from ...'}, {'title': 'Account', 'link': 'https://www.google.com/account/about/', 'snippet': 'Your Google Account makes every service you use personalized to ...'}, {'title': 'Google Maps', 'link': 'https://maps.google.com/', 'snippet': 'Find local businesses, view maps and get driving directions in ...'}, {'title': 'Flights', 'link': 'https://www.google.com/travel/flights', 'snippet': 'Use Google Flights to explore cheap flights to anywhere ...'}]}, 'source': 'Google'}, {'position': 2, 'title': 'Google - About Google, Our Culture & Company News', 'link': 'https://about.google/', 'redirect_link': 'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://about.google/&ved=2ahUKEwj8hcbXq9KFAxVV4ckDHd2UDAEQFnoECDIQAQ', 'displayed_link': 'https://about.google', 'favicon': 'https://serpapi.com/searches/662484c518ca86b75f96a2ac/images/5de156c0b2334c8f4dced513da6bc877aefbebde57cd0c55f167716547971a80.png', 'snippet': 'Stay up to date with Google company news and products. Discover stories about our culture, philosophy, and how Google technology is impacting others.', 'snippet_highlighted_words': ['Google', 'Google'], 'sitelinks': {'inline': [{'title': 'Products', 'link': 'https://about.google/products/'}, {'title': "All of Google's Products", 'link': 'https://about.google/intl/ALL_us/products/'}, {'title': 'Women - Google', 'link': 'https://about.google/stories/accelerating-equity-for-women/'}, {'title': 'About Google, Our Culture...', 'link': 'https://about.google/intl/ALL_in/'}]}, 'source': 'About Google'}, {'position': 3, 'title': 'The Keyword | Google Product and Technology News and ...', 'link': 'https://blog.google/', 'redirect_link': 'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://blog.google/&ved=2ahUKEwj8hcbXq9KFAxVV4ckDHd2UDAEQFnoECDEQAQ', 'displayed_link': 'https://blog.google', 'favicon': 'https://serpapi.com/searches/662484c518ca86b75f96a2ac/images/5de156c0b2334c8f4dced513da6bc87768df7c3ab0416ff82fe7fcf3c3f8d9e7.png', 'snippet': "Get the latest news and stories about Google products, technology and innovation on the Keyword, Google's official blog.", 'snippet_highlighted_words': ['Google', "Google's"], 'source': 'Google Blog'}, {'position': 4, 'title': "Browse All of Google's Products & Services", 'link': 'https://about.google/intl/ALL_us/products/', 'redirect_link': 'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://about.google/intl/ALL_us/products/&ved=2ahUKEwj8hcbXq9KFAxVV4ckDHd2UDAEQFnoECCoQAQ', 'displayed_link': 'https://about.google › intl › ALL_us › products', 'favicon': 'https://serpapi.com/searches/662484c518ca86b75f96a2ac/images/5de156c0b2334c8f4dced513da6bc877ab8e99f81fa8cd38594d0a0862e6bb25.png', 'snippet': 'Browse a list of Google products designed to help you work and play, stay organized, get answers, keep in touch, grow your business, and more.', 'snippet_highlighted_words': ['Google'], 'source': 'About Google'}, {'position': 5, 'title': 'Google', 'link': 'https://en.wikipedia.org/wiki/Google', 'redirect_link': 'https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://en.wikipedia.org/wiki/Google&ved=2ahUKEwj8hcbXq9KFAxVV4ckDHd2UDAEQFnoECCsQAQ', 'displayed_link': 'https://en.wikipedia.org › wiki › Google', 'favicon': 'https://serpapi.com/searches/662484c518ca86b75f96a2ac/images/5de156c0b2334c8f4dced513da6bc877bdc30c97b88e377bbe062227e608f9fe.png', 'snippet': 'Google LLC is an American multinational corporation and technology company focusing on online advertising, search engine technology, cloud computing, ...', 'snippet_highlighted_words': ['Google'], 'sitelinks': {'inline': [{'title': 'History', 'link': 'https://en.wikipedia.org/wiki/History_of_Google'}, {'title': 'Google Search', 'link': 'https://en.wikipedia.org/wiki/Google_Search'}, {'title': 'Google Chrome', 'link': 'https://en.wikipedia.org/wiki/Google_Chrome'}, {'title': 'Google Pixel', 'link': 'https://en.wikipedia.org/wiki/Google_Pixel'}]}, 'source': 'Wikipedia'}]

# Primitive Display for Results
for num, single_result in enumerate(organic_results):
    print(
        f"Result {num+1}: {single_result["title"]} , Position {single_result["position"]} "
    )
    print("____________________________________________________________")

# Appending specified results to an empty lists
# I made the  ###  as  a delimiter to extract the values of json file correctly
#for single_result in organic_results:
#    titles.append(f"{single_result["title"]}")
#    positions.append(f"{single_result["position"]}")

# Assigning the list of needed only results values  in the dictionary for json load
#organic_specific_results["Website_Name"] = titles
#organic_specific_results["Position_Priority"] = positions

#print(organic_specific_results)

#Making a list of all words in snippets to re-compare it with each value of sinppet dict
the_all_words_of_tuples_of_snippets = []
for snippet in organic_results:
    for word_in_no_tuple in snippet["snippet"].lower().split(","):
        the_all_words_of_tuples_of_snippets.append(word_in_no_tuple)

#Making a dictionary with key as title and value as snippets
snippets_dict = {}
temp_list = []

for single_snippet in organic_results:
        key = single_snippet["title"]
        item = single_snippet["snippet"].lower().split(",")
        #for element in snippets_dict:
        #if key not in snippets_dict:
        snippets_dict[key] = item
        #else: #Optional condition
            #continue   
x = 0        
relevancy = 0
relevancy_values = []
relevancy_valued_dict = {}

print(the_all_words_of_tuples_of_snippets)
#The process of comparison of each value of key with all values of other key
#And making a new dic with relevancy values by numbers

for key_of_dict, tuple_value in snippets_dict.items():
    for word in tuple_value:
        for single_snippet in the_all_words_of_tuples_of_snippets:
            if word == single_snippet:
                x += 1
    relevancy = x - len(tuple_value)
    relevancy_values.append(relevancy)
    if key_of_dict not in relevancy_valued_dict:
        if relevancy == 0:
            relevancy_valued_dict[key_of_dict] = (relevancy+1)
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
# json_object_organic_specific_results = json.dumps(
#     organic_specific_results, indent=4
# )  # I found that the indent value is to better read the output if printed
# print(json_object_organic_specific_results)
# # write the JSON string to a file
# with open('organic_specific_results_with_no_ctr.json', 'w') as f:
#     f.write(json_object_organic_specific_results)
#     print("Done")