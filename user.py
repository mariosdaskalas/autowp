import re
import random
import string
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from basic import *

target = call_target()
username, password = call_credentials()

def generate_username():
    characters = string.ascii_letters + string.digits + '._-'
    username = ''.join(random.choice(characters) for _ in range(random.randint(5, 32)))
    return username

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
    page.goto(f"{target}/wp-admin/user-new.php")
    page.get_by_label("Username (required)").click()
    page.get_by_label("Username (required)").fill(generate_username())
    #page.get_by_label("Username (required)").press("Tab")
    page.get_by_label("Email (required)").click()
    page.get_by_label("Email (required)").fill(f"{generate_username()}@wp.local")
    page.get_by_label("First Name").click()
    page.get_by_label("First Name").fill(f"first_{generate_username()}")
    page.get_by_label("Last Name").click()
    page.get_by_label("Last Name").fill(f"last_{generate_username()}")
    page.get_by_label("Website").click()
    page.get_by_label("Website").fill("https://example.com/")
    page.get_by_label("Password (required)", exact=True).click()
    page.get_by_label("Password (required)", exact=True).press("ArrowRight")
    page.get_by_label("Password (required)", exact=True).fill("password")
    page.locator("td").filter(has_text="Confirm use of weak password").click()
    page.get_by_label("Confirm use of weak password").check()
    page.get_by_label("Send the new user an email").uncheck()
    page.get_by_label("Role").select_option("administrator")
    page.get_by_role("button", name="Add New User").click()
    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
