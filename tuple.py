mytup = ("python", "machine learning", "nodejs", "react")

print (len(mytup))
print (max(mytup))
print (min(mytup))

# multiplication 

print (mytup * 2)


# sorted  in  Alpha order

print (sorted(mytup))

# membership checking
 
print ("python" in mytup, "php" in mytup)

#  deleting tuple
del(mytup)
# print(mytup)


mytup1 = ([1,2,3], [5,6,7], ["kay", "jay", "ishu"])
print (list(mytup1))  # converting tuple into list 


for i in mytup1 :
    print(tuple(i))  # converts list into tuple
    print(i)