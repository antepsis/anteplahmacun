class combinations:

	def combination_norep(n, r):
		top = 1
		for i in range(1, n):
			top = i*top

		bottom1 = 1
		bottom2 = 1
		dif = n - r
		for j in range (1, r):
			bottom1 = j*bottom1

		for k in range (1, dif):
			bottom2 = k*bottom2

		bot = bottom1 * bottom2	
		result = top / bot

		return result

	