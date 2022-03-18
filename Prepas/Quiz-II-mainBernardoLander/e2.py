import pickle
import os
from utilse2 import *


# diccionario con información de vehículos
parking_lot = [
  {
    "type": "AUTOMOVIL",
    "plate": "ABC12D",
    "brand": "Chevrolet",
    "spot": "A12",
    "arrival": "10:00:36",
    "handicapped": False
  },
  {
    "type": "MOTOCICLETA",
    "plate": "EFG34H",
    "brand": "Suzuki",
    "spot": "B10",
    "arrival": "10:20:15"
  },
  {
    "type": "AUTOMOVIL",
    "plate": "IJK56M",
    "brand": "Mazda",
    "spot": "A33",
    "arrival": "11:48:22",
    "handicapped": False
  }
]

def main():
  #recibir_datos_del_txt(C:\Users\berna\Desktop\Ej AyP\Prepas\Quiz-II-mainBernardoLander\parkingDB.txt)

  db = cargar_objetos(parking_lot)
  parking = db
  print ("BIENVENIDO\n")
  while True:
    
    op = num_verify(1,3,'''Por favor ingresa una opcion:
    1. Para hacer una salida de vehiculo.
    2. Para ver Vehiculos.
    3. Registrar un Vehiculo nuevo en el estacionamiento''')

    if op == 1:
      #salida
      
      print ("Puestos actualmente ocupados\n")

      for i in range(len(parking)):
        print (f"{i}. para {parking[i].spot}")
      
      parking , db = vehicle_out(parking)


    elif op == 2:
      #mostrar
      print("Lista de vehiculos actualmente en el estacionamiento")
      for i in range(len(parking)):
        print(f'''Placa: {parking[i].plate}
                  Marca: {parking[i].brand}
                  Puesto Ocupado: {parking[i].spot}
                  Hora de Llegada: {parking[i].arrival}''')
        if parking[i].minusvalid:
          print("Vehiculo Minusvalido\n")

    else:
      #ingresar
      opnum = num_verify(1,2,"Ingresa 1. para ingrsar un Carro y 2. para una Motocicleta\n")

      if opnum == 1:
        #carro
        plate = verify_str('''Por favor ingresa la placa del vehiculo\n''')
        brand = verify_str('''Por favor ingresa la marca del vehiculo\n''')
        spot = verify_str_num('''Por favor ingresa el puesto del vehiculo\n''')
        arrival = input("Por favor ingresa la hora de llegada del vehiculo\n")
        minusvalid = yes_no("Ingrsa Y o N si el carro es Minusvalido")
        new_car = car (plate, brand, spot,arrival, minusvalid)
        db.append(new_car)
        parking.append(new_car)
      
      else:
        plate = verify_str('''Por favor ingresa la placa del vehiculo\n''')
        brand = verify_str('''Por favor ingresa la marca del vehiculo\n''')
        spot = verify_str_num('''Por favor ingresa el puesto del vehiculo\n''')
        arrival = input("Por favor ingresa la hora de llegada del vehiculo\n")
        new_bike = motorcycle (plate, brand, spot,arrival, minusvalid)
        db.append(new_bike)
        parking.append(new_bike)

    if yes_no("Desea continuar?\n Y/N"):
      continue
    else:
      print ("Hasta Luego")
      break

main()



