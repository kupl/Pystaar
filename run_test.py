import argparse
import pytest
from pathlib import Path
import os, sys

sys.path.append(str(Path(__file__).parent.parent.resolve()))

from run_test_dir import run_neg, run_pos
import os, sys

import logger

logger = logger.set_logger(os.path.basename(__file__))

def run(config) :
    # logger.info("Run Test")
    run_neg.preprocessing(config)
    run_pos.preprocessing(config)
    # logger.info("Done Test")

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path) 
    parser.add_argument("-p", "--project-directory", dest="project_dir", action="store", required=True, type=Path)
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path) 
    # parser.add_argument("-f", "--test_file", dest="test_file", action="store", default=None, type=Path)
    # parser.add_argument("-m", "--test_method", dest="test_method", action="store", default=None, type=Path)

    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    src_dir = args.src_dir.resolve()
    sys.path.append(str(project_dir))
    sys.path.append(str(src_dir))

    # run(args.test_dir, args.test_file, args.test_method)
    run(args.config)

if __name__ == "__main__" :
    main()
