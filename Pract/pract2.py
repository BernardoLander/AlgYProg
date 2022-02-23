from email import message


def greet(first_name,last_name):
    print(f"Hi there {first_name} {last_name}")


greet("rober","pat")
greet("rammen","noodles")

#funtiones that permorm a task
#return a value

def get_greeting (name):
    return f"hi {name}"


message = get_greeting("Mosh")
file = open("content.txt", "w")
file.write(message)

