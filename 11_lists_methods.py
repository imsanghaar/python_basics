#  Lists Methods

# append 
# insert
# pop
# len 
# sort 
# reverse
# index
#Remove

# Append Method
numbers_list = [1,2,3,4,6,7,8]
print("List before append", numbers_list)
# append
numbers_list.append(9)
numbers_list.append(10)
numbers_list.append(11)
print("List after append", numbers_list)

# Insert Method
number = [1,2,3,4,6,7,8]
print("List before insert", number)
number.insert(9,10)
print("List after insert", number)

#  pop
p = [1,2,3,4,5]
p.pop()
print(p)

# remove
ls = [1,2,3,4,6,7]
print("List before remove", ls)
ls.remove(2)
print("List after remove", ls)


#  len (length)
num = [1,2,3,6,8] # length = how many elements are there in the list = 5
print("Before the length", num )
print("The length of num is: ", len(num)) 