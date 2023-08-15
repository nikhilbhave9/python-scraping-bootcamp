from utils.extract import extract_full_body_html
from utils.parse import parse_raw_attributes
from utils.process import format_dict, save_to_disk
from config.tools import get_config
from selectolax.parser import HTMLParser

if __name__ == "__main__":
    config = get_config()
    html = extract_full_body_html(from_url=config.get('url'))
    tree = HTMLParser(html)

    # print(tree.css("div.salepreviewwidgets_StoreSaleWidgetContainer_UlvFk")) # This is inflexible 
    game_divs = tree.css('div[class*="salepreviewwidgets_StoreSaleWidgetContainer"]')

    # Declare a list of dicts for the results 
    list_of_games = []


    for game_div in game_divs:

        # Get title
        # To obtain title, we have to get the selector from items array and feed it to parse_raw_attributes 
        get_title = parse_raw_attributes(game_div, config.get('item'))
        # Do the same for everything
        game_attrs = parse_raw_attributes(game_div, config.get('item'))
        
        # ------------------------------------------------------------
        # Post-processing
        # ------------------------------------------------------------

        # title --> Nothing
        # thumbnail --> src
        # tags  --> First 5
        # date --> Convert to date type
        # reviews --> Only integer
        # currency --> Extract first part
        # prices --> Inetger and extract second part

        # ------------------------------------------------------------

        game_attrs_transformed = format_dict(game_attrs)
        list_of_games.append(game_attrs_transformed)

        # ------------------------------------------------------------

        # # Get title
        # game_div_title = game_div.css_first('div[class*="salepreviewwidgets_StoreSaleWidgetTitle"]').text()
        # print(game_div_title)

        # # Get thumbnail link
        # game_div_img = game_div.css_first('img[class*="salepreviewwidgets_CapsuleImage"]').attrs["src"]
        # print(game_div_img)

        # # Get category tags 
        # category_div = game_div.css('a[class*="salepreviewwidgets_Tag"]')
        # game_div_tags = []
        # for a in category_div:
        #     game_div_tags.append(a.text())
        # print(game_div_tags)

        # # Get release date (and convert to date format)
        # game_div_date = game_div.css_first('div[class*="WidgetReleaseDateAndPlatformCtn"]').text()
        # print(game_div_date)

        # # Get number of reviews (and convert to integer format)
        # game_div_reviews = game_div.css_first('div[class*="ReviewScoreCount"]').text() # Why is this working even if it is is a parent container 
        # print(game_div_reviews)

        # # Get original price
        # game_div_price_old = game_div.css_first('div[class*="StoreOriginalPrice"]').text()
        # print(game_div_price_old)

        # # Get discounted price
        # game_div_price_new = game_div.css_first('div[class*="StoreSalePriceBox"]').text()
        # print(game_div_price_new)

        # # Calculate discount percentage
        # print(" ")

        # # Populate dictionary and append to list 
        # game = {
        #     'title': game_div_title,
        #     'thumbnail': game_div_img,
        #     'categories': game_div_tags,
        #     'release_date': game_div_date,
        #     'reviews': game_div_reviews,
        #     'og_price': None,
        #     'new_price': None
        # }

    save_to_disk("extract", list_of_games)


