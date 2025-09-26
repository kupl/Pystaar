#!/bin/bash

# running requests
time python opensource_benchmark/run_benchmark_test.py -s /Pystaar/benchmark/requests/requests -p /Pystaar/benchmark/requests -c /Pystaar/test_info/requests_info.json
time python run_fault_localize.py -c /Pystaar/test_info/requests_info.json
time python run_patch_generate.py -s /Pystaar/benchmark/requests/requests -c /Pystaar/test_info/requests_info.json
time python run_validate.py -s /Pystaar/benchmark/requests/requests -c /Pystaar/test_info/requests_info.json

# runnig pandas
time python opensource_benchmark/run_benchmark_test.py -s /Pystaar/benchmark/pandas/pandas -p /Pystaar/benchmark/pandas -c /Pystaar/test_info/pandas_info.json
time python run_fault_localize.py -c /Pystaar/test_info/pandas_info.json
time python run_patch_generate.py -s /Pystaar/benchmark/pandas/pandas -c /Pystaar/test_info/pandas_info.json
time python run_validate.py -s /Pystaar/benchmark/pandas/pandas -c /Pystaar/test_info/pandas_info.json

# ruuning salt
time python opensource_benchmark/run_benchmark_test.py -s /Pystaar/benchmark/salt/salt -p /Pystaar/benchmark/salt -c /Pystaar/test_info/salt_info.json
time python run_fault_localize.py -c /Pystaar/test_info/salt_info.json
time python run_patch_generate.py -s /Pystaar/benchmark/salt/salt -c /Pystaar/test_info/salt_info.json
time python run_validate.py -s /Pystaar/benchmark/salt/salt -c /Pystaar/test_info/salt_info.json