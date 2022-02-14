#Dada una oración, escriba un programa Python para verificar si esa oración es un
#Pangrama o no. Un pangrama es una oración que contiene todas las letras del alfabeto inglés.

#Decir cuántas letras se repiten en la oración original


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

onoff = True
letters_list = []
letter_repeat_count = 0

print("***BIENVENIDO AL BUSCADOR DE PARAGRAMA***")

while onoff:
     oracion = input("Por favor inserte una oracion para verificar si es un paragrama \n ===>>")
     oracion = oracion.lower()
     
     for i in range(len(oracion)):
         repeated = False
         for x in range(len(alfabeto)):

            if alfabeto[x] == oracion[i]:

                for y in range(len(letters_list)):

                     if letters_list[y] == oracion [i]:
                         letter_repeat_count += 1

                         repeated = True

                if not repeated:
                    letters_list.append(oracion[i])
    
     cont = 0

     for i in range(len(letters_list)):
         for x in range(len(alfabeto)):
             if alfabeto[x] == letters_list[i]:
                 cont += 1

     if cont == len(alfabeto):
         print (f"Es un paragrama! Y se repiten letras {letter_repeat_count} veces\n")
    
     else:
         print ("No es un paragrama")

     while True:
        op = input("Para verificar otra oracion marque 1. para salir marque 0.\n===>")

        if op.isnumeric:
            op = int(op)
            if op == 1:
                print ("Reiniciando programa")
                break

            elif op == 0:
                print ("Hasta Luego")
                onoff = False
                break


            else:
                print ("ERROR Input invalido")
        else:
             print ("ERROR Input invalido")