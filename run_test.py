import argparse
from pathlib import Path
import sys
from run_test_dir.run_test import run

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path) 
    parser.add_argument("-p", "--project-directory", dest="project_dir", action="store", required=True, type=Path)
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path) 


    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    src_dir = args.src_dir.resolve()
    sys.path.append(str(project_dir))
    sys.path.append(str(src_dir))

    run(args.config)

if __name__ == "__main__" :
    main()
