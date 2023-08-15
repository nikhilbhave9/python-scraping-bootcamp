import re

pattern = r'₹'
strg = "₹1233"

results = re.split(pattern, strg)
print(results)