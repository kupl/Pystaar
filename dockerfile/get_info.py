import json
import os
import sys

def get_benchmark_info(base_path):
    """
    Finds project folders in the specified base path, extracts necessary
    information from bug_info.json, and prints it in a shell-readable format.
    """
    
    project_folders = [
        os.path.join(base_path, d)
        for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d))
    ]

    for project_folder in project_folders:
        # Construct the project name and number
        folder_name = os.path.basename(project_folder)
        repo=folder_name
            
        # Read bug_info.json
        info_file_path = os.path.join(project_folder, 'bug_info.json')
        if not os.path.exists(info_file_path):
            continue
            
        with open(info_file_path, 'r') as f:
            bug_info = json.load(f)
            
        # Extract variables
        py_version = bug_info.get('py_version', '')
        git_url = bug_info.get('git', '')
        fixed_pr_id = bug_info.get('fixed_pr_id', '')
        code_files = ' '.join([f"'{f}'" for f in bug_info.get('code_files', [])])
        
        # Get test files
        test_files_string = ' '.join([
            f"'{os.path.join(project_folder, root, f)}'"
            for root, _, files in os.walk(project_folder)
            for f in files
            if f.endswith('.py') or f.endswith('.cfg')
        ])

        # Print the extracted information in a format the shell script can parse
        print(
            f"PROJECT_FOLDER='{project_folder}' "
            f"PROJECT='{folder_name}' "
            f"REPO='{repo}' "
            f"PY_VERSION='{py_version}' "
            f"GIT='{git_url}' "
            f"FIXED_PR_ID='{fixed_pr_id}' "
            f"FILES={code_files} "
            f"TEST_FILES={test_files_string}"
        )

if __name__ == '__main__':
    base_path = sys.argv[1] if len(sys.argv) > 1 else '/Pystaar/benchmark_info'
    get_benchmark_info(base_path)