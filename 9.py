#encaptulation example 
class Bankaccount:
    def __init__ (self,account_number,balance):
        self._account_number=account_number
        self._balance=balance
    def get_balance(self):
        return self._balance
account1=Bankaccount("12345",1000)
print(account1._account_number)
print(account1.get_balance())