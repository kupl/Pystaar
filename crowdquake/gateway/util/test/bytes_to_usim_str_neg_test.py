def test_neg_1():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	bytes_to_usim_str('string')

def test_neg_2():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	bytes_to_usim_str(12345)

def test_neg_3():
	from example.crowdquake.gateway.util.src.gateway.util import bytes_to_usim_str
	bytes_to_usim_str(None)