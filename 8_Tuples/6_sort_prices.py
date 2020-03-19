def sort_prices(list_of_tuples):
    last = len(list_of_tuples)
    for i in range(0, last):
        for j in range(0, last-i-1):
            if (list_of_tuples[j][1] > list_of_tuples[j + 1][1]):
                temp = list_of_tuples[j]
                list_of_tuples[j] = list_of_tuples[j + 1]
                list_of_tuples[j + 1] = temp

    return list_of_tuples

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(products)
sort_prices(products)
print(products)
