from hashlib import sha512
from json import loads
import os
import importlib.resources as pkg
from .. import db

def reportRead(key, op):
    try:
        if op == "delete":
            inp = input("do you want to delete all your history? [Y/N]")
            if inp.strip().lower() == "y":
                for file in os.listdir("inkatermReports"):
                    os.remove(f"inkatermReports/{file}")
            else:
                print("Ok")
        idb = loads(pkg.files(db).joinpath("idb.json").open("r", encoding="utf-8").read())
        if sha512(key.encode()).hexdigest() in idb["license"].values():
            name = ""
            for i, j in idb["license"].items():
                if sha512(key.encode()).hexdigest() == j:
                    name = i
            file = f"inkatermReports/{name}.json"
            return file
        else:
            print("invalid key")
            return False
    except:
        print("this is fine")
