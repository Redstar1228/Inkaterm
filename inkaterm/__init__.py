from inkaterm.procces import main
from inkaterm.report import showRep

def ink(file, char = "# ", same = True, report = False):
    return main(file, char, same, report)
def history(op = "nothing"):
    showRep(op)
