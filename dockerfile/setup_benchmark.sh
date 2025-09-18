#!/bin/bash

set -e # Exit immediately if a command exits with a non-zero status.

mkdir -p benchmark
array=()

# --- Python 스크립트를 실행하여 정보를 읽어오는 부분 ---
while read -r line; do
    # Read the line from Python script's stdout and set variables
    eval "$line"

    echo "Processing ${PROJECT_FOLDER}..."

    # Change directory to the project folder
    cd "$PROJECT_FOLDER"

    # Go back to the benchmark directory
    cd /Pystaar/benchmark

    # Check if the repository is already cloned
    if [ ! -d "/Pystaar/benchmark/${REPO}" ]; then
        echo "Cloning ${GIT}..."
        git clone "${GIT}"
        array+=("${REPO}")
    fi

    new_dir="${REPO}"

    # Copy dependency files
    cp "${PROJECT_FOLDER}/dependency_setup.sh" "/Pystaar/benchmark/${new_dir}/dependency_setup.sh"
    cp "${PROJECT_FOLDER}/requirements.txt" "/Pystaar/benchmark/${new_dir}/pyter_requirements.txt"

    cd "${new_dir}"

    # --- Pyenv and Git operations ---
    pyenv install -s "${PY_VERSION}"
    pyenv virtualenv "${PY_VERSION}" "${new_dir}"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    source ~/.bashrc

    pyenv activate "${new_dir}"
    pyenv local "${new_dir}"

    pip install rich

    git checkout "${FIXED_PR_ID}"

    # Checkout previous versions of specific files
    for file in "${FILES[@]}"; do
        git checkout HEAD~1 "${file}"
    done
    
    # Copy test files
    for testfile in "${TEST_FILES[@]}"; do
        # Extract the relative path of the test file
        relative_path="${testfile#${PROJECT_FOLDER}/}"
        # Make sure the directory exists before copying
        mkdir -p "$(dirname "$relative_path")"
        cp "${testfile}" "${relative_path}"
    done

    #../dependency_setup.sh # This line is commented out in your original script
    # pyenv deactivate # This line is commented out in your original script

done < <(python get_info.py /Pystaar/benchmark_info)