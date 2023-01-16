"""
CP1404 - Practicals
"""

import wikipedia

user_search = input("Search: ")
while user_search != "":
    wiki_page = wikipedia.page(user_search)
    try:
        print("Title: " + wiki_page.title)
        print(wikipedia.summary(user_search))
        print("URL: " + wiki_page.url)
        user_search = input("Search: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        user_search = input("Search: ")