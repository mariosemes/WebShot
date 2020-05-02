import configparser
import time

class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

def create_settings_file(path):
    print("Creating settings.ini file.")
    f = open("settings.ini", "w+")
    f.write("[settings]\n")
    f.write("chromepath = " + str(path) + "\n")
    f.close()

try:
    with open('settings.ini') as f:
        print("Settings file exists.")
        f = MyParser()
        f.read("settings.ini")
        path = f.as_dict()
except FileNotFoundError:
    print("Settings file does not exists.")
    chromedriverpath = input("Please type your Chromedriver path folder: ")
    create_settings_file(chromedriverpath)
    time.sleep(3)
    print("Checking if the file is created.")
    f = MyParser()
    f.read("settings.ini")
    path = f.as_dict()

print(path["settings"]["chromepath"])


