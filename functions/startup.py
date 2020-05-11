import time
import configparser
import os.path
from sys import platform
from functions.chromiumdler import *

def create_resolutions_file():
    print("Creating resolutions.ini file.")
    f = open("resolutions.ini", "w+")
    f.write("[desktop]\n")
    f.write("Full HD = 1920x1080\n")
    f.write("Laptop 17 = 1536x864\n")
    f.write("Laptop 15 = 1600x900\n")
    f.write("Laptop with HiDPI screen = 1440x900\n")
    f.write("Laptop 13 = 1366x768\n")
    f.write("Laptop with MDPI screen = 1440x900\n")
    f.write("\n")
    f.write("[tablet]\n")
    f.write("iPad Mini = 768x1024\n")
    f.write("iPad Pro 10 = 834x1112\n")
    f.write("iPad Pro 12.9 = 1024x1366\n")
    f.write("Samsung Galaxy Tab 2 = 800x1280\n")
    f.write("iPad Mini Landscape = 1024x768\n")
    f.write("iPad Pro 10 Landscape = 1112x834\n")
    f.write("iPad Pro 12.9 Landscape = 1366x1024\n")
    f.write("Samsung Galaxy Tab 2 Landscape = 1280x800\n")
    f.write("\n")
    f.write("[mobile]\n")
    f.write("Samsung Galaxy S7 = 360x640\n")
    f.write("Samsung Galaxy Note8 = 414x846\n")
    f.write("Samsung Galaxy S9 = 360x740\n")
    f.write("iPhone 5 = 320x568\n")
    f.write("iPhone 7 / 8 = 375x667\n")
    f.write("iPhone 6Plus / 6S Plus = 414x736\n")
    f.write("iPhone Xs = 375x812\n")
    f.close()


def create_login_ini(filename):
    try:
        os.mkdir("logins")
    except OSError:
        print("Creation of the directory %s failed" % path)

    file = os.path.join("logins", filename)
    file = file + ".ini"
    print(f"Creating {filename}.ini file.")
    f = open(file, "w+")
    f.write("[login]\n")
    f.write("login_url = \n")
    f.write("user_x_path = \n")
    f.write("username = \n")
    f.write("pass_x_path = \n")
    f.write("password = \n")
    f.write("login_button = \n")
    f.close()

    if platform == "linux" or platform == "linux2":
        os.system('xdg-open "%s"' % file)
    elif platform == "darwin":
        os.system('open "%s"' % file)
    elif platform == "win32":
        os.startfile(file)


def startup_check():
    if platform == "win32":
        if path.exists("chromedriver.exe"):
            print("ChromeDriver exists.")
        else:
            chromium_downloader()

    try:
        with open('resolutions.ini') as f:
            print("Resolution file exists.")
    except FileNotFoundError:
        print("Resolution file does not exists.")
        create_resolutions_file()
        time.sleep(3)
        print("Restart the app.")
        time.sleep(3)
        exit()


