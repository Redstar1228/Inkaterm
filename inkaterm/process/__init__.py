from inkaterm.procces.reader import ppm
from termcolor import colored
import time

def main(file, char, same):
    theImage = ""
    x = []
    line = """
    """
    img = ppm(file)
    for i in img:
        r = int(i[0])
        g = int(i[1])
        b = int(i[2])
        if r < 45 and g < 45 and b < 45:
            n = "black"
        elif r > g and b > g and b > 100 and r > 100 and (r - g > 60 or b - g > 60):
            n = "magenta"
        elif r < g and b > 40:
            if b < 100:
                n = "blue"
            else:
                n = "cyan"
        elif g > b and g > r and g > 40 and g < 256:
            n = "green"
        elif r > b and r > g and r > 60 and r < 256 and g < 50:
            n = "red"
        elif (r - g < 80 or g - r > -80) and b < 100 and g > 60:
            n = "yellow"
        elif r > 44 and g > 44 and b > 40 and r < 201 and g < 201 and b < 201:
            n = "dark_grey"
        else:
            n = "white"
        x.append(colored(char, n, on_color = f"on_{n}" if same else None))
    z = 0
    y = ppm(file, "size").split()
    for row in range(int(y[1])):
        for col in range(int(y[0])):
            theImage += x[z]
            z += 1
            time.sleep(0.00000001)
        theImage += "\n"
    return theImage
