def fibonacci(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	
	previous, current = 0, 1
	for _ in range(2, n+1):
		previous, current = current, previous + current
	return current 
