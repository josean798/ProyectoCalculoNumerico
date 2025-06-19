import sys
import os
import numpy as np
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from Process.ProcessMain import ProcessMain


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    storageInputDir = os.path.join(base_dir, "StorageInput")
    storageDir = os.path.join(base_dir, "Storage")
    
    ProcessMain(storageInputDir, storageDir)

if main() == "__main__":
    main()


