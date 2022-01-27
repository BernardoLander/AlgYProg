#Numero perfecto es todo numero natural que es igual a la suma de sus divisores propios( 6 es un num perfecto porque 1 + 2 + 3 = 6 y multiplicado da 6)

print("***WELCOME TO THE NUMERO PERFECTO CALCULATOR PATENT PENDING***")
while True:
    num = input("GIVE ME NUMBER FOR PERFECTO TIME: \n ===>>")
    

    if num.isnumeric():
        suma = 0
        num = int(num)

    for x in range(1,num):
        if num % x == 0:
            suma = suma + x
    
    if num == suma:
        print("THE NUMBER", num ,"IS PERFECTO")

    else:
        print("SADLY NUMBER",num , "IS NOT PERFECTO :(")
    op = input("ENTER 0 TO PERFECTO AGAIN, ENTER 1 TO YIELD\n ===>>>")
    #Error because of comparing a string to a int
    while not op.isnumeric and op != 1 and op != 0:
        op = input("ENTER 0 TO PERFECTO AGAIN, ENTER 1 TO YIELD\n ===>>")

    op = int(op)

    if op == 0:

        continue

    elif op == 1:

        break



