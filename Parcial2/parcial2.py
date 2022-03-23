from parcial2obj import Alcholicas, Virgenes, Cliente
from parcial2utils import num_verify, verify_str, yes_no,simple_numverify
from parcial2methods import agregara_barra, add_client, show_select_barra, facturizionamiento



def main():
    onoff = True

    clientes = []
    client_count = 0
    barra = {

        "Alcholicas":[],
        "Virgenes": []

    }
    while onoff:

        op = num_verify (0,2,'''Bienvenido al saman Bar
                Presione 1. realizar una compra
                Presione 2. para revisar las estadisticas del bar
                Presione 0. para agregar bebidas a la barra
                ===>''')

        if op == 1:
            clientes = add_client(clientes)
            show_select_barra(barra, clientes[client_count])
            facturizionamiento(clientes[client_count])
            client_count += 1
        
        
        elif op == 2:
            #Estadisticas
            pass
        
        else:
            #agregar bebidas
            barra = agregara_barra(barra)
            print("Agregado con exito!")

        onoff = yes_no('''Desea continuar en el programa?
                            Y/N ==>''')


main()