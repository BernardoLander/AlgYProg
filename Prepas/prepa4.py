from unicodedata import name


db={
    "profesores":{
        "10777124":{
            "name" : "luis",
            "LastName" : "Bello",
            "materias" : {
                "BTQ09":{
                    "name" : "historia",
                    "credits" : "5"
                }
            }
        },
        "11666123":{
            "name" : "antonio",
            "LastName" : "Guerra",
            "materias":{
                "FBTSP05":{
                    "name" : "algoritmos",
                    "credits" : "3"

                }
            }

        }
    },
    "students": {
        "28013672":{
            "name" : "Rommel",
            "LastName" : "Sanzonetti",
            "materias" : ["mate","historia","logica"]
        }
    }
}


#print(db["profesores"]["11666123"]["LastName"])

#Iteration in diccionaries

for Key,value in db["students"].items():

    print(f'''Nombre:{value["name"]}''')

    for materia in value["materias"]:
        print(materia)


for Key2,value2 in db["profesores"].items():

    print(f'''Nombre: {value2["name"]},\n Apellido: {value2["LastName"]}''')

    
    for Key3,value3 in value2["materias"].items():

        print (f'''Codigo: {Key3},\n Nombre: {value3["name"]}''')
