import os
import os.path
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from Screenshot import Screenshot_Clipping
from pathlib import Path
from sys import platform
from random import randint


# Controller for checking when the path is in the compiled version or in the raw one
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


# Function to open a new browser Session
def open_session():
    # Chromedriver path defined per OS - Linux not needed
    if platform == "darwin":
        chromedriver = "../utils/chromedriver"
    elif platform == "win32":
        chromedriver = "..\\utils\\chromedriver.exe"

    # Chromedriver options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    # Custom options for chromedriver for Linux
    if platform == "linux" or platform == "linux2":
        random_port = randint(9000, 9999)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=" + str(random_port))

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if platform == "linux" or platform == "linux2":
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome(executable_path=resource_path(chromedriver), options=options)

    executor_url = driver.command_executor._url
    session_id = driver.session_id
    return driver, session_id, executor_url


# Function to close the Session & Driver
def close_session(driver):
    driver.quit()


# Function to attach to an open Driver Session
def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)

    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id

    WebDriver.execute = original_execute
    return driver
