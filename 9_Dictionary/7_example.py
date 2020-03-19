my_dict = {"first_name":"John","last_name":"Snow","birthday":"24/06/74","hobbies":["Sing","Act","Golf"]}
print(my_dict)

print(my_dict["last_name"])
print(str(my_dict["birthday"])[3:5:1])
print(len(my_dict["hobbies"]))
print(my_dict["hobbies"][-1])
my_dict["hobbies"].append("Cooking")
print(len(my_dict["hobbies"]))
birthday_tuple = (str(my_dict["birthday"])[0:2:1],str(my_dict["birthday"])[3:5:1],str(my_dict["birthday"])[6:8:1])
print(birthday_tuple)
gender=input("insert gender: ")

my_dict["gender"]=gender
print(my_dict)
