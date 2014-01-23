# """
# Uses Newton's method to find and return a root of a polynomial function.   
# Returns a tuple containing the root and the number of iterations required to get to the root.
# Example:
# >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)  	#x4 + 3.0x3 + 17.5x2 - 13.39
# >>> x_0 = 0.1
# >>> epsilon = .0001
# >>> print compute_root(poly, x_0, epsilon)
# (0.80679075379635201, 8)
# poly: tuple of numbers, length > 1
# Represents a polynomial function containing at least one real root.
# The derivative of this polynomial function at x_0 is not 0.
# x_0: float
# epsilon: float > 0
# returns: tuple (float, int)
# """

def evaluate_poly(poly, x):					#Defines a function that will evaluate a given polynomial
	poly_tuple = (poly)						#Initializes the tuple variable for the equation
	value_of_x = float(x)					#Initializes the variable for the given value of x
	ans = 0
	num_iterate = len(poly_tuple)
	for z in range (0, num_iterate):
		mononomial = poly_tuple[z] * (value_of_x ** z)
		ans = ans + mononomial
#		print ans
	return ans

def compute_deriv(poly):
	deriv = ()
	for i in range(1, len(poly)):
		new_coef = poly[i] * i
		deriv = deriv + (new_coef,)
	return deriv

def compute_root(poly_r, x_0, epsilon):
	number_of_iterations = 1
	while abs(evaluate_poly(poly_r, x_0)) > epsilon:
		x_0 = x_0 - (evaluate_poly(poly_r, x_0)/evaluate_poly(compute_deriv(poly_r), x_0))
		number_of_iterations = number_of_iterations + 1
	ans = (x_0, number_of_iterations)
	return ans

x = 0.1
e = .0001
initial_polynomial = (-13.39, 0.0, 17.5, 3.0, 1.0)
print compute_root(initial_polynomial, x, e)
#print type(compute_root(initial_polynomial, x, e))














