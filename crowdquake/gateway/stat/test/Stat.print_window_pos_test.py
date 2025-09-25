def test_pos_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=5, reporting_interval_sec=1)
	
	for i in range(5):
	    stat.add(i, 0.05 * i, 50)
	    time.sleep(0.2)
	
	stat.print_window()

def test_pos_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=15, sampling=2)
	
	for i in range(15):
	    stat.add(i, 0.2 * i, 200)
	    time.sleep(0.3)
	
	stat.print_window()

def test_pos_3():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=8, reporting_interval_sec=2)
	
	for i in range(8):
	    stat.add(i, 0.15 * i, 150)
	    time.sleep(0.5)
	
	stat.print_window()

def test_pos_4():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=20)
	
	for i in range(20):
	    stat.add(i, 0.1 * i, 100)
	    time.sleep(0.1)
	
	stat.print_window()

def test_pos_5():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=5, reporting_interval_sec=1)
	
	for i in range(1, 6):
	    stat.add(i, 0.05 * i, 50)
	    time.sleep(0.2)
	
	stat.print_window()

def test_pos_6():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=15, sampling=2)
	
	for i in range(1, 16):
	    stat.add(i, 0.2 * i, 200)
	    time.sleep(0.3)
	
	stat.print_window()

def test_pos_7():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	import time
	
	stat = Stat(num_window_size=8, reporting_interval_sec=2)
	
	for i in range(1, 9):
	    stat.add(i, 0.15 * i, 150)
	    time.sleep(0.5)
	
	stat.print_window()