# PySTAAR

PySTAAR is an end-to-end, extensible tool for automated Python type error repair. 

## Web Interface

PySTAAR provides a web interface for users to interact with the framework.
You can access the web interface at [PySTAAR Web Interface](https://pystaar.org).

## Running via Docker (Recommended)
It is highly recommended to run PySTAAR via the Docker image.

### Build the Docker image
You can build the Docker image using the provided `Dockerfile`. Run the following command in the terminal:
```bash
docker build -t pystaar dockerfile/.
```

### Run the Docker container
After building the Docker image, you can run the Docker container using the following command:\
```bash
docker run -it pystaar
```
This command will start the Docker container and open an interactive terminal session.

### Reproduce Results on open-source projects
We have included three open-source projects for you to test PySTAAR. 
Each is pre-configured with a single type error that PySTAAR will automatically fix.

#### Setup Projects
To set up the projects, run the following command in the Docker container:
```bash
bash opensource_benchmark/setup_benchmark.sh
bash opensource_benchmark/install_benchmark.sh
```
These commands will download and install the necessary dependencies for the projects.

#### Execute PySTAAR on Projects
You can run PySTAAR on three open-source projects using the following commands:
```
bash opensource_benchmark/run_pystaar_benchmark.sh
```
This command will execute PySTAAR on all three projects sequentially.

Alternatively, you can run PySTAAR on each project individually using the following commands (for `requests` project as an example):
```bash
python opensource_benchmark/run_benchmark_test.py -s /Pystaar/benchmark/requests/requests -p /Pystaar/benchmark/requests -c /Pystaar/test_info/requests_info.json
python run_fault_localize.py -c /Pystaar/test_info/requests_info.json
python run_patch_generate.py -s /Pystaar/benchmark/requests/requests -c /Pystaar/test_info/requests_info.json
python run_validate.py -s /Pystaar/benchmark/requests/requests -c /Pystaar/test_info/requests_info.json
```
The detailed information about the commands can be found [Below Section](#running-the-framework-on-a-specific-module).


### Reproduce Results on industrial application
You can also run PySTAAR on an industrial application (CrowdQuake) using the following command:
```bash
pip install -r requirements-crowdquake.txt
bash run_pystaar_crowdquake.sh
```
This command will execute PySTAAR on 7 samples from the CrowdQuake project.

## Running via Local Environment
We also provided PySTAAR in a local environment. First, clone the repository:

```bash
git clone https://github.com/kupl/Pystaar.git
cd Pystaar
pip install -r requirements.txt
``` 

Next, install the modified version of [pyannotate](https://github.com/dropbox/pyannotate):

```bash
pip install --use-pep517 -e pyannotate
```

### Setup OpenAI API Key for LLM-based Test Generation  

To execute the PySTAAR with existing components, you should set up OpenAI API key in the environment variable
```bash
export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
```

### Running the whole framework
To run the PySTAAR framework, we provide a sample script that demonstrates how to use the framework:

```bash
python pystaar.py -sf project/source/add.py -s project/source -p project -f test
```

Each option denote following:
- `-sf`: Source file to test whether it has type errors.
- `-s`: Source directory containing the source file and other source files.
- `-p`: Project directory containing the source file.
- `-f` (optional): Specific function to test for type errors.

You can check other options by running the script with `-h` or `--help` option:
```bash
python pystaar.py -h
```


### Running the framework on a specific module
Each module in the framework can be run independently. 

#### Test Generation 
To generate tests for a specific source file, use the following command:

```bash
python run_test_generation.py -sf project/source/add.py -p project
```

As a result of this command, the framework will generate tests for the functions in the specified source file. The generated tests will be saved in the `test` directory. Moreover, the framework will also generate a configuration file in the `test` directory, with name `config.json`, which contains the information about the test execution process, needed for further patch generation. Additional arguments can be found in the `run_test_generation.py` file. Further explanation of the `config.json` file can be found in [Configuation File](#configuration-file).

#### Execution of Tests
To run the fault localization module, use the following command:
```bash
python run_test.py -s project/source -p project -c test/config.json
```

This command will execute the tests generated in the previous step and will save the results in the `test` directory. Additionally, passing `-n` or `--only-neg` will only run the negative tests.

#### Fault Localization
To run the fault localization module, use the following command:
```bash
python run_fault_localize.py -c test/config.json
```
This command will run the fault localization module and will save the results in the `fl_output` directory in `test` directory. 

#### Patch Generation
To generate patches for the identified type errors, use the following command:
```bash
python run_patch_generate -s project/source -c test/config.json
```
This command will generate patches for the identified type errors and will save the results in the `generated_patches` directory in `test` directory.

#### Patch Validation
To validate the generated patches, use the following command:
```bash
python run_validate.py -s project/source -c test/config.json
```
This command will validate the generated patches and will save the results in the `validated_patches` directory in `test` directory. 

### Total Patch Generation
To run the whole patch generation process (Execution of Tests, Fault Localization, Patch Generation, Patch Validation), use the following command:
```bash
python patch_run.py -s project/source -p project -c test/config.json
```
This command can be used when tests are already generated and the user wants to customize the `config.json` file.

#### Configuration File
The configuration file is a JSON file that contains the information about the test execution process, needed for further patch generation. 
You can find example configuration files in the `test_info` directory.
The file should contain the following fields:

```json
{
    "name": <Project Name>
    "pos" : [
        "--continue-on-collection-errors", 
        "--execution-timeout", "300", 
        "-k", "not neg",
        <Positive Test Case Directories>
    ],
    "neg" : [
        "--continue-on-collection-errors", 
        "--execution-timeout", "300", 
        <Negative Test Case Directories>
    ]
}
```

Setting the Test Case Directories is done according to the [pytest command line option](https://docs.pytest.org/en/stable/reference/reference.html#ini-options-ref).

Followings are the frequently used fields in the configuration file:
- `<test-file-directory>`: Test specific directory containing the test files. For example, `example/sample/test/source_test.py` tests all the methods in `example/sample/src/source_test.py`.

- `<test-file-directory>::<test-method-name>`: Only test a specific method in the test file.
For example, `example/sample/test/source_test.py::test_progbar_neg1` tests `test_progbar_neg1` in `example/sample/src/source_test.py`.

- `-k <EXPRESSION>`: Executes tests that match the given expression. For example, `-k "not neg"` will run all tests that don't contain the word `neg` in their names.
