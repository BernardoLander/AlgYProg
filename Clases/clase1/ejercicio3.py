print("Welcome to the mersenne Calculator")

#Input N to return if 2^n number is prime

#imput
v = int(input("Please give me number:\n"))

#Variable for result
u = 1
#Loop to multiplipy v times
while v > 0:
    u = u*2
    v = v-1

u -= 1
aux = u - 1
cont = 0
#check for prime number

if u == 1:
    print("1 is not a prime number")

else:
    while aux > 1:
        if u % aux == 0:
            cont +=1
    aux -= 1

if cont == 0:
    print("The number", u , "is prime")

if cont > 0:
    print("The number", u , "is not prime")
