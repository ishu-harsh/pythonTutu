num = int(input("Enter Your Number : "))

factorial = 1

if num < 0 :
    print ("  please enter positive number  :")
elif num == 0 :
    print ("factorial is")
else : 
    for i in range(1, num+1):
        factorial = factorial*i

print (factorial)