print("Welcome")

#Input N to return 2^n result

#imput
v = int(input("Please give me number:\n"))

#Variable for result
u = 1

#Loop to multiplipy v times
while v > 0:
    u = u*2
    v = v-1

#print result
print("The number is:", u)

#errors: 1. v=-1 i not the same as v-=1.  2. u cant be = 2 because the counter starts at an offset