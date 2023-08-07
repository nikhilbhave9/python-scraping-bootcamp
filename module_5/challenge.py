# 1st page - title, price as float and rating as int
# data should be stored in a list of dictionaries

import requests as r 
from bs4 import BeautifulSoup as bs

resp = r.get("https://books.toscrape.com/")
soup = bs(resp.content, "html.parser")

# Result list
result = []

# Extract the product pods 
product_pods = soup.find_all("article", attrs={"class": "product_pod"})

print(type(product_pods))