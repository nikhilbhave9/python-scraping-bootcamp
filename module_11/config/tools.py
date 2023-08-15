import json

_config = {
    "url": "https://store.steampowered.com/specials", 
    "container": [
        {
            "name": "store_sale_divs",
            "selector": 'div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]',
            "match": "all",
            "type": "node"
        }
    ],
    "item": [
        {
            "name": "title",
            "selector": 'div[class*="salepreviewwidgets_StoreSaleWidgetTitle"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "thumbnail",
            "selector": 'img[class*="salepreviewwidgets_CapsuleImage"]',
            "match": "first",
            "type": "node"
        },
        {
            "name": "category",
            "selector": 'a[class*="salepreviewwidgets_Tag"]',
            "match": "all",
            "type": "text"
        },
        {
            "name": "date",
            "selector": 'div[class*="WidgetReleaseDateAndPlatformCtn"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "reviews",
            "selector": 'div[class*="ReviewScoreCount"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "currency",
            "selector": 'div[class*="StoreOriginalPrice"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "originalprice",
            "selector": 'div[class*="StoreOriginalPrice"]',
            "match": "first",
            "type": "text"
        },
        {
            "name": "discountedprice",
            "selector": 'div[class*="StoreSalePriceBox"]',
            "match": "first",
            "type": "text"
        }
        
    ]

}

def get_config(load_from_file=False):
    if load_from_file:
        with open("config.json", "r") as f:
            return json.load(f)    
    return _config

def generate_config():
    with open("config.json", "w") as f:
        json.dump(_config, f, indent=4)


if __name__ == '__main__':
    generate_config()