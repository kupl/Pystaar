#!/bin/bash

mkdir -p /Pystaar/benchmark
array=()

for project_folder in $(find /Pystaar/opensource_benchmark/benchmark_info -mindepth 1 -maxdepth 1 -print)
do
    project="$( cut -d '/' -f 5 <<< "$project_folder" )";
    echo "Setting up project: $project"

    cd $project_folder

    py_version=$(jq -r '.py_version' bug_info.json)
    repo=$(jq -r '.repo' bug_info.json)
    git=$(jq -r '.git' bug_info.json)
    fixed_pr_id=$(jq -r '.fixed_pr_id' bug_info.json)
    declare -a "files=($(jq -r '.code_files | .[] | @sh' bug_info.json))"

    cd /Pystaar/benchmark

    if [ ! -d "/Pystaar/benchmark/${repo}" ]; then
        git clone ${git} 
        array+=(${repo})
    fi

    cp ${project_folder}/dependency_setup.sh /Pystaar/benchmark/${repo}/dependency_setup.sh
    cp ${project_folder}/requirements.txt /Pystaar/benchmark/${repo}/pyter_requirements.txt


    pyenv install -s ${py_version}
    pyenv virtualenv ${py_version} ${repo}
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    source ~/.bashrc

    cd /Pystaar/benchmark/${repo}

    pyenv activate ${repo}
    pyenv local ${repo}

    pip install rich

    git checkout ${fixed_pr_id}

    for file in "${files[@]}"; do
        git checkout HEAD~1 ${file}
    done

    for testfile in $(find $project_folder -name '*.py' -o -name '*.cfg')
    do
        testfile="$(realpath $testfile)"
        direc="$( cut -d '/' -f 6- <<< "$testfile" )";
	yes | cp $testfile /Pystaar/benchmark/${repo}/$direc
    done
done