from inkaterm.procces.reader import ppm
from termcolor import colored
from datetime import datetime as time
from json import loads, dump
import os

def main(file: str, char: any, same: bool, report: bool) -> str:
    if True:
        name = "report"
        theImage = ""
        x = []
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
        if report:
            if True:
                details = {
                    "size": [y[0], y[1]],
                    "name": file,
                    "format": file.split(".")[-1]
                }
            
                if not os.path.exists("inkatermReports"):
                    os.mkdir("inkatermReports")
                if not os.path.exists(f"inkatermReports/{name}.json"):
                    open(f"inkatermReports/{name}.json", "w").write("{}")
                fil = loads(open(f"inkatermReports/{name}.json", "r").read())
                fil[time.now().strftime("%Y:%m:%d:%H:%M:%S") + f":{time.now().microsecond // 1000:03d}"] = details
                dump(fil, open(f"inkatermReports/{name}.json", "w"), sort_keys = True)
        return theImage      
