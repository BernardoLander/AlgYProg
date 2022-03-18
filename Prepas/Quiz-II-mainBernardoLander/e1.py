# string para opción b)
string = "👍🤠!sotnup 7 ognet aY"


def voltear(string, i = 1):
    
    if i == len(string) + 1:
        return
    else:
        aux = len(string) - i
        print (string[aux], end="")
        return voltear(string, i + 1)


def main():

    voltear(string)

main()

