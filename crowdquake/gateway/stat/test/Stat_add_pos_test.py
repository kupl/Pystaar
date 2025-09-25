def test_pos_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(iteration=1, latency=0.5, msg_length=100)

def test_pos_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(iteration=2, latency=0.3, msg_length=200)

def test_pos_3():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(iteration=3, latency=0.1, msg_length=150)

def test_pos_4():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(iteration=4, latency=0.7, msg_length=300)

def test_pos_5():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	stat = Stat(num_window_size=10)
	stat.add(iteration=5, latency=0.2, msg_length=250)