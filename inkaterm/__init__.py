from inkaterm.procces import main
from inkaterm.report import showRep

def ink(file, char = "# ", same = True, pro = {"key": "None", "report": False}):
    return main(file, char, same, pro)
def history(key, op = "nothing"):
    showRep(key, op)
