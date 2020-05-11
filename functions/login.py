from functions.browser import *
from functions.functions import *


def login_to_site(filename, session_id, executor_url):
    filename = os.path.join("logins", filename)
    logininfo = read_ini_as_dict(filename)

    url = logininfo['login']['login_url']
    user_x_path = logininfo['login']['user_x_path']
    username = logininfo['login']['username']
    pass_x_path = logininfo['login']['pass_x_path']
    password = logininfo['login']['password']
    login_button = logininfo['login']['login_button']

    bro = attach_to_session(executor_url, session_id)
    bro.get(url)

    # Entering username
    bro.find_element_by_xpath(user_x_path).send_keys(username)
    time.sleep(1)

    # Entering password
    bro.find_element_by_xpath(pass_x_path).send_keys(password)
    time.sleep(1)

    # Clicking the login button
    bro.find_element_by_xpath(login_button).click()
    time.sleep(1)