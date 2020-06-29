import os ,sys



# for writing in file

file = open("myfile", "w+")
for i in range(1,int(sys.argv[1])+1) :
    file.write("Hello\n")

file.close()




