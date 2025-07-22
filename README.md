# PySTAAR: An End-to-End, Extensible Framework for Automated Python Type Error Repair

The repository contains the framework for PySTAAR, for the paper "PySTAAR: An End-to-End, Extensible Framework for Automated Python Type Error Repair".

# Installation Guide 
We recommend using a PySTAAR in a local environment. First, clone the repository:

```bash
git clone https://github.com/kupl/Pystaar.git
cd Pystaar
pip install -r requirements.txt
``` 

Next, install the modified version of [pyannotate](https://github.com/dropbox/pyannotate):

```bash
pip install --use-pep517 -e pyannotate
```

# Execution Guide 
## Running the whole framework
To run the PySTAAR framework, we provide a sample script that demonstrates how to use the framework:

```bash
python pystaar.py -sf project/src/add.py -s project/src -p project -c test/config.json -f test
```

Each argument denote following:
- `--sf`: Source file to test whether it has type errors.
- `--s`: Source directory containing the source file and other source files.
- `--p`: Project directory containing the source file.
- `--c`: Configuration file in JSON format. 
- `--f`: Specific function to test for type errors.

The last argument is optional. If not provided, the framework will test all functions in the source file.

## Running the framework on a specific module
Each module in the framework can be run independently. 

### Test Generation 
To generate tests for a specific source file, use the following command:

```bash
python llm_run.py -sf project/src/add.py -p project
```

As a result of this command, the framework will generate tests for the functions in the specified source file. The generated tests will be saved in the `test` directory. Moreover, the framework will also generate a configuration file in the `test` directory, with name `config.json`, which contains the information about the test execution process, needed for further patch generation. Additional arguments can be found in the `llm_run.py` file. Further explanation of the `config.json` file can be found in [Configuation File](#configuration-file).

### Execution of Tests
To run the fault localization module, use the following command:
```bash
python run_test.py --config test/config.json
```

This command will execute the tests generated in the previous step and will save the results in the `test` directory. Additionally, passing `-n` or `--only-neg` will only run the negative tests.

### Fault Localization
To run the fault localization module, use the following command:
```bash
python run_fault_localize.py --config test/config.json
```
This command will run the fault localization module and will save the results in the `fl_output` directory in `test` directory. 

### Patch Generation
To generate patches for the identified type errors, use the following command:
```bash
python run_patch_generate --config test/config.json
```
This command will generate patches for the identified type errors and will save the results in the `generated_patches` directory in `test` directory.

### Patch Validation
To validate the generated patches, use the following command:
```bash
python run_validate.py --config test/config.json
```
This command will validate the generated patches and will save the results in the `validated_patches` directory in `test` directory. 

### Total Patch Generation
To run the whole patch generation process (Execution of Tests, Fault Localization, Patch Generation, Patch Validation), use the following command:
```bash
python patch_run.py -s project/src -p project -c test/config.json
```
This command can be used when tests are already generated and the user wants to customize the `config.json` file.

### Configuration File
The configuration file is a JSON file that contains the information about the test execution process, needed for further patch generation. The file should contain the following fields:

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
