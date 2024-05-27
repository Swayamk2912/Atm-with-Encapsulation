#we will make a atm with the use of oops method which is encapsulation:


print("Hello Sir/Mam,\nWelcome to Sk Bank")


class atm:
    def __init__(self):
        self.bal=100000
        
    def __withdraw(self):
        self.amt=int(input("Enter The Amount You want to Withdraw:"))
        if self.amt<=self.bal:
            print("Transaction Successful")
            self.bal=self.bal=self.amt
            print(f"Current Account Balance:{self.bal}")
            
        else:
            print("Insufficient Balance In your Account")
            
            
    def __deposit(self):
        self.amt=int(input("Enter Amount to deposit:"))
        self.bal=self.bal+self.amt
        print("Transaction Successful. ")
        
    def __balenq(Self):
            print("Your Current Account Balance is:",Self.bal)
            
    def login(self):
        self.pinent=int(input("Enter Your Pin:"))
        self.pin=1234
        if self.pinent!=1234:
            print("Incorrect Pin,Kindly Enter The Pin again")
            
        else:
            while True:
                self.choice=int(input("Enter 1 For Withdraw\nEnter 2 For Deposit\nEnter 3 For Balance Enquiry\nEnter 4 To Exit"))
                if self.choice==1:
                        self.__withdraw()
                elif self.choice==2:
                    self.__deposit()
                    
                elif self.choice==3:
                    self.__balenq()
                    
                else:
                    print("Thanks For Visiting.......")
                    break             
                
obj=atm()
obj.login()           
            
        
               
        