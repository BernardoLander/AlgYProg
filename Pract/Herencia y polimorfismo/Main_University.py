
'''10.2 MIEMBROS UNIVERSIDAD
Se desea desarrollar un sistema para el manejo de las clases, preparadurías, estudiantes,
preparadores y profesores. Cada profesor cuenta con su nombre, apellido, cédula y las
secciones que dictan, las cuales son 3. Los estudiantes tienen su nombre, apellido, carnet
y las secciones que cursan. Cada estudiante cursa 5 secciones. Las secciones tienen el
nombre y código de la asignatura, el profesor que las dicta, salón asignado y horario.
'''

from University_Functions import *
from Professor import *
from Persona import *
from Student import *
from Preparer import *


p1=Preparer("Rommel","Sanzonetti",19,20181130029,"algoritmos")
print(p1.get_name())
print(p1.get_carnet())


# print(p1.name)
# print(p1.__name)






# print('***WELCOME***')
# print('This program will provide you through a MENU OF OPTIONS:\n')

# #VARIABLES
# students_list=[]
# professors_list=[]
# preparers_list=[]




#MESSAGES TO REPEAT THE PROGRAM
# msg_out='Enter 0 to repeat the menu or another number to exit of the program'
# msg_not_valid_option='the option is not valid'

# #MESSAGES MENU
# msg_option_menu = '''1.Enroling subjects as student (You can only have 5 subjects)\n2.Entering the professor of a subject\n3.Entering the preparer of a subject\n4.Show professors, preparers and students\n\n===> '''

# option=0
# out=0

# while out==0:

#     option=enter_a_int(option,msg_option_menu,msg_not_valid_option)

#     if option==1:
#         students_list=add_student(students_list)

#     elif option==2:
#         professors_list=add_professor(professors_list)

#     elif option==3:
#         preparers_list=add_preparer(preparers_list)
    
#     elif option==4:
        
#         print("*** STUDENTS ***")
#         show_students(students_list)
#         print('\n')
        
#         print("*** PREPARERS ***")
#         show_preparers(preparers_list)
#         print("\n")
        
#         print("*** PROFESSORS ***")
#         show_professors(professors_list)
#         print('\n')
    
#     out = enter_a_int(out,msg_out,msg_not_valid_option)





# student_list=[]
# student_list = add_student(student_list)

# show_students(student_list)
