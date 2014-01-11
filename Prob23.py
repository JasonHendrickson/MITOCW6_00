#Prob 2.3 
#Determine 12 month payoff payments by bisection


#Get user input
balance = float(raw_input('Enter the outstanding balance on your credit card: ')) 
rate = float(raw_input('Enter the annual credit card interest rate as a decimal: ')) 

#Initialize state variables
epsilon = 10			#Specifies acceptable variance from abs 0
lowpmt = balance/12		#Initial low bound (Balance without interest)
hipmt = (balance * (1 + (rate/12.0))**12)/12		#Initial high bound (Balance w/full years interest
pmt = (lowpmt + hipmt)/2		#midpoint between high and low bound


#Main program, runs until remaining balance is within acceptable variance specified above
while abs(balance) >= epsilon:
	month = 12					#reset months to 12
	balance = origbal			#reset balance to original value
	#Subloop called repeatedly while searching for accurate pmt amount
	for month in range(0, 13):
		balance = (balance * (1 + (rate/12.0))) - pmt
		#print 'One payment at: $' + str(pmt)
		#print 'For month #' + str(month)
		#print 'Your current balance is: $' + str(balance)
		#assert pmt <= balance
		month = month - 1
	#Adjusts high and low bounds after test of results	
	if balance > 0.0:
		lowpmt = pmt
	else:
		hipmt = pmt
	#resets pmt to new midpoint	
	pmt = (lowpmt + hipmt)/2
	#Provides output of each calculated value for debugging
	print 'high payment: ' + str(hipmt)
	print 'low payment: ' + str(lowpmt)
	print str(pmt)
#Provides final output of program	
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: $' + str(pmt)
print 'Number of months needed: ' + str(month)
print 'Balance: $' + str(balance)


