my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

# Get the first item
item1 = next(my_iterator)
print(item1)  # Output: 1

# Without calling next again, the iterator stays at the current position
# Subsequent calls to next will continue from the same position
item2 = next(my_iterator)
print(item2)  # Output: 2

# Now, call next again to get the next item
print(item2)  # Output: 3