import argparse
import os, sys
from pathlib import Path
from run_test_dir.run_test import run as run_test
from run_fault_localize import run as run_fault_localize
from run_patch_generate import run as run_patch_generator
from run_validate import run as run_validator

CUR_DIR = Path(os.getcwd())

def run(project_dir, src_dir, config, only_test, patch_gen): 
    project_dir = Path(project_dir).resolve()
    src_dir = Path(src_dir).resolve()

    sys.path.append(str(project_dir))
    sys.path.append(str(src_dir))


    if not patch_gen:
        run_test(config)

    if only_test:
        return

    run_fault_localize(config)

    # src_dir = os.getcwd() + "/example/real/src"

    try:
        run_patch_generator(src_dir, config)
    except AssertionError:
        pass
    # src_dir = os.getcwd() + "/example/real/src"
    run_validator(src_dir, config)

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path)
    parser.add_argument("-p", "--project-directory", dest="project_dir", action="store", required=True, type=Path)
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path)

    additive_option = parser.add_mutually_exclusive_group()
    additive_option.add_argument("-t", "--only-test", dest="only_test", action="store_true", help="Only run test casses")
    additive_option.add_argument("-g", "--patch-gen", dest="patch_gen", action="store_true", help="Run patch generation")

    args = parser.parse_args()

    run(args.project_dir, args.src_dir, args.config, args.only_test, args.patch_gen)

if __name__ == "__main__" :
    main()
