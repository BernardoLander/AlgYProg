from string import ascii_letters


def alphabet_list():
    abc = []
    for i in range(len(ascii_letters)):
        abc.append(ascii_letters[i])
    
    return (abc)


def main():
   abc = alphabet_list()
   print (abc)

main()