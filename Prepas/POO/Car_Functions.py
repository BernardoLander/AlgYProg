from random import *
from Carro_ import *

def random_position(cars_list,car):
 
    
    is_position_repited=True

    while (is_position_repited) or (car.get_position() == -1):
        
        car.set_position(randint(1,6))
        is_position_repited=False

        for car_pos in range(len(cars_list)):

            if car.get_position()== cars_list[car_pos].get_position():
                is_position_repited=True
                break
        


def add_car(cars_list,new_car):

    return cars_list.append(new_car)


def positions_in_order(cars_list):

    for x in range(len(cars_list)):

        for w in range(x):

            if cars_list[x].get_position() < cars_list[w].get_position():
                aux=cars_list[x]
                cars_list[x]=cars_list[w]
                cars_list[w]=aux



def print_car_list(cars_list):
    
    for car in range(len(cars_list)):

        print(f"{cars_list[car].get_driver()} with the {cars_list[car].get_mark()} car has arrived on the position N°{cars_list[car].get_position()}\n")




