from json import loads
import os

def reportRead(op):
    try:
        if op == "delete":
            inp = input("do you want to delete all your history? [Y/N]")
            if inp.strip().lower() == "y":
                for file in os.listdir("inkatermReports"):
                    os.remove(f"inkatermReports/{file}")
            else:
                print("Ok")
        name = "report"
        file = f"inkatermReports/{name}.json"
        return file
    except Exception as e:
        print(f"{e}\nthis is fine")
