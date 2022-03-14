
def list_create(num):
    list = []
    while num > 1:
        list.append(int(num))
        num = num / 2
    return list
        
def russian(list , num):
    column2 = []
    aux = 0
    for i in range(len(list)):
        if list[i] % 2 == 1:
            aux = num * 2 ** i
            column2.append(aux)

    return (column2)

def list_adition (list):
    aux = 0

    for i in range(len(list)):
        aux = list[i] + aux

    return aux







def main():
    column1 = []
    column2 = []
    print("WELCOME TO RUSSIAN ADDER")
    numa = int(input("Enter Number A\n"))
    numb = int(input("Enter Number B\n"))
    column1 = list_create(numa)
    column2 = russian(column1, numb)
    print("Your result is:")
    print (list_adition(column2))



main()