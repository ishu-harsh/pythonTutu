import sys , os

arg = int(sys.argv[1])
name = sys.argv[3]
cname= sys.argv[2]
rename = os.rename(cname, name)

file = open(name, "r+")


# print (file.read(arg))
print (os.getcwd())
print (file.mode)
print (file.name)
file.seek(7)
print (file.read(arg))

file.close()


#python3 read_file.py 30 cname newname 