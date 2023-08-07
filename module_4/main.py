# REQUESTS --> Higher level library 
import requests

url = "http://quotes.toscrape.com"
resp = requests.get(url)  
# print(resp)
# print(resp.headers)


# from urllib.request import urlopen

# url = "http://quotes.toscrape.com"
# resp = urlopen(url)
# print(resp.read().decode("utf-8"))
