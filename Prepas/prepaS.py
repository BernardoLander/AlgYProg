def add_students(db):
    name = str_valid('Ingresa el nombre del estudiante: ','Ingreso Invalido. Ingrese nuevamente su nombre: ')
    last_name =str_valid('Ingresa el apellido del estudiante: ','Ingreso Invalido. Ingrese nuevamente su apellido: ')
    dni = number_validation('Ingrese su cedula: ','Ingreso Invalido. Porfavor ingresa tu cedula: ')
    asignaturas = []
    option = 0
    while option == 0:    
        materia = str_valid('Ingresa el nombre de la materia: ', 'Ingreso Invalido. Porfavor ingrese el nombre de la materia correctamente: ')
        option = option_continue_validation('Ingres 0 si desea continuar o ingrese 1 si desea salir: ','Ingreso Invalido. Por favor ingres 0 para continuar o 1 para salir: ')
        asignaturas.append(materia)
        db[dni] = {'name':name , 'lastName':last_name, 'Asignaturas':asignaturas }
        option=int(option)
    return db


def str_valid(msg1, msg2):
    while True:
        palabra = input(msg1) #palabra en este caso no toma ningun valor, lo que va a tomar el valor es el msg, con lo que pongamos como parametro al momemnto de ingresar la funcion
        if palabra.replace(" ",'').isalpha():
            break
        else:
            print(msg2)
    return palabra


def number_validation(msg1, msg2): #si paso dos parametros, arriba en dni tendria que poner dos parametros tambien
    while True:
        numero = input(msg1)
        if numero.isnumeric() and 0<int(numero):
            break
        else:
            print(msg2)
    return numero


def option_continue_validation(msg1, msg2):
    while True:
        numero = input(msg1)
        if numero.isnumeric() and 0<=int(numero)<=1:
            break
        else:
            print(msg2)
    return numero


def show_students(db):
    for dni, students in db.items():
        print(f'''\nCedula {dni}\n Nombre: {students['name']}\nApellido {students['lastName']}''')
    print('Materias:')
    for materia in students['Asignaturas']:
        print(materia)
        

def main():
    db ={}
    print('Bienvenido')
    resp = 's'
    while resp == 's':
        menu = input('Ingresa: \n1.Ingreso de estudiante a la basa de datos. \n2.Para eliminar un estudiante de la base de datos. \n3.Para mostrar los estudiantes registrados en la base de datos. \n4. Editar a un estudiante registrado \n==>')
        while not (menu.isnumeric() and 1<= int(menu) <=5):
            menu = input('Ingreso Invalido. Ingresa: \n1.Ingreso de estudiante a la basa de datos. \n2.Para eliminar un estudiante de la base de datos. \n3.Para mostrar los estudiantes registrados en la base de datos.\n4. Para editar un estudiante registrado. \n==>')
        if int(menu) == 1:
            db = add_students(db)
            print(db)
        elif int(menu) == 2:
            pass
        elif int(menu) ==3:
            show_students(db)
main()