def test_neg_1():
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
	
	mock_ctx = MockContext()
	protocol = EQMSProtocol(mock_ctx)
	protocol.data_received(123)  # Int input

def test_neg_2():
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
	
	mock_ctx = MockContext()
	protocol = EQMSProtocol(mock_ctx)
	protocol.data_received("string")  # String input

def test_neg_3():
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol
	
	class MockContext:
	    capture_mode = False
	    capture_path = ''
	    def log_failure(self, err, reason):
	        pass
	    def sink_acc_msg(self, key, value, timestamp):
	        pass
	    def sink_air_msg(self, key, value, timestamp):
	        pass
	    def sink_env_msg(self, key, value, timestamp):
	        pass
	
	protocol = EQMSProtocol(MockContext())
	protocol.data_received(123)