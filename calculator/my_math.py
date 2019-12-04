def check(v1, v2):
	return isinstance(v1, (int, float)) and isinstance(v2, (int, float))

def add(v1, v2):
	if not check(v1, v2):
		return "Incorrect types"
	return v1+v2

def sub(v1, v2):
	if not check(v1, v2):
		return "Incorrect types"
	return v1-v2

def mul(v1, v2):
	if not check(v1, v2):
		return "Incorrect types"
	return v1*v2

def div(v1, v2):
	if not check(v1, v2):
		return "Incorrect types"
	if v2 == 0:
		return "Faild v2 is 0!"
	return v1/v2
