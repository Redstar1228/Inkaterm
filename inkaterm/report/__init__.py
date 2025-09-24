from json import loads
from inkaterm.report.panelRead import reportRead as rp
import os

def showRep(op):
    try:
        file = rp(op = op)
        if os.path.exists(file):
            f = loads(open(file, "r").read())
            for i in f:
                if len(f) > 0:
                    print(f"in {i} you printed the {f[i]['name']} with {f[i]['size'][0]}X{f[i]['size'][1]} size and {f[i]['format']} format")
                else:
                    print("nothing in your history")
    except Exception as e:
        print(f"this is fine\n{e}")
