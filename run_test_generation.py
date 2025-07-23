from argparse import ArgumentParser
from enum import Enum
from pathlib import Path

from llm_test_generation.models.model import ModelFactory
from llm_test_generation.tools.errorline_finder.run import run as run_finder, _classify_by_function
from llm_test_generation.tools.test_generator.run import run as run_tester
from llm_test_generation.util.filesys import read_json, write_file, make_directory
from llm_test_generation.validation.framework import TestFrameworkFactory

import sys, os, json 

sys.path.append(str((Path(__file__).parent).resolve()))
available_models = ModelFactory.get_keys()
available_frameworks = TestFrameworkFactory.get_keys()

# LLM을 이용한 테스트 코드 생성 초기 값 열거형 클래스.
class Default(Enum):
  Model = "response"
  Framework = "pytest"
  Finder_Config_Path =  Path(__file__).parent / "llm_test_generation" / Path("configs/openai/response/errorline_finder.json")
  Neg_Config_Path = Path(__file__).parent / "llm_test_generation" / Path("configs/openai/response/neg_test_generator.json")
  Pos_Config_Path = Path(__file__).parent / "llm_test_generation" /  Path("configs/openai/response/pos_test_generator.json")
  Framework_Config_Path = Path()
  TestCases_Path = Path(__file__).parent / Path("test")
  Out_DirPath = Path("out")


def main(args):
  # 파싱한 인자 연결.
  src = args.src_file
  project = args.project_dir
  res = args.res
  fcts = args.fcts
  iter = args.iter
  num = args.neg
  model = args.model
  fw = args.framework
  err_path = args.err_configs
  neg_path = args.neg_configs
  pos_path = args.pos_configs
  fw_path = args.fw_configs
  out = args.out

  res = dict(item.split(":", 1) for item in res if ":" in item)
  err_config = read_json(err_path) if err_path != Path() else {}
  neg_config = read_json(neg_path) if neg_path != Path() else {}
  pos_config = read_json(pos_path) if pos_path != Path() else {}
  fw_config = read_json(fw_path) if fw_path != Path() else {}

  try: project_root: Path = project[0]
  except:
    project_root = project
  sys.path.insert(0, str(project_root.resolve()))
  os.environ["PYTHONPATH"] = str(project_root)

  errorlines = run_finder(src[0], fcts, 5, model, err_config)
  classified = _classify_by_function(errorlines)

  for fct, errs in classified.items():
    tests = run_tester(src, res, errs, iter, 5, num, model, neg_config, pos_config, fw, fw_config)

    test_path = out/f"{fct}_test.py"
    codes = "\n\n".join(test.to_py() for test in tests)

    make_directory(out)
    write_file(test_path, codes)
  

  for test_file in Default.TestCases_Path.value.glob("*.py"):
    if "_pos" in test_file.name:
      test_pos_path = test_file
    if "_neg" in test_file.name:
      test_neg_path = test_file

  with open(Default.TestCases_Path.value / "config.json", "w") as f:
    config = {
      "name": "sample",
      "pos": [
        "--continue-on-collection-errors",
        "--execution-timeout",
        "300",
        "-k",
        "not neg",
        str(test_pos_path)
      ] ,

      "neg": [
        "--continue-on-collection-errors",
        "--execution-timeout",
        "300",
        str(test_neg_path)
      ],
    }

    json.dump((config), f)

def parse():
  parser = ArgumentParser()
  parser.add_argument("-sf", "--source_file", dest="src_file", metavar="SOURCE_PATH", type=Path, required=True,
                      default=[], nargs='+',
                      help="source code file path")
  parser.add_argument("-p", "--project-directory", dest="project_dir", metavar="PROJECT_PATH", type=Path, required=True, default=[], nargs=1)
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
  args = parser.parse_args()

  main(args)


if __name__ == "__main__":
  parse()