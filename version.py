import urllib.request


def get_version():
    version_file = open(r"version.txt", "r")
    version = version_file.readline()
    version_file.close()
    version = str(version)
    return version


def get_web_version():
    target_url = "https://raw.githubusercontent.com/mariosemes/WebShot/master/version.txt"
    for line in urllib.request.urlopen(target_url):
        web_version = line.decode('utf-8')
    return web_version


def check_verion():
    current_ver = get_version()
    web_ver = get_web_version()
    print("| Checking for updates...")
    if web_ver > current_ver:
        print("| There is an update waiting. Please visit GITHUB and download the latest version.")
        print("| Visit: https://github.com/mariosemes/WebShot")
        print(f"| Version {web_ver} is available.")
    else:
        print("| App up-to-date.")
