#Este programa se hizo anteriormente pero usando una cadena de condicionales. Ahora, se pide el mismo programa pero utilizando diccionarios.
# A continuación se te presentan 5 códigos postales escritos en código Morse, todos almacenados en un mismo string y separados por “*”.
#Tu labor consiste en descifrar cuáles son los números que componen cada código utilizando un diccionario que contenga lo mostrado en la tabla.

codigos_postales = "...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____."

morse_decoder = {".____" : "1", "..___" : "2", "...__" : "3", "...._" : "4", "....." : "5", "_...." : "6", "__..." : "7", "___.." : "8", "____." : "9","_____" : "0"}

morse_sets = []

i = 0

while i < len(codigos_postales):
    
    if codigos_postales[i] == "*":

        morse_sets.append("\n")
        i += 1
        continue
    
    elif codigos_postales[i] == " ":
        i += 1
        continue
    
    else:
        
        morse_sets.append(codigos_postales[i]+codigos_postales[i+1]+codigos_postales[i+2]+codigos_postales[i+3]+codigos_postales[i+4])
        i += 5

out = ""

for y in range(len(morse_sets)):

    if morse_sets[y] in morse_decoder.keys():
        
        out = out + str(morse_decoder[morse_sets[y]])

    elif morse_sets[y] == "\n":
    
        out = out + morse_sets[y]
        
print (out)
