age = int(input("Enter your age: "))
if age<0:
    print("Enter a valid age")
elif age<12:
    print ("You are kid")
elif age>=13 and age<=25:
    print ("You are teenager")
elif age>25 and age<70:
    print("You are an adult")
else:
    print("You are old")