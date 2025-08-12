from json import loads
from inkaterm.report.panelRead import reportRead as rp

def showRep(key, op):
    try:
        file = rp(key, op)
        if not file == False:
            f = loads(open(file, "r").read())
            for i in f:
                if len(f) > 0:
                    print(f"in {i} you printed the {f[i]['name']} with {f[i]['size'][0]}X{f[i]['size'][1]} size and {f[i]['format']} format")
                else:
                    print("nothing in your history")
    except:
        print("this is fine")
