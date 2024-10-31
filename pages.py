import re
import random
from playwright.sync_api import Playwright, sync_playwright, expect
from basic import *

target = call_target()
username, password = call_credentials()

default_text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean in dolor volutpat ex accumsan fermentum. Quisque ornare ut mi vel mattis. Aenean vel elementum mi. Aliquam ultrices, metus sit amet malesuada rhoncus, metus orci semper sem, eget volutpat arcu ante et enim. Maecenas ut lacus placerat, mattis justo quis, suscipit ante. Maecenas a venenatis mi. In ultricies augue id dolor dignissim, id feugiat nulla rutrum. In hac habitasse platea dictumst. Curabitur suscipit hendrerit lorem. Pellentesque in arcu eu mauris viverra hendrerit. Proin ut vestibulum sapien.
'''

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.goto(f"{target}/wp-login.php")
    page.get_by_label("Username or Email Address").click()
    page.get_by_label("Username or Email Address").fill(username)
    page.get_by_label("Password", exact=True).click()
    page.get_by_label("Password", exact=True).fill(password)
    page.get_by_role("button", name="Log In").click()
    page.goto(f"{target}/wp-admin/post-new.php?post_type=page")
    page.get_by_label("Close", exact=True).click()
    page.get_by_label("Options", exact=True).click()
    page.get_by_role("button", name="Options", exact=True).click()
    page.get_by_label("Editor settings").get_by_role("heading", name="No Title").click()
    page.get_by_label("Actions").click()
    page.get_by_role("menuitem", name="Rename").click()
    page.get_by_label("Name", exact=True).click()
    page.get_by_label("Name", exact=True).fill(f"wp_title_{random.randint(1, 1000)}")
    page.get_by_role("button", name="Save").click()
    page.locator("iframe[name=\"editor-canvas\"]").content_frame.get_by_label("Add default block").click()
    page.locator("iframe[name=\"editor-canvas\"]").content_frame.get_by_label("Empty block; start writing or").fill(default_text)
    page.get_by_role("button", name="Publish", exact=True).click()
    page.get_by_label("Editor publish").get_by_role("button", name="Publish", exact=True).click()
    page.get_by_label("Editor publish").get_by_role("link", name="View Page").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
