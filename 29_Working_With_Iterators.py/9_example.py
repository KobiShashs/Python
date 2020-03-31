# In your wallet you have
#3 - 20$
#5 - 10$
#2 - 5$
#5 - 1$

#How many option you can hold 100$ no returns

import itertools

wallet = [20,20,20,10,10,10,10,10,5,5,1,1,1,1,1]
result = [seq for i in range(len(wallet), 0, -1) for seq in itertools.combinations(wallet, i) if sum(seq) == 100]
print (set(result))

print(len(set(result)))

