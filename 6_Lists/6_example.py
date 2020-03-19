def format_list(my_list):
   print(str(my_list))
   print(str(my_list[:]))
   print(str(my_list).strip('[]'))
   print(", ".join(map(str,my_list)))

format_list(['moshe','david','kobi',"kobi"])