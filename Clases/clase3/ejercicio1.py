




#boolean for check instead of counter
num = 0
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