def sneaky_func(thing):
    try:
        print("A" + thing)
        return
    except:
        print("B")
    else:
        print("C")
    finally:
        print("D")


sneaky_func("Moshe")
print("------")
sneaky_func(17)