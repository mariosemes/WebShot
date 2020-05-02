import configparser


class MyParser(configparser.ConfigParser):
    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d


f = MyParser()
f.read("settings.ini")
resolution = f.as_dict()

def get_list_keys(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

print(get_list_keys(resolution))

list = []
for r in resolution:
    list.append(resolution[r])
print(list)

# reslist = []
# for r in desktop_resolution:
#     print(r)
#     print(desktop_resolution[r])
#     #desktop_w, desktop_h = desktop_resolution[r].split("x")
#     #print("Desktop width: " + desktop_w)
#     #print("Desktop height: " + desktop_h)
#     reslist.append(desktop_resolution[r])
#
# print(", ".join(reslist))
