score = raw_input("Enter Score: ")
try:
    score>=0 and score <=1
except:
    score=-1
    print "enter a valid number"
    
if score >=.9:
   print "A"
elif score >=.8:
   print "B"
   
   