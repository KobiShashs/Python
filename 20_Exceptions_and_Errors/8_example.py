# StopIteration


def throw_stop_iteration_error():
    x = ['Hey', 'there', 'Python', 'programmers']
    obj = iter(x)  # using iter function for x
    next(obj)  # Iteration 1 using next function
    next(obj)  # Iteration 2
    next(obj)  # Iteration 3
    next(obj)  # Iteration 4
    next(obj)  # Iteration 5

# ImportError


def throw_import_error():
   import moshe


def throw_assertion_error():
    x = "hello"
    # if condition returns True, then nothing happens:
    assert x == "hello"
    # if condition returns False, AssertionError is raised:
    assert x == "goodbye"
# IndentationError


def throw_indentation_error():
    if 3 == 3:
        print("True")  # This line isn't in the right place
    else:
        print("False")


# SyntaxError

def throw_syntax_error():
    print("Moshe")  # removed last ")"
# ZeroDivisionError


def throw_division_error(x):
    print(x/0)


# KeyError


def throw_key_error():
    ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
    print(ages['Michael'])


# TypeError

def throw_type_error(x, y):
    print(x+y)


def main():
    pass
    #throw_stop_iteration_error()
    #throw_import_error()
    # throw_assertion_error()
    # throw_indentation_error()
    # throw_syntax_error()
    # throw_division_error(3)
    # throw_key_error()
    #throw_type_error('k', 4)
main()
