# Python3 code to demonstrate  
# removing consecutive duplicates 
# using groupby() + list comprehension 
from itertools import groupby  
def sequence_del(my_str):
# using groupby() + list comprehension 
# removing consecutive duplicates  
    res = [i[0] for i in groupby(my_str)] 
    print(str(res))
    
sequence_del("ppyyyyythhhhhooonnnnn")
#'python'
sequence_del("SSSSsssshhhh")
#'Ssh'
sequence_del("Heeyyy   yyouuuu!!!")
#'Hey you!'


