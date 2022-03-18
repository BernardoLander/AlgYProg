import pickle
import os



def recibir_datos_del_txt(nombre_txt,datos):
    
    lectura_binaria= open(nombre_txt,'rb')
    
    if os.stat(nombre_txt).st_size != 0:
        datos=pickle.load(lectura_binaria)

    lectura_binaria.close()

    return datos



def cargar_datos_en_txt(nombre_txt,datos):

    escritura_binaria=open(nombre_txt,'wb')

    datos=pickle.dump(datos,escritura_binaria)
    
    escritura_binaria.close()




class vehiculo():
    def __init__(self,plate, brand, spot, arrival):
        self.plate = plate
        self.brand = brand
        self.spot = spot
        self.arrival = arrival
        self.out_time = ""


class motorcycle (vehiculo):
    def __init__(self, plate, brand, spot, arrival):
        vehiculo().__init__(plate, brand, spot, arrival)


class car (vehiculo):
    def __init__(self,plate, brand, spot, arrival, minusvalid):
        vehiculo().__init__(plate, brand, spot, arrival,)

        self.minusvalid = minusvalid



def cargar_objetos(bd):
    newdb = []
    for i in range(len(bd)):

        for key, value in bd[i].items():

            if bd[i]["type"] == "AUTOMOVIL":

                new_car = car(bd[i]["plate"],bd[i]["brand"],bd[i]["spot"], bd[i]["arrival"], bd[i]["handicapped"])
                newdb.append(new_car)

            elif key["type"] == "MOTOCICLETA":

                new_bike = motorcycle(bd[i]["plate"],bd[i]["brand"],bd[i]["spot"], bd[i]["arrival"])
                newdb.append(new_bike)
    
    return newdb
                

def num_verify(rangemin = 1, rangemax = 3, msg = ""):

    num = input(msg)

    if num.isnumeric():
        if int(num) <= rangemax:
            if int(num) >= rangemin:
                return int(num)
            else:
                print("ERROR INVALID NUMBER")
                return num_verify(rangemin, rangemax , msg)
        else:
            print("ERROR INVALID NUMBER")
            return num_verify(rangemin, rangemax, msg)
    else:
        print ("ERROR INVALID INPUT")
        return num_verify(rangemin, rangemax, msg)
        

def vehicle_out(parking = [], db = []):

    op = num_verify(1,len(parking),"Escriba el numero del Vehiculo que salio del estacionamiento\n")

    out_time = input("Escriba la hora de salida del Vehiculo\n")

    parking.pop(parking[op])
    db[op].out_time = out_time
    db[op].spot = None

    return parking , db



def verify_str(msg):
    text = input(msg)
    if text.isalpha():
        return text
    else:
        print("ERROR INVALID INPUT")
        return verify_str(msg)


def verify_str_num(msg):
    text = input(msg)
    if text.isalnum():
        return text
    else:
        print("ERROR INVALID INPUT\n")
        return verify_str_num(msg)

def yes_no (msg):
    op = input(msg)

    if op.capitalize() == "Y":
        return True
    elif op.capitalize() == "N":
        return False
    else:
        print("ERROR INVALID INPUT\n")
        return yes_no(msg)
