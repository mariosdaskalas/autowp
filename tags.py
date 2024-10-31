import re
import random
from playwright.sync_api import Playwright, sync_playwright, expect
from basic import *

target = call_target()
username, password = call_credentials()

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
    page.goto(f"{target}/wp-admin/edit-tags.php?taxonomy=post_tag")
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill(f"wp_tag_{random.randint(1, 1000)}")
    page.get_by_role("button", name="Add New Tag").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
