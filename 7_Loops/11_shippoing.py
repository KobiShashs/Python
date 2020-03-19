
def bye():
    print("Bye Bye!")


def show_menu():
    print("Please choose your action")
    print("\t1 - Print all items")
    print("\t2 - Print number of items")
    print("\t3 - Search if item exist by name")
    print("\t4 - Search how many times item appears in the list by name")
    print("\t5 - Remove item by name")
    print("\t6 - Add an item")
    print("\t7 - Print invalid items")
    print("\t8 - Remove All Duplicats")
    print("\t9 - Exit")

def not_support():
    print("Please insert only values between 1 to 9")

def remove_duplicates(mylist):
    #print(mylist)
    mylist = list(set(mylist))
    #print(mylist)
    return mylist

def print_illegal_items(list_args):
    res = []
    for item in list_args:
        if((len(item)<3) or (not item.isalnum())):
            res.append(item)
    
    print("illegal values "+ str(res))




def add_item_to_list(list_args):
    item_name = input("please insert product name")
    print("Going to add item...")
    list_args.append(item_name)
    print("Ited added...")


def remove_item_from_list(list_args):
    item_name = input("please insert product name")
    for item in list_args:
        if(item == item_name):
            print("Item "+item + " will be remove")
            list_args.remove(item)
            print("Item "+item + " removed")


def check_how_many_items_exist():
    item_name = input("please insert product name")
    count = 0
    for item in list_of_items:
        print("item", item)
        if(item == item_name):
            count += 1
    print(item_name + " appears " + str(count) + " times")


def check_if_item_exist(list_args):
    item_name = input("please insert product name")

    for item in list_args:
        if(item == item_name):
            print(item_name + " in " + str(list_args))
            return True
    print(item_name + " not in " + str(list_args))
    return False


def print_count(list_args):
    print("There are " + str(len(list_args))+" items")


def print_all_items(list_args):
    print(list_args)


def action_user_input():
    user_input = input()
    action = int(user_input)
    return action


def startGame(list_args):
    show_menu()
    action = action_user_input()

    while (action != 9):
        if(action == 1):
            print_all_items(list_args)
        elif (action == 2):
            print_count(list_args)
        elif (action == 3):
            check_if_item_exist(list_args)
        elif (action == 4):
            check_how_many_items_exist(list_args)
        elif (action == 5):
            remove_item_from_list(list_args)
        elif (action == 6):
            add_item_to_list(list_args)
        elif (action == 7):
            print_illegal_items(list_args)
        elif (action == 8):
            copy = list_args.copy()           
            list_args=remove_duplicates(copy)
            #remove_duplicates(list_args)
        else:
            not_support()
        show_menu()
        action = action_user_input()

    bye()


# shoppings = input("please insert you list:")
shoppings = "Milk, Cottage, Tomatoes, Milk"
list_of_items = shoppings.replace(" ", "").split(",")
for item in list_of_items:
    print("item", item)
startGame(list_of_items)


# def print_all_items():
