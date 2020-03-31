gen = (x ** 2 for x in [1, 2, 3])
print(dir(gen)) #generator contains __iter__ & __next__ methods!

print("-----------")

import collections,types
print(issubclass(types.GeneratorType,collections.Iterator))
# Generator is Type of Iterator

