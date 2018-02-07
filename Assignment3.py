# Input and comparisons Biren 3008

string = open("strings.txt","r")

a = []
b = []

for i in range(0,1) :
    a.append((string.readline()))
    a[i] = a[i].replace('\n','')
    b.append((string.readline()))

for odd in range(0,1) :
    print("Odd number list from string file :")
    print ((a[odd]))

for even in range(0,1) :
    print("Even number list from string file :")
    print ((b[even]))
