def test_neg_1():
	from project.source.add import test
	
	test('string')

def test_neg_2():
	from project.source.add import test
	
	test(None)

def test_neg_3():
	from project.source.add import test
	
	test([1, 2, 3])

def test_pos_1():
	from project.source.add import test
	result = test(5)
	print(result)

def test_pos_2():
	from project.source.add import test
	result = test(-3)
	print(result)

def test_pos_3():
	from project.source.add import test
	result = test(0)
	print(result)

def test_pos_4():
	from project.source.add import test
	result = test(2.5)
	print(result)

def test_pos_5():
	from project.source.add import test
	result = test(-7.5)
	print(result)