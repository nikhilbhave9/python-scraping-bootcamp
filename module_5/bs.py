import requests as r 
from bs4 import BeautifulSoup as bs

resp = r.get("https://books.toscrape.com/")
soup = bs(resp.content, "html.parser")

first_div = soup.div
# print(first_div)

first_ul = soup.ul
# print(list(first_ul.children))
# for child in first_ul.children:
#     print(child)


# Getting Text 
print(soup.ul.get_text()) # .string returns only THAT attribute, not its children
print(soup.ul.text) # this is the non-functional form of .get_text()
print(soup.ul.get_text(separator=", ", strip=True))

print(len(soup.find_all())) # Len = 541, but what all is included in this?
# Includes all the elements such as <html>, <head>, <body>, etc.
print(len(soup.find_all(["a", "div"])))

# We want to get prices 
# the prices are in a <p> tag with class "price_color"
price_tags = soup.find_all("p", attrs={"class": "price_color"})
price_tags_text = [price.get_text() for price in price_tags]
print(price_tags_text)


