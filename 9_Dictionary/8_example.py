def count_chars(my_str):
    my_dict = dict()
    from collections import Counter
    my_dict = Counter(my_str)
    return my_dict

magic_str = "abra cadabra"
print(count_chars(magic_str))
#{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


