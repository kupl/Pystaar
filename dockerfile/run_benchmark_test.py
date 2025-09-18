import argparse
from pathlib import Path
import subprocess
import json

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="src_dir", action="store", required=True, type=Path) 
    parser.add_argument("-p", "--project-directory", dest="project_dir", action="store", required=True, type=Path)
    parser.add_argument("-c", "--config-file", dest="config", action="store", required=True, type=Path) 


    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config_content = json.load(f)
        name = config_content.get("name", "default_project")

    pyenv_path = f"/root/.pyenv/versions/{name}/bin/python"

    # Execute new process
    try:
        result = subprocess.run(
            [pyenv_path, "run_test.py",
             "-s", str(args.src_dir),
             "-p", str(args.project_dir),
             "-c", str(args.config)],
            check=True,
            capture_output=True,
            text=True
        )
        print("Process output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e.stderr)
    



if __name__ == "__main__" :
    main()
