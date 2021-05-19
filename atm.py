class Atm:
    def __init__(self,cardnumber,pin):
      self.cardnumber= cardnumber
      self.pin= pin

    def check_balance(self):
        print("your balance is 7000")  

    def withdrawl(self,amount):
        new_amount= 7000-amount 
        print("you have withdrawed"+str(amount)+"your remaining amount is"+str(new_amount)) 

def main():
    Card_number= input("insert you card number:")
    Pin_number= input("enter you pin:")
        
    new_person= Atm(Card_number,Pin_number)
    print("choose your action to be done")
    print(" 1. balance enquiry  2. withdrawl")
    activity= int(input("enter activity number:"))

    if(activity == 1):
        new_person.check_balance()
    elif(activity == 2):
        amount=int(input("enter amount:"))
        new_person.withdrawl(amount)
    else:
        print("enter a valid number")   





if __name__ == "__main__":
    main()







