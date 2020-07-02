mylist =  ["jay", "pakcie", "jhon", "hacker"]
mylist2 =  ["orange" , "pinaple", "Almonds"]
# print (mylist[0]) # 0 index value 
# print (mylist[-1]) # print jhon
# print (mylist[-2]) 
# print (mylist[-3])
# print (mylist[0:2])


# cnctnte = (mylist +  mylist2) 
# print(cnctnte)
# print (cnctnte * 2)
# print ("kali" in cnctnte, "jay" in mylist)

# updating listhackerhacker""
# mylist[1] = "harsh"
# print(mylist)

# deleting 
# del(mylist[0])
# print(mylist)



# pop  and remove


print(mylist.pop(2))
print(mylist)
print(mylist2.remove("Almonds"))
print(mylist2)


# append

mylist2.append("moti")
print(mylist2)

# extend

mylist3 = sorted(["new", "kali", "pow"])
# mylist3.extend(mylist2)
print(mylist3)
print(mylist3[1])

# insert 
mylist3.insert(1, "jay")
print(mylist3)

# sorted - will sort list in Alpha order
print(sorted(mylist3 + mylist2 + mylist))


# reverse 
for i in mylist3[::-1] :
    print(i)


# tuple in lis
tup_list = [(3,"jay", 6), "monkey", "banana"]
print (tup_list[0][0:2])