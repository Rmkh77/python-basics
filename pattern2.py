a=int(input("enter no.of rows:"))
for i in reversed(range(a)):
    for j in range(i+1):
        print("*",end='')
    print()
