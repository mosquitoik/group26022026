import requests
from pprint import pprint  #can be removed

url = 'https://dummyjson.com/posts'
response = requests.get(url=url)
# print(response.content)
# print(response.text)
pprint(response.json(), indent=4)   #pprint, indent=4 - can be removed if the site html or js not json

# print('dfgvbhjfq\nkygdfhqvjhfdfh\nkechgjfr')
# print("""nbhg""")