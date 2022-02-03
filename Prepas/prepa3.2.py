a = [
    [1,4,6],
    [4,2,5],
    [6,5,3]
]

numb = input("Please give me number to multiply the matrix to\n==>")

if numb.isnumeric():

    numb = int(numb)

    for x in range(len(a)):

        for y in range(len(a[x])):
            h=a[x][y] * numb
            a[x].pop(y)
            a[x].insert(y,h)

print (a)
