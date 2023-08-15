# Contains all of our extraction logic
from playwright.sync_api import sync_playwright

def extract_full_body_html(from_url):
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(from_url)

        # page.screenshot(path="steam.png", full_page=True)

        # How to ensure that the full page is loaded before the screenshot

        page.wait_for_load_state("networkidle") 
        # page.screenshot(path="steam.png", full_page=True)

        # However, the page doesn't load everything at once (for performance reasons)

        page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
        page.screenshot(path="steam2.png", full_page=True)
        page.wait_for_load_state("domcontentloaded")  # ADD AN EXTRA CHECK TO MAKE SURE EVERYTHING ON THE PAGE IS LOADED
        # page.wait_for_load_state('div[class*="salepreviewxyz"]') # MORE FLEXIBLE, ALLOWS FOR WAITING TILL A SPECIFIC ELEMENT IS LOADED 

        # -----------------------------------
        # Now that the work of the automation tool is done, we proceed with parsing
        
        html = page.inner_html("body")

        return html