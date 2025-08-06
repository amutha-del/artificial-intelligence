# Initial list
my_list = [1, 2, 3]
print("Original list:", my_list)

# 1. Add lists using + operator (creates a new list)
list2 = [4, 5]
new_list = my_list + list2
print("After add (+):", new_list)

# 2. Append an element (adds single element at end)
my_list.append(6)
print("After append(6):", my_list)

# 3. Extend list by another list (adds all elements)
my_list.extend([7, 8])
print("After extend([7, 8]):", my_list)

# 4. Delete element by index using del
del my_list[1]  # deletes element at index 1
print("After del my_list[1]:", my_list)

# 5. Delete element by value using remove()
my_list.remove(7)  # removes first occurrence of 7
print("After remove(7):", my_list)
