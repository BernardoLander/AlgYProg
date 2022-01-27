print("**WELCOME TO THE PRIME CALCULATOR**")
num = int(input("Insert prime number:\n ===>>"))

#boolean for check instead of counter
flag = False

for x in range(2,num):
    if num % x == 0:
        flag = True
        #break to exit the loop
        break

if flag:
    print (num,"is not a prime number")
else:
    print (num,"is a prime number : )")