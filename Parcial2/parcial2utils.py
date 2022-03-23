def num_verify(rangemin = 1, rangemax = 3, msg = ""):

    num = input(msg)

    if num.isnumeric():
        if int(num) <= rangemax:
            if int(num) >= rangemin:
                return int(num)
            else:
                print("ERROR INVALID NUMBER")
                return num_verify(rangemin, rangemax , msg)
        else:
            print("ERROR INVALID NUMBER")
            return num_verify(rangemin, rangemax, msg)
    else:
        print ("ERROR INVALID INPUT")
        return num_verify(rangemin, rangemax, msg)


def simple_numverify(msg):
    num = input(msg)

    if num.isnumeric():
        return num
    
    else:
        print ("ERROR INVALID INPUT")
        return simple_numverify(msg)



def verify_str(msg):
    text = input(msg)
    if text.replace(" ","").isalpha():
        return text
    else:
        print("ERROR INVALID INPUT")
        return verify_str(msg)


def yes_no (msg):
    op = input(msg)

    if op.capitalize() == "Y":
        return True
    elif op.capitalize() == "N":
        return False
    else:
        print("ERROR INVALID INPUT\n")
        return yes_no(msg)


def fibonacci(num_tofind, num0, num1):

    limit = 100
    num0 = 0
    num1 = 1
    
    if num1 != num_tofind:
        if num1 < limit:
            return fibonacci(num_tofind, num0 + num1, num0 +num1)
    else:

        return True
