#Escriba una función llamada leer_tiempo()
#La función debe tomar un argumento, un número entero y devolver un string que indique cuántas semanas y días son.


def leer_tiempo(days):
    extra_days = days % 7
    days = days - extra_days
    weeks = days / 7
    out = f"{int(weeks)} semana(s) y {extra_days} dias(s)"
    return out



print (leer_tiempo(13))
    