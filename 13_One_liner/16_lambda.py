import functools

print((lambda x,y: x+y)(2,5))

shopping_list = [200, 120, 330, 50]
print(functools.reduce((lambda x,y: x+y), shopping_list))


new_add = (lambda x,y: x+y)
print(functools.reduce(new_add, shopping_list))
