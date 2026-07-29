import json
import os

import pytest
from playwright.sync_api import Browser, Page, Playwright



#Not in use - there is better way to use the credential as data - its relevant for test_framework_api_cred_by_fixture_NOT_USE.py - the Udemy course solution
# @pytest.fixture(scope="session") #run for one execution
# def user_credential_fxtr(request): #request - pytest global variable
#     return request.param



#every parameterized test gets a new browser and new context and page.
#in case scope="session" the test will failed because its running in 2 iteration ( different users ) fo on the sec time the chromium_setup will not run
# @pytest.fixture(scope="function")
# def chromium_setup (playwright:Playwright):
#     my_browser = playwright.chromium.launch(headless=False)
#     my_context = my_browser.new_context()
#     my_page = my_context.new_page()
#
#     yield my_page #return my_page
#     my_context.close()
#     my_browser.close()


with open('data/execution_data.json') as _execution_data_file:
    execution_data = json.load(_execution_data_file)

    
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default=execution_data["browser"], help="my option: chrome or firefox"
    )
    parser.addoption(
        "--url", action="store", default=execution_data["application_url"], help="application url"
    )

#A more efficient structure reuses the browser but creates a fresh context per test:
@pytest.fixture(scope="session")
def browser_setup(playwright: Playwright,request): # request gives access to global variables
    browser = playwright.chromium.launch(headless=False)

    browser_name=request.config.getoption("--browser_name")  #get the arg from the command line : pytest -s test_e2e_framework_web_api.py --headed --browser_name firefox
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        browser = playwright.firefox.launch(headless=False)

    yield browser

    browser.close()


#new context for each test
@pytest.fixture(scope="function")
def context_setup(browser_setup: Browser,request) :
    url = request.config.getoption("--url")
    context = browser_setup.new_context()
    page = context.new_page()
    page.goto(url)
    yield page

    context.close()
