from selectolax.parser import Node

def parse_raw_attributes(node: Node, selectors: list):
    # What are we doing here exactly? 
    # Getting as input a div node +
    # The list of selectors (from config) 
    # we pass to extract each attr we want: title, category, etc.

    # Declare our return dict that will contain all attributes for a particular div
    parsed = {}

    for s in selectors:
        match = s.get("match")
        type_ = s.get("type")
        selector = s.get("selector")
        name = s.get("name")

        if match == "all":
            matched = node.css(selector)

            if type_ == "text":
                parsed[name] = [node.text() for node in matched]
            elif type_ == "node":
                parsed[name] = matched
        
        elif match == "first":
            matched = node.css_first(selector)

            if type_ == "text":
                parsed[name] = matched.text()
            elif type_ == "node":
                parsed[name] = matched

    return parsed
    