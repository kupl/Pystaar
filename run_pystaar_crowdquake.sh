#!/bin/bash

# 1
python run_test.py -s example/crowdquake/gateway/eqms/src -p example/crowdquake/gateway/eqms -c example/crowdquake/gateway/eqms/EQMSProtocol.data_received_config.json
python run_fault_localize.py -c example/crowdquake/gateway/eqms/EQMSProtocol.data_received_config.json
python run_patch_generate.py -s example/crowdquake/gateway/eqms/src -c example/crowdquake/gateway/eqms/EQMSProtocol.data_received_config.json
python run_validate.py -s example/crowdquake/gateway/eqms/src -c example/crowdquake/gateway/eqms/EQMSProtocol.data_received_config.json

# 2
python run_test.py -s example/crowdquake/gateway/eqms/src -p example/crowdquake/gateway/eqms -c example/crowdquake/gateway/eqms/bcd_time_to_timestamp_config.json
python run_fault_localize.py -c example/crowdquake/gateway/eqms/bcd_time_to_timestamp_config.json
python run_patch_generate.py -s example/crowdquake/gateway/eqms/src -c example/crowdquake/gateway/eqms/bcd_time_to_timestamp_config.json
python run_validate.py -s example/crowdquake/gateway/eqms/src -c example/crowdquake/gateway/eqms/bcd_time_to_timestamp_config.json

# 3
python run_test.py -s example/crowdquake/gateway/producer/src -p example/crowdquake/gateway/producer -c example/crowdquake/gateway/producer/KafkaProducer_close_config.json
python run_fault_localize.py -c example/crowdquake/gateway/producer/KafkaProducer_close_config.json
python run_patch_generate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_close_config.json
python run_validate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_close_config.json

# 4
python run_test.py -s example/crowdquake/gateway/producer/src -p example/crowdquake/gateway/producer -c example/crowdquake/gateway/producer/KafkaProducer_produce_config.json
python run_fault_localize.py -c example/crowdquake/gateway/producer/KafkaProducer_produce_config.json
python run_patch_generate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_produce_config.json
python run_validate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_produce_config.json

# 5
python run_test.py -s example/crowdquake/gateway/producer/src -p example/crowdquake/gateway/producer -c example/crowdquake/gateway/producer/KafkaProducer_produce_with_sensor_timestamp_config.json
python run_fault_localize.py -c example/crowdquake/gateway/producer/KafkaProducer_produce_with_sensor_timestamp_config.json
python run_patch_generate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_produce_with_sensor_timestamp_config.json
python run_validate.py -s example/crowdquake/gateway/producer/src -c example/crowdquake/gateway/producer/KafkaProducer_produce_with_sensor_timestamp_config.json

# 6
python run_test.py -s example/crowdquake/gateway/stat/src -p example/crowdquake/gateway/stat -c example/crowdquake/gateway/stat/Stat__init__config.json
python run_fault_localize.py -c example/crowdquake/gateway/stat/Stat__init__config.json
python run_patch_generate.py -s example/crowdquake/gateway/stat/src -c example/crowdquake/gateway/stat/Stat__init__config.json
python run_validate.py -s example/crowdquake/gateway/stat/src -c example/crowdquake/gateway/stat/Stat__init__config.json

# 7
python run_test.py -s example/crowdquake/gateway/stat/src -p example/crowdquake/gateway/stat -c example/crowdquake/gateway/stat/Stat_add_config.json
python run_fault_localize.py -c example/crowdquake/gateway/stat/Stat_add_config.json
python run_patch_generate.py -s example/crowdquake/gateway/stat/src -c example/crowdquake/gateway/stat/Stat_add_config.json
python run_validate.py -s example/crowdquake/gateway/stat/src -c example/crowdquake/gateway/stat/Stat_add_config.json