try:
    if '1' != 1:
        raise "SomeError" #Not valid
    else:
        print("SomeError has not occurred")
except "someError":
    print("SomeError has occurred")