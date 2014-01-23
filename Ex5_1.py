# Exponentiation


def exponentiation (b, n):
	if n == 0:
		return 1
	else:
		return b * exponentiation(b, n-1)
		

base = int(raw_input('Enter the base number: '))
expo = int(raw_input('Enter the exponent: '))

print exponentiation(base, expo)
