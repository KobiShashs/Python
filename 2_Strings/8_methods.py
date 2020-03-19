print("print me in UPPERCASE".upper())
print("234".zfill(5))
print("1".zfill(5))

word = "Moshe"
print('e' in word)
print('e' not in word)

word = " "
print(word.count('p'))
print(word.find('irt'))
print(word.startswith('Ha'))
print(word.startswith('Ka'))
print(word.endswith('y'))
print(word.endswith('r'))
print(word[-2::-4])
print(word.isspace())

str = 'pythonexamples125'
isalnum = str.isalnum()
print('Is String Alphanumeric :', isalnum)