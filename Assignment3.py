# Input and comparisons Biren 3008

string = open("string.txt","r")

odd_even = input(str("What type of lines you want to print Odd Or Even? : "))

count = 0
for line in string.readlines() :
    
    if odd_even == "Even":
        
        if count % 2 == 0:
            print("Even index %d line from string file is :" %count)
            print(line)
        count += 1
    
    if odd_even == "Odd":
        
        if count % 2 == 1:
            print("Odd index %d line from string file is :" %count)
            print(line)
        count += 1
   

        
