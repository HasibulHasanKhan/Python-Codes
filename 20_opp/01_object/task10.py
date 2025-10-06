# Encapsulation : practice of protecting internal object data from being directly accessed or modified from outside the clas

class Bank:
    def __init__(self, balance):
        self._balance = balance
        self.__pin = 1234

    def check_balance(self):
        return self._balance
    

b = Bank(700)
print(b.check_balance())
# print(b.__pin)  ❌ Error (private)