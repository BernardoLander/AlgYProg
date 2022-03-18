from string import ascii_letters


cadena= '''
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
def alphabet_list():
    abc = []
    for i in range(len(ascii_letters)):
        abc.append(ascii_letters[i])
    return abc

def algoritmo_recursivo(text, abc):
    cont = 0
    for i in range(len(text)):
        if 
