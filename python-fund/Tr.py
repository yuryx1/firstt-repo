x = 10
y = 0

value = 10

while x != y:
    for i in range(value+1):
        for j in range(i):
            print("*",end="")
        print(end="\n")
    y = x


