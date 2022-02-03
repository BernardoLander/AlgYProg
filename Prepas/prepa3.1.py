#Numeros de digitos incrementales
#dado un entero x de tres digitos diferentes, imprima "SI" si sus tres digitos van en forma ascendente de 
#izquierda a derecha, de lo contrario imprima "NO"

print("**WELCOME***\n")
n = input("please give 3 numbers to check if they are in an ascending order\n")
l = []

r = int(n)

if n.isnumeric and len(n) == 3:

    for i in range(len(n)):
        p = r % 10^i
        l.append(p)
else:
    print("Invalid Input")
    
if l[0] > l[1] and l[1] > l[2]:
    print("SI")
else:
    print("NO")
    