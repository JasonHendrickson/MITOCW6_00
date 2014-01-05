#Prob 2.2
#Determines minimum payment to pay off credit card in 12 months

balance = float(raw_input('Enter the outstanding balance on your credit card: ')) 
rate = float(raw_input('Enter the annual credit card interest rate as a decimal: ')) 
pmt = 10
origbal = balance 				#Maintain a recording of the original balance

while balance >= 0.0:
	month = 12					#reset months to 12
	balance = origbal			#reset balance to original value
	for month in range(0, 13):
		balance = (balance * (1 + rate/12.0)) - pmt
		#print 'One payment at: $' + str(pmt)
		#print 'For month #' + str(month)
		#print 'Your current balance is: $' + str(balance)
		#assert pmt <= balance
		month = month - 1
	pmt = pmt +10				#Increment pmt

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: $' + str(pmt)
print 'Number of months needed: ' + str(month)
print 'Balance: $' + str(balance)

