import argparse
from pathlib import Path
import sys 

sys.path.append(str((Path(__file__).parent / "llm_test_generation")))

from llm_run import main as llm_test_generation_main
from llm_run import Default, available_models, available_frameworks
from patch_run import run as patch_run_main

def run(args):
    llm_test_generation_main(args)
    patch_run_main(args.project_dir, args.src_dir, "test/config.json", args.only_test, args.patch_gen)

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-sf", "--source_file", dest="src_file", metavar="SOURCE_PATH", type=Path, required=True,
                      default=[], nargs='+',
                      help="source code file path")
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path)
    parser.add_argument("-p", "--project-directory", dest="project_dir", action="store", required=True, type=Path)
    # parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path)

    # Optional arguments for LLM test generation
    parser.add_argument("-r", "--res", metavar="MANUAL_RESOURCE", type=str,
                      default=[], nargs='+',
                      help="manual additional data <title>:<content>")
    parser.add_argument("-f", "--fcts", metavar="FUNCTION_NAMES", default=[], nargs='+',
                        help="target function names")
    parser.add_argument("-n", "--neg", metavar="NEG_TEST_NUM", type=int,
                        default=3,
                        help="negative test number")
    parser.add_argument("-i", "--iter", metavar="ITERATION_NUM", type=int,
                        default=1,
                        help="request iteration number")
    
    parser.add_argument("-m", "--model", metavar="MODEL_NAME", type=str,
                      default=Default.Model.value, choices=available_models,
                      help=f"LLM model name {available_models}")
    parser.add_argument("-fw", "--framework", metavar="FRAMEWORK_NAME", type=str,
                        default=Default.Framework.value, choices=available_frameworks,
                        help=f"Test framework name {available_frameworks}")
    parser.add_argument("-ec", "--err-configs", metavar="ERRORLINE_CONFIGS_PATH", type=Path,
                        default=Default.Finder_Config_Path.value,
                        help="errorlines finder configs path")
    parser.add_argument("-nc", "--neg-configs", metavar="NEG_CONFIGS_PATH", type=Path,
                        default=Default.Neg_Config_Path.value,
                        help=f"negative test generation configs path")
    parser.add_argument("-pc", "--pos-configs", metavar="POS_CONFIGS_PATH", type=Path,
                        default=Default.Pos_Config_Path.value,
                        help=f"positive test generation configs path")
    parser.add_argument("-fc", "--fw-configs", metavar="FRAMEWORK_CONFIG_PATH", type=Path,
                        default=Default.Framework_Config_Path.value,
                        help="Test framework config json path")
    parser.add_argument("-o", "--out", metavar="OUTPUT_PATH", type=Path,
                        default=Default.Out_DirPath.value,
                        help="output path")

    additive_option = parser.add_mutually_exclusive_group()
    additive_option.add_argument("-t", "--only-test", dest="only_test", action="store_true", help="Only run test casses")
    additive_option.add_argument("-g", "--patch-gen", dest="patch_gen", action="store_true", help="Run patch generation")

    args = parser.parse_args()
    run(args)

if __name__ == "__main__" :
    main()
