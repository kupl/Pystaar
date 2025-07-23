import argparse
import os, sys
from pathlib import Path
from run_fl.run_fault_localize import run

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path)

    args = parser.parse_args()

    run(args.config)

if __name__ == "__main__" :
    main()
