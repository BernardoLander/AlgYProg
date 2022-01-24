table = int(input("Please choose a base number for the table:\n"))

for i in range (1,11):
    print(table, str(i) + f" = {table * i}", sep=" x ")