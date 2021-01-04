my_list = [1, 2, 3, 4, 5, 6]

#my_list2 =  list(range(1,102, 9))
print(my_list)
#print(my_list2)
#print(type(my_list))

# Operations on lists:
# -1 gives the last element in the list
# 0 gives the first element in the list
print(my_list[-1])

#Let's create a slice from the 2nd element to the 4th element
print(my_list[1:4])

#length of the list
print(len(my_list))

# Maximum and minimum of the list
print(max(my_list))
print(min(my_list))

#Add an element onto our list
my_list.append(120)
print(my_list)

#Reverse a list
#my_list.reverse()
print(my_list)

#Create another list and add two lists together
my_list2= [10, 20, 30, 40, 50]
print(my_list+my_list2)
