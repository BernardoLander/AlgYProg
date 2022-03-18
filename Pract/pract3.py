#Escriba una función llamada densidad_de_poblacion que tome dos argumentos:
#poblacion y area, y devuelva una densidad de población. calculada a partir de esos valores.

def densidad_de_poblacion (poblacion , area):
    densidad = poblacion / area
    return densidad


print(densidad_de_poblacion(15,2)) 
