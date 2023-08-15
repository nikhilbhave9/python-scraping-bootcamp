from datetime import datetime
import re
from selectolax.parser import Node
import pandas as pd

def get_attrs_from_node(node: Node, attr: str):
    if node is None or not issubclass(Node, type(node)):
        raise ValueError("The function expects a selectolax node to be provided")
    
    return node.attributes.get(attr)

def get_first_n(input_list: list, n: int = 5):
    return input_list[:n]

def reformat_date(rdate: str, input_format: str = '%b %d, %Y', output_format: str = '%Y-%m-%d'):
    dt_obj = datetime.strptime(rdate, input_format)
    return datetime.strftime(dt_obj, output_format)

def regex(input_str: str, pattern: str, task: str = "findall"):
    if task == "findall":
        return re.findall(pattern, input_str)
    elif task == "split":
        return re.split(pattern, input_str)
    else: 
        raise ValueError("ERROR")
    



def format_dict(attrs: dict):
    
    transforms = {
        "thumbnail": lambda n: get_attrs_from_node(n, "src"),
        "category": lambda input_list: get_first_n(input_list, 5),
        "date": lambda rdate: reformat_date(rdate, '%b %d, %Y', '%Y-%m-%d'),
        "reviews": lambda raw: int(''.join(regex(raw, r'\d+', "findall"))),
        "currency": lambda raw: "₹",
        "originalprice": lambda raw: regex(raw, r'₹', "split")[1],
        "discountedprice": lambda raw: regex(raw, r'₹', "split")[1]
        

    }

    for k, v in transforms.items():
        if k in attrs:
            attrs[k] = v(attrs[k])

    return attrs

def save_to_disk(filename="extract", data: list[dict] = None):
    if data is None:
        raise ValueError("ERROR")
    
    df = pd.DataFrame(data)
    filename = f"{datetime.now().strftime('%Y_%m_%d')}_{filename}.csv"
    df.to_csv(filename, index=False)