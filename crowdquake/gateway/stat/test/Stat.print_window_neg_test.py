def test_neg_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10, on_report=123)
	while True:
	    stat.add(1, 0.5, 100)

def test_neg_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10, on_report="not_callable")
	while True:
	    stat.add(1, 0.5, 100)