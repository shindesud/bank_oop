from random import *
from abc import abstractmethod,ABC
class Savings(ABC):
    @abstractmethod
    def createaccount(self):
        pass
    @abstractmethod
    def authentication(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def checkbalance(self):
        pass

class Account:
    def __init__(self):
        ##key[0]= name & key[1]=initialdeposit
        self.savingsaccount={}
        
    def createaccount(self,name,initialdeposit):
        self.accountno=randint(10000,99999)
        self.savingsaccount[self.accountno]=[name,initialdeposit]
        print('Account created successfully and account no is:',self.accountno)
        

    def authentication(self,name,accountno):

        if accountno in self.savingsaccount.keys():
            if self.savingsaccount[accountno][0]==name:
                print("Authentication successful")
                self.accountno=accountno
                return True
            else:
                print("Authentication unsuccessful")
                return False
        else:
            print('Authentication Failed')
            return False
        
    def withdraw(self,withdrawamount):
        if self.savingsaccount[self.accountno][1]<withdrawamount:
            print('withdrawal amount is more,Insufficient Balance')
        else:
            self.savingsaccount[self.accountno][1]-=withdrawamount
            print('Withdrawal successful')
            print('Available balance after withdrawal is:')
            self.checkbalance()

    def deposit(self,depositamount):
        self.savingsaccount[self.accountno][1]+=depositamount
        print("Amount Deposited successfully")
        print('Available balance after depositing money is:')
        self.checkbalance()

    def checkbalance(self):
        print(self.savingsaccount[self.accountno][1])

account=Account()
while True:
    print("1.create an account\n",
          "2.access existing account\n",
          "3.exit")
    
    ch=int(input('enter choice'))
    if ch==1:
        
        name=input('enter name')
        initialdeposit=int(input('enter iniitial deposit'))
        account.createaccount(name,initialdeposit)
    elif ch==2:
        
        print('enter name')
        name=input()
        print('enter account number')
        accountno=int(input())
        status=account.authentication(name,accountno)
        if status is True:
            while True:
                print("1.withdraw")
                print("2.deposit")
                print("3.checkbalance")
                print('break')
                ch=int(input('enter you choice'))
                if ch==1:
                    withdrawamount=int(input('enter withdrawal amount'))
                    account.withdraw(withdrawamount)
                elif ch==2:
                    depositamount=int(input('enter amount to deposit'))
                    account.deposit(depositamount)
                elif ch==3:
                    account.checkbalance()
                elif ch==4:
                    break
        
    elif ch==3:
            quit()

            



        







        
        
