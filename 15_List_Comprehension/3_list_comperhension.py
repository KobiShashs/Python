my_list = [1, 2, 3, 4, 5]
squared_list_for_even_only = [x * x for x in my_list if x % 2 == 0]
print(squared_list_for_even_only)


nested_list = [x*2 for x in range(10) if x>3 if x<7]
print(nested_list)

even_odd_list = ["Even" if i%2==0 else "Odd" for i in range(10) ]
print(even_odd_list)