#Program for calculating the area for a circle or a triangle or a square
#Intro 

print("Welcome, This program will procide you atool to calculate a figure's area\n")
op = input("Enter: \n 1.Triangle 2. Square 3.Circle \n===>")
#Check if option is numeric and in range
if op.isnumeric() == True:
    if int(op)>= 1 and int(op) <= 3:
        print("Great Choice...")
        #Triangle getinput numeric check and operation
        if int(op) == 1:
            b = input("Please give me the base of the triangle:\n==>")
            h = input("Please give me the Height of the triangle:\n==>")
            if b.isnumeric() == True and h.isnumeric() == True:
                b = float(b)
                h = float(h)
                print("the Triangle's area is:", {b*h/2})
            else:
                print("INVALID INPUT")
        #Square getinput numeric check and operation
        elif int(op) == 2:
            b = input("Please give me the side of the square:\n==>")
            if b.isnumeric() == True:
                b = float(b)
                print(f"The area of the Square is: ", {b*b})
            else:
                print("INVALID INPUT")
        #Triangle getinput numeric check and operation
        else:
            r = input("Please give me the radius of the circle\n==>")
            if r.isnumeric() == True:
                r = float(r)
                print(f"The Area of the circle is: ", {(r**2)*3.14})
            else:
                print("INVALID INPUT")
else:
    print("INVALID INPUT")


    #Errors: 1. prints weren't closing when an operation is on the string because you have to have a coma separating the strings from other stuff
    #2. isnumeric is for numbers as strings or chars not floats
    #3. you cant cast numbers for an operation inside a string