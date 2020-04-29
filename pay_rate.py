# This program will calculate your paycheck 
# This includes OT work but is only a gross figure
# 
pay_rate = float(input("How much do you earn per hour? "))
hours_worked = float(input("How many hours have you worked this week: "))
ot_rate = pay_rate * 1.5
ot_hours= float(hours_worked - 40)
if hours_worked <= 40:
	pay_total= hours_worked * pay_rate
else:
    pay_total= 40 * pay_rate
#
#  Set the OTpay_total variable 
otpay_total= (ot_hours * ot_rate) + pay_total
# 
if hours_worked <= 40:
	print("Total pay is:", pay_total, "For working",hours_worked,"hours this week!")
else:
	ot_hours= (hours_worked - 40)
	print ("Total Pay with OT is:",otpay_total, "For working",ot_hours,"hours of OT!" )