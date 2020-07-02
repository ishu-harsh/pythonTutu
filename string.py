mystring = "this is Vs Code"

print(mystring[1])
print(mystring)
print(len(mystring))
print("is" in mystring)
print(mystring[0:5]) #indexing in string 


mystring2 = "i am devops engineer and python programmer"

print (mystring2.capitalize())
print (mystring2.upper())
print (mystring2.count("p"))
print (mystring2.count("i", 1, len(mystring2)))



course = "python"
day = "monday"

print("this is %s class. Today is %s" %(course, day))


print (course.find("m")) # will find 
print (day.index("m")) 


print(mystring2[5:11]) # slicing 
print (mystring2[::-1]) #reverse string
print(mystring2*3)