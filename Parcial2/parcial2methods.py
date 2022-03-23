from Parcial2.parcial2obj import Cliente
from parcial2obj import Alcholicas, Virgenes
from parcial2utils import num_verify, verify_str, yes_no, simple_numverify

def agregara_barra(db):

    new_drink = None

    op = num_verify(1,2,'''Modificador de Barra:
                            1. Para agregar bebida Alchoholica
                            2. Para agregar bebida No Alchoholica\n==>''')
    if op == 1:
        #agregar alchoholica
        name = verify_str('''Por favor introduzca el nombre de la bebida\n==>''')
        price = simple_numverify('''Por favor introduzca el precio de la bebida\n==>''')
        grado = simple_numverify('''Por favor introduzca el grado alchoholico de la bebida\n==>''')

        new_drink = Alcholicas(name, price, grado)
        db["Alcholicas"].append(new_drink)

    

    elif op == 2:
        #agregar no alchoholica
        name = verify_str('''Por favor introduzca el nombre de la bebida\n==>''')
        price = simple_numverify('''Por favor introduzca el precio de la bebida\n==>''')
        temperatura = simple_numverify('''Por favor introduzca la temperatura para ingerir de la bebida\n==>''')

        new_drink = Virgenes(name, price, temperatura)
        db["Virgenes"].append(new_drink)

    if yes_no('''Desea continuar agregando bebidas?
                Y/N ==>'''):
                agregara_barra(db)
    else:
        return db



def add_client(client_db):
    new_client = None

    name = verify_str('''Porfavor introduzca su nombre\n==>''')
    age = simple_numverify('''Por favor introduzca su Edad\n==>''')
    dni = simple_numverify('''Por favor introduzca su cedula\n==>''')

    new_client = Cliente(name, age, dni)

    client_db.append(new_client)

    return client_db



def show_select_barra(db, cliente):

    print ("****SELECCION DE NO ALCHOHOLICOS****")

    for i in range(len(db["Virgenes"])):
        print(f'''{i}. {db["Virgenes"][i].name}
                    Precio: {db["Virgenes"][i].price}
                    Temperatira de servido: {db["Virgenes"][i].temperatura}''')
    
    if cliente.minor is not True:
        print ("***** SELECCION DE ALCOHOLICOS*****")
        for i in range(len(db["Alcholicas"])):
            print (f'''{i}. {db["Alcholicas"][i].name}
                        Precio: {db["Alcholicas"][i].price}
                        Temperatira de servido: {db["Alcholicas"][i].temperatura}''')
        
    if yes_no('''Desea algun trago de nuestra seleccion de No Alchoholicos?
            Y/N ==>'''):

        drink = num_verify(0, len(db["Virgenes"]), '''Por favor indique el Numero del trago que desea\n ==>''')
        cliente.compras.append(db["Virgenes"][drink])

    elif yes_no('''Desea algun trago de nuestra seleccion Alchoholicos?
            Y/N ==>'''):

        drink = num_verify(0, len(db["Alcholicas"]), '''Por favor indique el Numero del trago que desea\n ==>''')
        cliente.compras.append(db["Alcholicas"][drink])
    
    else:
        print("No se realizo compra")
        return show_select_barra(db,cliente)
        



    if yes_no('''Desea continuar comprando?\n Y/N ==>'''):
            return show_select_barra(db,cliente)
    
    else:

        return
        
    


def facturizionamiento(cliente):
    print ("Realizando factura")
    total = 0
    print(f'''Para el cliente {cliente.name} de cedula {cliente.dni}
            Articulos comprados:\n''')
    for i in range(len(cliente.compras)):
        print(f'''{cliente.compras[i].name}
                    Precio: {cliente.compras[i].price}''')
        total = total + cliente.compras[i].price
    
    print(f'''Total a pagar {total}''')

    #if fibonacci(age):
       # total = total - total*0.05
