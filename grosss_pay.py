#create a script to calculate pay

hours =raw_input("enter the number of hours you worked:")
rate =raw_input("enter the rate that you are assigned :$")
gross_pay=float(hours)*float(rate)
gross_pay=str(gross_pay)
print "your gross pay for the period is $"+gross_pay+" only"
quit()