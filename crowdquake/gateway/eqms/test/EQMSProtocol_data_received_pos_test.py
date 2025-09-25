def test_pos_1():
	from asyncio import transports
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = None
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	transport = transports.BaseTransport()
	protocol.connection_made(transport)
	
	byte_data = bytes([0xF1, 0x01, 0x02, 0x03, 0x04, 0x00, 0x10, 0xA1, 0x00, 0x0C, 0x04, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0xED, 0xFD])
	protocol.data_received(byte_data)

def test_pos_2():
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = None
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	bytearray_data = bytearray([0xF1, 0x01, 0x02, 0x03, 0x04, 0x00, 0x10, 0xA1, 0x00, 0x0C, 0x05, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0xED, 0xFD])
	protocol.data_received(bytearray_data)

def test_pos_3():
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = None
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	memoryview_data = memoryview(b"\xF1\x01\x02\x03\x04\x00\x10\xA1\x00\x0C\x0D\x20\x21\x22\x23\x24\x25\x26\xED\xFD")
	protocol.data_received(memoryview_data)

def test_pos_4():
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = None
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	bytes_data = bytes([0xF1, 0x01, 0x02, 0x03, 0x04, 0x00, 0x10, 0xA1, 0x00, 0x0C, 0x06, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0xED, 0xFD])
	protocol.data_received(bytes_data)

def test_pos_5():
	from asyncio import transports
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = Path("./")
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	transport = transports.BaseTransport()
	protocol.connection_made(transport)
	
	byte_data = bytes([0xF1, 0x01, 0x02, 0x03, 0x04, 0x00, 0x10, 0xA1, 0x00, 0x0C, 0x04, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0xED, 0xFD])
	protocol.data_received(byte_data)

def test_pos_6():
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = Path("./")
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	bytearray_data = bytearray([0xF1, 0x01, 0x02, 0x03, 0x04, 0x00, 0x10, 0xA1, 0x00, 0x0C, 0x05, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0xED, 0xFD])
	protocol.data_received(bytearray_data)

def test_pos_7():
	from pathlib import Path
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    def __init__(self):
	        self.capture_mode = False
	        self.capture_path = Path("./")
	
	    def log_failure(self, err, reason):
	        pass
	
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	ctx = MockContext()
	protocol = EQMSProtocol(ctx)
	
	memoryview_data = memoryview(b"\xF1\x01\x02\x03\x04\x00\x10\xA1\x00\x0C\x0D\x20\x21\x22\x23\x24\x25\x26\xED\xFD")
	protocol.data_received(memoryview_data)