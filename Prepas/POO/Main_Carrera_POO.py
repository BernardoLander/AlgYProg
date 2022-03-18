'''9.5 CARRERA
Desarrolle un programa que simule una carrera de 6 automóviles y el respectivo lugar de
llegada de cada auto se verá dado aleatoriamente. Cada automóvil posee por lo menos
dos características(atributos) que le permiten ser diferenciado con otros:
Marca del automóvil.
Conductor.
Al final el programa deberá ser capaz de imprimir en pantalla la lista de llegada de los
automóviles de forma ordenada.
'''



from Carro_ import * #NOTESE QUE EL NOMBRE DEL FILE ES "CARRO_" Y EL NOMBRE DE LA CLASE ES 'CAR' ES UN ERROR APROPOSITO PARA QUE LO TENGAN EN CUENTA!
                    #PUES POR LO GENERAL SE LLAMAN IGUAL AMBAS



from Car_Functions import *
#MERCEDES, MCLAUREN, FERRARI, RED BULL, RENAULT, WILLIAMS

print("***Welcome this program simulates a cars race among six cars***")
print("\n")

cars_list=[]

# while len(cars_list)<6:

#     car_mark=input("Enter the car's mark:\n===> ")
#     car_driver=input("Enter the name of the car's driver:\n===> ")

#     new_car= Car(car_mark,car_driver)

#     random_position(cars_list,new_car)
#     add_car(cars_list,new_car)

# positions_in_order(cars_list)
# print_car_list(cars_list)



# De una manera no tan interactiva pero mas rapida, otra simulacion seria:
car_1=Car('Ferrari','Rommel')
random_position(cars_list,car_1)
add_car(cars_list,car_1)

car_2=Car('McLauren','Miguel')
random_position(cars_list,car_2)
add_car(cars_list,car_2)

car_3=Car('Red Bull','Luis')
random_position(cars_list, car_3)
add_car(cars_list,car_3)

car_4=Car('Williams','Jose')
random_position(cars_list,car_4)
add_car(cars_list,car_4)

car_5=Car('Renault','Freddy')
random_position(cars_list,car_5)
add_car(cars_list,car_5)

car_6=Car('Mercedes','Rafael')
random_position(cars_list, car_6)
add_car(cars_list,car_6)


positions_in_order(cars_list)
print_car_list(cars_list)

