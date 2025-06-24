import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Process.ProcessMain import ProcessMain
from Structure.MyDate import myDate
from Structure.myReplace import myReplace


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    storageInputDir = os.path.join(base_dir, "StorageInput")
    storageDir = os.path.join(base_dir, "Storage")
    date = str(myDate.now())
    dateReplace = myReplace(date)
    date = dateReplace.getReplace(":", "-")
    ProcessMain(storageInputDir, storageDir, date)

if __name__ == "__main__":
    main()


