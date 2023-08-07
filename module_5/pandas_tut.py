# Extracted strings from data, now what? 
# Go from list of dictionaries to a pandas dataframe

import pandas as pd 

list_of_books = [
    {
        "title": "ABC",
        "price": 3,
        "rating": 2
    }, 
    {
        "title": "XYZ",
        "price": 50,
        "rating": 5
    }, 
    {
        "title": "Inferno",
        "price": 1,
        "rating": 1
    }, 

]

# Creating dataframes
df = pd.DataFrame(list_of_books)
print(df)
print(df.price.mean())