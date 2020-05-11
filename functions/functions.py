import configparser
import glob

class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d


def read_ini_as_dict(filename):
    f = MyParser()
    f.read(filename)
    dictionary = f.as_dict()
    return dictionary


def list_all_ini():
    list = glob.glob("logins\*.ini")
    counter = 0
    for item in list:
        counter += 1
        print(f"| {counter}) {item[7:]}")
    return list


def select_ini_file(number):
    number = int(number) - 1
    list = glob.glob("logins\*.ini")
    list_item = list[int(number)]
    return list_item[7:]