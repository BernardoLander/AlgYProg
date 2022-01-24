print("Welcome to the Calculator")
print("*** 1. To add a number 2. To subtract a number 3. To multiply a number 4. To divide a number***")
op = input("Please Give me a Number in range:\n==>")

if op.isnumeric() and int(op)<5 and int(op)>0:
    op = int(op)
    #check which option
    if op == 1:
        v = float(input("Please give a number to add:\n==>"))
        u = float(input("Please give a number to add:\n==>"))
        #print result
        print("Result is:",{v+u})

    elif op == 2:
        v = float(input("Please give a number to subtract by:\n==>"))
        u = float(input("Please give a number to subtract to:\n==>"))
        #print result
        print("Result is:",{v-u})

    elif op == 3:
        v = float(input("Please give a number to multiply:\n==>"))
        u = float(input("Please give a number to multiply:\n==>"))
        #print result
        print("Result is:",{v*u})
    
    else:
        v = float(input("Please give a number to divide by:\n==>"))
        u = float(input("Please give a number to divide to:\n==>"))
        #print result
        print("Result is:",{v/u})
else:
    print("Error, please input number in range")