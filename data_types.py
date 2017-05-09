def data_type(x):
	if isinstance(x, str):
		return len(x)
	if isinstance(x, bool):
		return x
	if isinstance(x, int):
		if(x<100):
			message= "less than 100"
		if(x>100):
			message= "greater than 100"
		if(x is 100):
			message= "equal to 100"
		return message
	if  x is None:
		return "no value"
		
