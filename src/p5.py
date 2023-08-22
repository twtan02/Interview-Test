def symmetric_difference(list1, list2):
    symmetric_diff = []
    
    for item1 in list1:
        if item1 not in list2:
            symmetric_diff.append(item1)
    
    for item2 in list2:
        if item2 not in list1:
            symmetric_diff.append(item2)
    
    return symmetric_diff

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

# Print the results
result = symmetric_difference(list1, list2)
print(result)
