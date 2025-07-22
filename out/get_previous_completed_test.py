def test_neg_1():
	from datetime import datetime
	from luigi import Task, Parameter
	from hello.luigi.util import get_previous_completed
	
	class TestTask(Task):
	    param = Parameter()
	
	# This should raise NotImplementedError because there is no date parameter
	get_previous_completed(TestTask(param='2023-10-01'))

def test_neg_2():
	from datetime import datetime
	from luigi import Task, DateParameter, Parameter
	from hello.luigi.util import get_previous_completed
	
	class TestTask(Task):
	    param1 = DateParameter()
	    param2 = DateParameter()
	
	# This should raise NotImplementedError because there are multiple date parameters
	get_previous_completed(TestTask(param1=datetime.now(), param2=datetime.now()))