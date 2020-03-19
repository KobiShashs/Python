def inverse_dict(my_dict):
    my_inverted_dict = dict(map(reversed, my_dict.items()))
    return(my_inverted_dict)

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
#{3: ['I', 'love'], 2: ['self.py!']}