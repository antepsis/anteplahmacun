class combinations:

	# Calculates Combinations without repetition
	def combination_norep(self, n, r):
		top = 1
		test_n = n

		# Checks if n is an integer
		try:
			test_n += 1
		except TypeError:
			print "n not an integer"
			return False
		
		test_r = r


		# Checks if r is an integer 
		try:
			test_r += 1
		except TypeError:
			print "r not an integer"
			return False
		
		
		for i in range(1, n+1):
			top = i*top

		#print(top)

		bottom1 = 1
		bottom2 = 1
		dif = n - r
		

		for j in range (1, r+1):
			bottom1 = j*bottom1

		for k in range (1, dif+1):
			bottom2 = k*bottom2

		bot = bottom1 * bottom2	
		result = top / bot
		
		print(result)

		return result



	# Calculates Combinations with repetition
	def combination_withrep(self, n, r):
		toplimit = r + n - 1
		top = 1
		test_n = n



		# Checks if n is an integer
		try:
			test_n += 1
		except TypeError:
			print "n not an integer"
			return False
		
		test_r = r



		# Checks if r is an integer
		try:
			test_r += 1
		except TypeError:
			print "r not an integer \nPlease Enter a valid integer"
			return False

		for i in range(1 , toplimit+1):
			top = i*top

		bot1 = 1
		
		for j in range(1, r+1):
			bot1 = j*bot1

		bot2 = 1
		
		for k in range(1, n):
			bot2 = k*bot2		

		bot = bot1*bot2
		result = top/bot

		print(result)

		return result



	#combination_withrep(5, 3)
	#combination_norep(5, 3)
