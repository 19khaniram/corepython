num = int(input("Enter Number="))
count = 0
for x in range (10,num):
    for i in range(2,x):
        if (x % i == 0):
            count += 1
            break
    if(count == 0):
    print("Prime Number is",x)
count=0