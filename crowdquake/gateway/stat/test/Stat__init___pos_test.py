def test_pos_1():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	def test_pos_1():
	    stat = Stat(num_window_size=10)
	    stat.add(1, 0.5, 100)
	    print(stat.window_max_latency)
	
	test_pos_1()

def test_pos_2():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	def test_pos_2():
	    stat = Stat(num_window_size=5, sampling=2)
	    for i in range(10):
	        stat.add(i, 0.1 * i, 50)
	    print(stat.window_max_latency)
	
	test_pos_2()

def test_pos_3():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	def test_pos_3():
	    def report_callback(stats):
	        print("Reported stats:", stats)
	    stat = Stat(num_window_size=20, on_report=report_callback)
	    for i in range(15):
	        stat.add(i, 0.2 * i, 200)
	    print(stat.window_max_latency)
	
	test_pos_3()

def test_pos_4():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	def test_pos_4():
	    stat = Stat(num_window_size=8, reporting_interval_sec=2)
	    for i in range(10):
	        stat.add(i, 0.3 * i, 300)
	    print(stat.window_max_latency)
	
	test_pos_4()

def test_pos_5():
	from example.crowdquake.gateway.stat.src.gateway.core.stat import Stat
	
	def test_pos_5():
	    stat = Stat(num_window_size=15, sampling=3, reporting_interval_sec=1)
	    for i in range(20):
	        stat.add(i, 0.05 * i, 150)
	    print(stat.window_max_latency)
	
	test_pos_5()