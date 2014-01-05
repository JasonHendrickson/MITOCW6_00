##Prob 2.1
##Sample of minimum payments on a credit card balance in a 12 month period

##Variables
month = 1 #tracs number of payment cycles
balance = float(raw_input('Enter the outstanding balance on your credit card:'))
rate = float(raw_input('Enter the annual credit card interest rate as a decimal:'))
minPer= float(raw_input('Enter the minimum monthly payment rate as a decimal:'))
TotPd = 0  #Calcs total amount paid

while month <= 12:
	pmt = round(float(minPer * balance), 2)  #Calcs the minimum monthly payment
	ActInt = round((rate/12.0)*balance, 2)  #Calcs the interest accrued each month
	PrinPd = round((pmt - ActInt), 2)  #Calcs the amount of payment applied to the balance
	balance = round ((balance - PrinPd), 2)  #calcs the new balance
	
	
	##Prints all info
	print 'Month: ' + str(month)
	print 'Minimum monthly payment: $' + str(round(pmt, 2))
	print 'Principle paid: $' + str(round(PrinPd, 2))
	print 'Remaining balance: $' + str(round(balance, 2))
	
	TotPd = TotPd + pmt
	month = month +1

print 'RESULT'
print 'Total amount paid: $' + str(TotPd)
print 'Remaining balace: $' + str(round(balance, 2))