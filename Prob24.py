def evaluate_poly(poly, x):					#Defines a function that will evaluate a given polynomial
	poly_tuple = (poly)						#Initializes the tuple variable for the equation
	value_of_x = float(x)					#Initializes the variable for the given value of x
	ans = 0
	num_iterate = len(poly_tuple)
	for z in range (0, num_iterate):
		mononomial = poly_tuple[z] * (value_of_x ** z)
		ans = ans + mononomial
		print ans
	return ans

print "This program calculates the polynomial f(x) = 7.0x^4 + 9.3x^3 + 5.0x^2 for any value of 'x'."
x = float(raw_input('Enter a value for x: '))
y = (0, 0, 5.0, 9.3, 7.0)
print evaluate_poly(y, x)
	
	
#Following lines were an experiment to determine input methods and feasibility of using tuple with raw_input	
#poly = tuple(raw_input('Enter a polynomial in the form of a tuple: '))
#print poly
#print len(poly)
#print type(len(poly))

	
#first_exp = int(raw_input('Enter the first exponent of the polynomial: '))
#first_coef = float(raw_input('Enter the first coefficient of the polynomial: '))
#second_exp = int(raw_input	
	
		