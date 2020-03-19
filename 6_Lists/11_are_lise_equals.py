def are_lists_equal(list1, list2):
    print(str(list1))
    print(str(list2))
    print (str(list1)==str(list2))

# list1 = [0.6, 1, 2, 3]
list1 = [3, 2, 0.6, 1]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
are_lists_equal(list1, list2)
are_lists_equal(list1, list3)