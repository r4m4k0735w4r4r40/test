class String():
    def __init__(self,s):
        self.s = s
        self.l = list(s)

    # Converting string to list.
    def __to_list(self) -> list:
        return list(self.s)

    # Converting list to stirng.
    def __to_string(self) -> str:
        return ''.join(self.l)

    # Update value of String object.
    def setTo(self,string:str) -> None:
        self.s = string
        self.l = self.__to_list()

    def __repr__(self):
        return self.s

    def sort(self):
        self.l = sorted(self.s)
        self.s = self.__to_string()

    # Update value of String object at particular index.
    def update(self,index:int,charecter:str) -> None:
        try:
            if len(self.s) > index:
                self.l[index] = charecter
                self.s = self.__to_string()
            else:
                raise "Eception"
        except:
            self.__error('Update')

    # Append string to String object.
    def append(self,string:str) -> None:
        try:
            self.s += string
            self.l = self.__to_list()
        except:
            self.__error('Append')

    # Remove value at particular index in String object.
    def remove(self,index:int) -> None:
        self.l = self.l[0:index] + self.l[index + 1:]
        self.s = self.__to_string()

    #Pop last value of String object.
    def pop(self) -> None:
        try:
            if len(self) == 0:
                raise 'Exception'
            else:
                self.l = self.l[0:-1]
                self.s = self.__to_string()
        except:
            self.__error('Pop','String object is empty')

    # Printing error to console.
    def __error(self,op=None,err='Looks something error') -> None:
        if op == None:
            print('error:Unable to perform operation. {}.'.format(err))
        else:
            print('error:Unable to perform {} operation. {}.'.format(op,err))