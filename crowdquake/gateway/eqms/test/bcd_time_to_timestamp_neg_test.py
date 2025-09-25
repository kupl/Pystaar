def test_neg_1():
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol, bcd_time_to_timestamp
	
	# Test with an integer
	bcd_time_to_timestamp(123456)

def test_neg_2():
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol, bcd_time_to_timestamp
	
	# Test with a float
	bcd_time_to_timestamp(123.456)

def test_neg_3():
	from example.crowdquake.gateway.eqms.src.gateway.core.eqms import EQMSProtocol, bcd_time_to_timestamp
	
	# Test with a dictionary
	bcd_time_to_timestamp({1: 2, 3: 4})