import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Process.ProcessMain import ProcessMain
from Structure.myDate import myDate
from Structure.myReplace import myReplace
from Structure.myList import myList

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    storageInputDir = os.path.join(base_dir, "StorageInput")
    storageDir = os.path.join(base_dir, "Storage")
    logDir = os.path.join(base_dir)
    date = str(myDate.now())
    dateReplace = myReplace(date)
    date = dateReplace.getReplace(":", "-")
    errorList = myList()
    arraysList = myList()
    ProcessMain(storageInputDir, storageDir, logDir, date, errorList, arraysList)

if __name__ == "__main__":
    main()