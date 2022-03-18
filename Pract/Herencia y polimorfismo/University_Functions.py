from Professor import *
from Student import *
from Persona import *
from Preparer import *



def enter_a_int(option,msg_1,msg_2):
    is_valid_option=False
    while not(is_valid_option):
        try:
            option=int(input(msg_1))
            is_valid_option=True
        except:
            print(msg_2)
    
    return option

def enter_an_input(word,msg_1,msg_2):

    word=input(msg_1)
    while word.isnumeric():
        print(msg_2)
        word = input(msg_1)

    return word


def add_professor(professors_list):

    #MESSAGES
    msg_name="enter the professor's name\n===> "
    msg_last_name="enter the professor's last_name\n===> "
    msg_id="enter the professor's id:\n===> "
    msg_not_valid_character='What you entered is not valid.'
    msg_subject="enter the subject that the teacher teaches\n===> "
    msg_section="enter the section that the teacher teaches\n===> "
    msg_repeat_add_secciones="Enter 0 to add another section or another number to exit.\n===> "

    #VARIABLES
    name=''
    last_name=''
    subject=''
    section=''
    id=0


    name=enter_an_input(name,msg_name,msg_not_valid_character)
    last_name=enter_an_input(last_name,msg_last_name,msg_not_valid_character)
    subject = enter_an_input(subject, msg_subject, msg_not_valid_character)
    id=enter_a_int(id,msg_id,msg_not_valid_character)

    professor= Professor(name,last_name,id,subject)

    continuar=0
    while continuar==0:
        
        section=input(msg_section)
        professor.set_secciones(professor.add_secciones(section))

        continuar=enter_a_int(continuar,msg_repeat_add_secciones,msg_not_valid_character)

    professors_list.append(professor)

    return professors_list


def add_preparer(preparers_list):

    #MESSAGES
    msg_name = "enter the preparer's name\n===> "
    msg_last_name = "enter the preparer's last_name\n===> "
    msg_id = "enter the preparer's id:\n===> "
    msg_not_valid_character = 'What you entered is not valid.'
    msg_subject = "enter the subject that the preparer teaches\n===> "
    msg_section = "enter the section that the preparer teaches\n===> "
    msg_carnet="enter the preparer's carnet\n===> "

    #VARIABLES
    name = ''
    last_name = ''
    subject = ''
    section = ''
    carnet=''
    id = 0


    name = enter_an_input(name, msg_name, msg_not_valid_character)
    last_name = enter_an_input(last_name, msg_last_name, msg_not_valid_character)
    subject = enter_an_input(subject, msg_subject, msg_not_valid_character)
    id = enter_a_int(id, msg_id, msg_not_valid_character)
    carnet=enter_a_int(carnet,msg_carnet,msg_not_valid_character)


    preparer = Preparer(name, last_name, id, carnet, subject)

    
    section = input(msg_section)
    preparer.set_secciones(preparer.add_secciones(section))
    
    preparers_list.append(preparer)

    return preparers_list




def add_subject(student,subject):

    return student




def add_student(students_list):

    #MESSAGES
    msg_name = "enter the student's name\n===> "
    msg_last_name = "enter the student's last_name\n===> "
    msg_id = "enter the student's id:\n===> "
    msg_not_valid_character = 'What you entered is not valid.'
    # msg_section = "enter the section that the teacher teaches\n===> "
    msg_carnet="enter the student's carnet\n===> "

    #VARIABLES
    name = ''
    last_name = ''
    subjects = []
    # section = ''
    carnet=''
    id = 0


    name = enter_an_input(name, msg_name, msg_not_valid_character)
    last_name = enter_an_input(last_name, msg_last_name, msg_not_valid_character)
    
    id = enter_a_int(id, msg_id, msg_not_valid_character)
    carnet=enter_a_int(carnet,msg_carnet,msg_not_valid_character)


    student = Student(name, last_name, id, carnet)

    
    # section = input(msg_section)
    subjects = add_subjects_in_the_list(subjects)
    student.set_subjects(subjects)
    
    students_list.append(student)

    return students_list


def add_subjects_in_the_list(subjects_list):
    #MESSAGES
    msg_not_valid_character = 'What you entered is not valid.'
    msg_subject = "enter the subject \n===> "
    subject=''
    
    for x in range(5):
        subject=enter_an_input(subject,msg_subject,msg_not_valid_character)
        subjects_list.append(subject)

    
    return subjects_list
    

def show_students(students_list):

    for student in range(len(students_list)):

        print((student+1),f'''{students_list[student].get_name()} \n{students_list[student].get_last_name()}\n{students_list[student].get_id()}\n{students_list[student].get_carnet()}\n{students_list[student].get_subjects()}\n\n''')



def show_professors(professors_list):

    for professor in range(len(professors_list)):

        print((professor+1), f'''{professors_list[professor].get_name()} \n{professors_list[professor].get_last_name()}\n{professors_list[professor].get_id()}\n{professors_list[professor].get_materia()}\n{professors_list[professor].get_secciones()}\n\n''')

def show_preparers(preparers_list):

    for preparer in range(len(preparers_list)):

        print((preparer+1),f'''{preparers_list[preparer].get_name()} \n{preparers_list[preparer].get_last_name()}\n{preparers_list[preparer].get_id()}\n{preparers_list[preparer].get_carnet()}\n{preparers_list[preparer].get_secciones()}\n\n''')




