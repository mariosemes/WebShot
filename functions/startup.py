import time

def create_settings_file():
    print("Creating settings.ini file.")
    f = open("settings.ini", "w+")
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


def startup_check():
    try:
        with open('settings.ini') as f:
            print("Settings file exists.")
    except FileNotFoundError:
        print("Settings file does not exists.")
        create_settings_file()
        time.sleep(3)
        print("Checking if the file is created.")
        startup_check()