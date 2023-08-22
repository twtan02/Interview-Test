def find_intersection(list1, list2):
    intersection = []
    
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                intersection.append(item1)
    
    return intersection

list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

# Print the results
result = find_intersection(list1, list2)
print(result)
