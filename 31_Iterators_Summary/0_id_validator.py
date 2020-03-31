

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
        print(list_result)
        list_fixed = [sum(int(c) for c in str(num)) for num in list_result]
        print(list_fixed)
        if(sum(list_fixed)%10==0):
            print("True")
        else:
            print("False")
    
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
    print(check_id_valid(123456780))
    print(check_id_valid(123456782))
if __name__ == "__main__":
    main()