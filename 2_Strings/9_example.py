word = "spaceship"
# e,p,p
print('e' not in word)
#False
print(word.isspace())
#False
print(word.count('p'))
##2
print(word.find('sh'))
#5
print(word.endswith('e'))
#False
print(len(word))
#9
print(word[-2::-4])
#ic
print(word.startswith('spa'))
#True