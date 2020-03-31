def id_generator(id):
    """This is a generator function for create valid ids"""
    idx=id
    while True:
        if(check_id_valid(idx)):
            yield idx
            idx+=1
        else:
            while(not check_id_valid(idx)):
                idx+=1


class IDIterator:
    """This Iterator creater valid Ids"""
    def __init__(self,id=0):
        self._id= id % 10000000000

    def add_employee(self, new_empl):
        self._employee_list.append(new_empl)

    def __iter__(self):
        return self

    def __next__(self):
        self._id+=1
        if(check_id_valid(self._id)):
            curr = self._id
            self._id+=1
            return curr
        while(not check_id_valid(self._id)):
            self._id+=1
        return self._id


def check_id_valid(id_number):
    """check if an Id is valid or not
    """
    try:
        if(str(id_number).isdigit() and len(str(id_number))!=9):
            raise InvlaidIdException(id_number)

        list_origin = [int(i) for i in list(str(id_number))] 
        list_mask = [1,2,1,2,1,2,1,2,1]
        #list_result = [int(x) * int(y) for x, y in zip(list_origin, list_mask)]
        list_result = list(map(lambda x, y : x * y, list_origin, list_mask))
        list_fixed = [sum(int(c) for c in str(num)) for num in list_result]
        if(sum(list_fixed)%10==0):
            return True
        else:
            return False
            
    
    except InvlaidIdException as e:
        print(e)




class InvlaidIdException (Exception):
    """Thrown an exception when id is not valid
    not valid len or contains alpha chars
    """
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return "Your id %s should cantains only numbers and with 9 digit" % self._id

    def get_id(self):
        return self._id

def main():
    ids = id_generator(123456780)
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    print(next(ids))
    #print(check_id_valid(123456780))
    #print(check_id_valid(123456782))
if __name__ == "__main__":
    main()