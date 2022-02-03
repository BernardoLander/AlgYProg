bd ={}

print("Bienvenido")
while True:
    #2nd while loop to whait for user correct option and break for later use
    while True:
        option = input('''Ingresa:\n1.Para agregar a un estudiante a la base de datos
                            2. Para eliminar un estudiante de la base de datos
                            3. Para mostrar la base de datos''')
        if option.isnumeric() and 1 <= option < 4:
            
            option = int(option)
            break
        else:
            print("Por favor ingresa una opcion valida")
    
    if option == 1:
        while True:
            name = input("Ingresa el nombre del estudiante\n==>")
            if  name.isalpha():
                break
        while True:
            lastName = input("Ingresa el apellido del estudiante\n==>")
            if  lastName.isalpha():
                break
        while True:
            dni = input("Ingresa la cedula del estudiante\n==>")
            if  dni.isalpha():
                break
        asignaturas = []
        while True:
            materia = input("Ingrese una materia:\n==>")

            if materia.isalpha() == False:
                print ("Error ingresa un nombre valido para la materia")
                continue
            else:
                asignaturas.append(materia)

            op = input("Ingrese 0 para agregar materias o 1 para dejar de agregar materias:\n==>")
            while True:
                if op.isnumeric():
                    int(op)
                    if int(op) == 1:
                        break
                    elif int(op) != 0:
                        print ("Error intenta de nuevo\n")
                    else:
                        break
                else:
                    
                    print("Error ingresa un numero valido\n")

            if int(op) == 1:
                break
        bd[dni] ={"name":name , "lastName":lastName,"assignments":asignaturas}
                    



        