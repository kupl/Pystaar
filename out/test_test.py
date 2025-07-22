def test_neg_1():
	from project.source.add import test
	result = test('string')

def test_neg_2():
	from project.source.add import test
	result = test(None)

def test_neg_3():
	from project.source.add import test
	result = test([1, 2, 3])

def test_pos_1():
	from project.source.add import test
	result = test(5)
	print(result)

def test_pos_2():
	from project.source.add import test
	result = test(3.14)
	print(result)

def test_pos_3():
	from project.source.add import test
	result = test(-10)
	print(result)

def test_pos_4():
	from project.source.add import test
	result = test(0)
	print(result)

def test_pos_5():
	from project.source.add import test
	result = test(1000000)
	print(result)