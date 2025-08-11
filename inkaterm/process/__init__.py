from inkaterm.procces.reader import ppm
from termcolor import colored
from json import loads, dump
from hashlib import sha512
from datetime import datetime as time
import os
import importlib.resources as pkg
from .. import db

def main(file: str, char: any, same: bool, pro: dict):
    idb = loads(pkg.files(db).joinpath("idb.json").open("r", encoding="utf-8").read())
    key = sha512(pro["key"].strip().encode()).hexdigest()
    if pro["key"] == "None" or key in idb["license"].values():
        theImage = ""
        x = []
        line = """
        """
        name = ""
        for i in idb["license"]:
            if idb["license"][i] == key:
                name = i
        img = ppm(file)
        for i in img:
            r = int(i[0])
            g = int(i[1])
            b = int(i[2])
            if r < 45 and g < 45 and b < 45:
                n = "black"
            elif r > g and b > g and b > 100 and r > 100 and (r - g > 60 or b - g > 60):
                n = "magenta"
            elif r > 44 and g > 44 and b > 40 and r < 180 and g < 180 and b < 180 and (r - b < 26 or r - b > -26) and (b - g < 26 or b - g > -26) and (r - g < 26 or r - g > -26):
                n = "dark_grey"
            elif r < g and b > 40 and r - b < -30:
                if b < 100:
                    n = "blue"
                else:
                    n = "cyan"
            elif g > b and g > r and g > 40 and g - r > 60 and r + b < g:
                n = "green"
            elif r > b and r > g and r > 60 and g < 50:
                n = "red"
            elif (r - g < 80 or g - r > -80) and b < 100 and g > 100:
                n = "yellow"
            else:
                n = "white"
            x.append(colored(char, n, on_color = f"on_{n}" if same else None))
        z = 0
        y = ppm(file, "size").split()
        for row in range(int(y[1])):
            for col in range(int(y[0])):
                theImage += x[z]
                z += 1
            theImage += "\n"
        if key in idb["license"].values():
            if pro["report"]:
                details = {
                    "size": [y[0], y[1]],
                    "name": file,
                    "format": file.split(".")[-1]
                }
            
                if not os.path.exists(f"inkatermReports/{name}.json"):
                    os.mkdir("inkatermReports")
                    open(f"inkatermReports/{name}.json", "w").write("{}")
                file = loads(open(f"inkatermReports/{name}.json", "r").read())
                file[time.now().strftime("%Y:%m:%d:%H:%M:%S") + f":{time.now().microsecond // 1000:03d}"] = details
                dump(file, open(f"inkatermReports/{name}.json", "w"))
        return theImage
    else:
        print("invalid key\nif you don't have a pro key, you can buy now with lower than 1$ with any crypto!")
