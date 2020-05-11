import os.path
import validators
from colorama import Fore, Back, Style
from colorama import init
from alive_progress import alive_bar, config_handler
from functions.startup import *
from functions.browser import *
from version import *

# use Colorama to make Termcolor work on Windows too
init()


class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d


f = MyParser()
f.read("resolutions.ini")
resolution = f.as_dict()


# Function to clean the screen in the CMD or TERMINAL
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_list_keys(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list


def list_resolution(webplatform):
    list = []
    for r in resolution[webplatform]:
        list.append(resolution[webplatform][r])
    return str(", ".join(list))


# The Welcome screen of the APP
def welcome_screen():
    clean_screen()
    webplatforms = get_list_keys(resolution)

    print("|")
    print("| " + Back.RED + "Welcome to WebShot [Website ScreenShot Tool for Frontend developers]." + Style.RESET_ALL)
    print("| Version " + get_version() + " | Licence GNU GPLv3")
    print("|")
    print("| " + Back.RED + "How to use:" + Style.RESET_ALL)
    print("| ""Paste or enter URL when asked and just wait until the app closes.")
    print("| ""When the job has finished, you should find a folder named as the domain of your")
    print("| ""given URL in the same directory where your UXTool.exe is. Have Fun!")
    print("|")
    print("| " + Back.RED + "Export resolutions" + Style.RESET_ALL)
    for web in webplatforms:
        print("| " + Back.RED + web + Style.RESET_ALL + " " + list_resolution(web))
    print("|")
    print("| " + Back.GREEN + "Let's get started!" + Style.RESET_ALL)


# Creating the folder name out of the domain
def get_folder_name(url):
    domainname = url.split("//")[-1].split("/")[0].split('?')[0].replace('www.', '')
    fullname = url.replace('https://', '').replace('/', '-').replace('www.', '').replace(domainname, '')[1:]
    if fullname == "":
        fullname = "root"
    elif fullname[-1] == "-":
        fullname = fullname[:-1]
    return domainname, fullname


# Function that makes all of it happen
def open_site(url, device_platform, width, height, driver, session_id, executor_url):

    ob = Screenshot_Clipping.Screenshot()

    bro = attach_to_session(executor_url, session_id)
    bro.set_window_size(width, height)
    bro.get(url)

    print("|")
    print("| " + Back.GREEN + "Shooting in progress:" + Style.RESET_ALL)
    print("| Platform: " + Fore.GREEN + device_platform + Style.RESET_ALL)
    print("| Width: " + Fore.GREEN + str(width) + Style.RESET_ALL)
    print("| Height: " + Fore.GREEN + str(height) + Style.RESET_ALL)
    print("|")
    print(
        "| Actual " + Fore.GREEN + device_platform + Style.RESET_ALL + " size check: " + str(bro.get_window_size()))

    domainname, fullname = get_folder_name(url)

    # Getting Working Directory
    path = str(Path.home())
    folderpath = os.path.join(path, "Desktop", domainname, fullname, device_platform)

    try:
        os.makedirs(folderpath)
    except OSError:
        pass
    else:
        print("| Folder created Successfully")


    # Getting fullpage screenshot
    img_url = ob.full_Screenshot(driver, save_path=folderpath,
                                 image_name=device_platform + '-' + str(width) + "x" + str(height) + '.jpg')

    print("|")
    print("| " + Back.MAGENTA + device_platform + "-" + str(width) + "x" + str(
        height) + " File Exported:" + Style.RESET_ALL)
    print("| " + img_url)


# Function to check if the URL is full
def check_url(url):
    if "http" in url:
        # print("Valid URL.")
        return url
    else:
        # print("Short url, converting to full.")
        url = "https://" + url
        return url


# Function to check if the URL is Valid
def check_url_if_valid(url):
    valid = validators.url(check_url(url))
    if valid == True:
        return True
    else:
        return False


def start_script(url, driver, session_id, executor_url):
    config_handler.set_global(spinner='message_scrolling')
    items = range(20)

    with alive_bar(len(items), bar='bubbles') as bar:
        webplatforms = get_list_keys(resolution)
        for web in webplatforms:
            for r in resolution[web]:
                desktop_w, desktop_h = resolution[web][r].split("x")
                if check_url_if_valid(url):
                    open_site(check_url(url), web, desktop_w, desktop_h, driver, session_id, executor_url)
                    bar()
                else:
                    print("URL non existing.")
                    time.sleep(3)
                    kickstarter()

    # Opening the final folder
    path = str(Path.home())
    folderpath = os.path.join(path, "Desktop", get_folder_name(url))

    if platform == "linux" or platform == "linux2":
        os.system('xdg-open "%s"' % folderpath)
    elif platform == "darwin":
        os.system('open "%s"' % folderpath)
    elif platform == "win32":
        os.startfile(folderpath)

    # Closing the Browser session
    close_session(driver)


def kickstarter():
    startup_check()
    check_verion()
    welcome_screen()
    # starting browser session
    driver, session_id, executor_url = open_session()

    while True:
        print("| Options:")
        print("| 1) WebShot Single Url")
        print("| 2) WebShot Multiple Urls")
        # print("| 3) Something custom... incoming")

        u1_input = input("| Please select an option: ")
        if u1_input == "1":
            u2_input = input("| Paste or Enter URL: ")
            if u2_input == "":
                print("Missing url. Try again.")
            else:
                # Starting the Testing script
                start_script(u2_input, driver, session_id, executor_url)
                kickstarter()
        elif u1_input == "2":
            url_list = []
            while True:
                print("| Urls in list:")
                for item in url_list:
                    print("| " + item)
                print("|")
                u2_input = input("| Paste or Enter URL (type 'done' to finish or 'c' to cancel): ")
                if u2_input == "":
                    print("| Missing url. Try again.")
                elif u2_input.lower() == "done":
                    # Starting the Testing script
                    for url in url_list:
                        start_script(url, driver, session_id, executor_url)
                    kickstarter()
                elif u2_input.lower() == "c":
                    print("| Operation canceled.")
                    break
                else:
                    if check_url_if_valid(u2_input):
                        print("| URL Valid. Adding to list.")
                        url = check_url(u2_input)
                        url_list.append(url)
                    else:
                        print("| URL not valid, please check it again.")
                        continue

        # elif u1_input == "3":
        #     print("Third option selected")
        else:
            print("Nothing selected. Try again")
            continue
