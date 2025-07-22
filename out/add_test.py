def test_neg_1():
	from src.add import add
	add('string')

def test_neg_2():
	from src.add import add
	add(None)

def test_neg_3():
	from src.add import add
	add([])

def test_pos_1():
	from src.add import add
	
	result1 = add(10)
	print(result1)

def test_pos_2():
	from src.add import add
	
	result2 = add(3.5)
	print(result2)

def test_pos_3():
	from src.add import add
	
	result3 = add(-5)
	print(result3)

def test_pos_4():
	from src.add import add
	
	result4 = add(0)
	print(result4)

def test_pos_5():
	from src.add import add
	
	result5 = add(1000000)
	print(result5)