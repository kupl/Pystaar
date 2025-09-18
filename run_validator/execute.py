import os
import subprocess
import shutil

class Execute() :
    def __init__(self, dir, project, pytest_info) :
        self.dir = dir

        self.project = project
        self.pytest_info = pytest_info
        self.pyenv_dir = f'/root/.pyenv/versions/{project}/bin/python'

        # check if pyenv python exists
        if not os.path.exists(self.pyenv_dir) :
            self.pyenv_dir = None

        self.airflow_init = False

    def execute_neg(self) :
        # if pyenv exists, use it
        if self.pyenv_dir is not None :
            python_dir = self.pyenv_dir
        else :
            python_dir = "python"

        pytest_execute = [python_dir, '-m', 'pytest']

        pytest_execute.extend(self.pytest_info['neg'])

        result = subprocess.Popen(pytest_execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        out, err = result.communicate()

        return out, err

    def execute_pos(self) :
        if self.pyenv_dir is not None :
            python_dir = self.pyenv_dir
        else :
            python_dir = "python"

        pytest_execute = [python_dir, '-m', 'pytest']

        pytest_execute.extend(self.pytest_info['pos'])

        result = subprocess.Popen(pytest_execute, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        out, err = result.communicate()

        return out, err

    def execute_program(self) :
        os.chdir(self.dir)
        result = subprocess.Popen(['./test.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')

        out, err = result.communicate()

        return out, err
