import argparse
from pathlib import Path
from run_validator.run_validate import run

def main() :
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path)
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path)

    args = parser.parse_args()

    run(args.src_dir, args.config)

if __name__ == "__main__" :
    main()
