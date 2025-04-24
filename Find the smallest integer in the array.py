array = [34, 15, -88, 2]

smallest = array[0]
for i in array:
    if i < smallest:
        smallest = i

# smallest = min(array)

print(smallest)