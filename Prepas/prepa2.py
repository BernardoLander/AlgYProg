from asyncio import wait_for
from concurrent.futures import wait


estudiantes = ["rommel","bernardo","miguel"]

estudiantes.append("carlos")



estudiantes.insert(1,"leo")
estudiantes.pop(-2)

print(estudiantes)



for index in range(8,0,-1):
    print(estudiantes)


