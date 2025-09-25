def test_neg_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	# Test with a string input for num_window_size
	stat = Stat('invalid_size')
	stat.add(1, 0.1, 100)

def test_neg_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	# Test with a float input for num_window_size
	stat = Stat(10.5)
	stat.add(1, 0.1, 100)

def test_neg_3():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	# Test with a list input for num_window_size
	stat = Stat([10])
	stat.add(1, 0.1, 100)