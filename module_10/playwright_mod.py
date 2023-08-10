import requests as r
from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
import subprocess

def extract_full_body_html(url):
    # Use playwright here

    url = "https://www.usaspending.gov/agency/department-of-defense"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)



if __name__ == "__main__":
    extract_full_body_html("https://www.usaspending.gov/agency/department-of-defense") 
