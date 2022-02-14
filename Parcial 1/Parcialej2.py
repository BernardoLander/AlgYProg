#La empresa de transporte Expresos Saman, ofrece tres destinos diarios a ciudades del
# país, en vehículos de capacidad de hasta 10 pasajeros. Para cada destino hay 3 vehículos.
# V valencia 500;  P puerto la cruz 700

destinos = {
    "V":{"nombre":"Valencia","Valor":500, "Cupos": 10},
    "P":{"nombre":"Puerto La Cruz","Valor":700, "Cupos": 10},
    "B":{"nombre":"Barquisimeto","Valor":800, "Cupos": 10}
}

#a) numero de cedula, cant de pasajeros, codigo y nombre de destino
#monto bruto a pagar, cuanto de descuento(si no aplica colocar 0)
# monto de IVA +16% de monto bruto - descuento, monto neto a paga
# chequear: cupos disponibles

onoff = True

print ("****BIENVENIDO AL SISTEMA DE SAMAN EXPRESS****")
while onoff:
    option = input("Presione 1. para realizar una compra. 2. Para cerrar el dia 3. Para cerrar el programa")

    if option.isnumeric:
        if option == 1:
            print ("Bienvenido a la seccion de compra de pasaje")
            while True:
                dni = input("Por favor ingrese su cedula sin puntos ni comas")
                num_pasajeros = input("Por favor ingrese la cantidad de pasajes que va a comprar para su destino")
                gowhere = input("Por favor ingrese el codigo de su ciudad destino:\n V para Valencia P para pto La Cruz y B para Barquisimeto")

                if dni.isnumeric and num_pasajeros.isnumeric:
                    num_pasajeros = int(num_pasajeros)
                    if num_pasajeros > 11:
                        gowhere = gowhere.capitalize()
                        if gowhere == "V" or gowhere == "P" or gowhere == "B":
                            break
                        else:
                            print("Ingreso de codigo de ciudad invalido por favor intente de nuevo")
                    else:
                        print("Cantidad de pasajeros invalida")
                else:
                    print("Ingreso invalido por favor intente de nuevo")
            
            if destinos[gowhere]["cupos"] >= num_pasajeros:
                print (f"Cedula: {dni}")
                print (f"Cantidad de pasajeros: {num_pasajeros}")
                print (f'''Destino: {destinos[gowhere]["nombre"]}''')
                print (f'''Monto Bruto a pagar: {destinos[gowhere]["Valor"]}''')
                if num_pasajeros >= 4:
                    print (f'''Monto de descuento: {destinos[gowhere]["Valor"] * 0.2}''')
                    descuento = destinos[gowhere]["Valor"] * 0.2
                else:
                     print (f'''Monto de descuento: {0}''')
                     descuento = 0

                print (f'''Monto de IVA: {destinos[gowhere]["Valor"] - descuento * 0.16}''')
                IVA = destinos[gowhere]["Valor"] - descuento * 0.16

                print (f'''Monto a pagar: {destinos[gowhere]["Valor"] - descuento + IVA}''')

                destinos[gowhere]["Cupos"] = destinos[gowhere]["Cupos"] - num_pasajeros
            
            else:
                print ("No esta esa cantidad de cupos disponibles a ese destino")


        elif option == 2:

            #cerrar dia La cantidad de clientes por destino (no pasajeros)
            # El Monto Total Neto Facturado por destino
            # El MontoTotal de Descuentos otorgados por destino
            # El Monto Total Neto Facturado por Expresos Saman
            # Los datos del cliente que más dinero pagó
        
        elif option == 0:

            onoff = False
        
        else:

            print ("Ingreso invalido por favor intente de nuevo")
    


    else:
        print ("Ingreso invalido por favor intente de nuevo")
