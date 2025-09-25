def test_neg_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add('string', 0.5, 100)

def test_neg_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	s = Stat(10)
	s.add(1, 0.5, '100')

def test_neg_3():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(None, 0.5, 100)