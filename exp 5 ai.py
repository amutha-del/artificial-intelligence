# List Operations in Python

# 1. Nested List
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)
print("Accessing Nested Element [1][2]:", nested_list[1][2])  # Output: 6

# 2. Length of List
my_list = [10, 20, 30, 40, 50]
print("\nOriginal List:", my_list)
print("Length of the List:", len(my_list))

# 3. Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print("\nList1:", list1)
print("List2:", list2)
print("Concatenated List:", concatenated)

# 4. Membership
print("\nIs 20 in my_list?", 20 in my_list)
print("Is 100 in my_list?", 100 in my_list)

# 5. Iteration
print("\nIterating through my_list:")
for item in my_list:
    print(item, end=' ')

# 6. Indexing
print("\n\nFirst element of my_list:", my_list[0])
print("Last element of my_list:", my_list[-1])

# 7. Slicing
print("\nFirst three elements of my_list:", my_list[:3])
print("Elements from index 2 to end:", my_list[2:])
print("Middle elements of my_list:", my_list[1:4])
