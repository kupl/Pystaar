def test_pos_1():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	
	result = bytes_to_usim_str(b'\x01\x02')
	print(result)

def test_pos_2():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	
	result = bytes_to_usim_str(b'\x00\x00\x00\x01')
	print(result)

def test_pos_3():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	
	result = bytes_to_usim_str(b'\xff\xff')
	print(result)

def test_pos_4():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	
	result = bytes_to_usim_str(b'\x10\x00\x00')
	print(result)

def test_pos_5():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	
	result = bytes_to_usim_str(b'\x01\x02\x03\x04')
	print(result)