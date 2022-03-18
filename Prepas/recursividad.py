cadena = '''
312313L....:;;;A;;;;;1231231231231313131 RE13123123
1313??????******C12312312312313
U;;;;R???S23123
12312312I.....V44515
454%###I####DAD)))))))))))))
((((((((((((((((((())))))
))))))))))))) ES{}}}}}}} ,,,<<>>>>>>>G@@@@@E
{{{{{{{{{{{{{{{NI}}}}}}}}}}}}}}}!!!!!!!$$$$$A......
........................L!!!!
 
'''





def seleccion_de_letra(txt, i):
    if i == len(txt):
        return (' ')
    elif txt[i].isalpha():
        print(txt[i], end='')
        return seleccion_de_letra(txt, i+1)
    elif txt[i] == " ":
        print(txt[i], end="")
        return seleccion_de_letra(txt, i+1)    
    else:
        return seleccion_de_letra(txt, i+1)

def main ():

    print(seleccion_de_letra(cadena, 0))

main()