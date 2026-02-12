balance = 0.0  #Global variable
kyc_documents = {} #empty dictionary

def check_balance():
    print("checking Balance")
    print(f"Your current balance is : {balance}")
    print("-------------------------------")

def deposite_money(amount):
    global balance
    if amount > 0:
        balance = amount + balance
    else:
        print("Cannot add negative or zero amount.")
        print("-------------------------------")

def withdraw_money(amount):
    global balance
    if amount <= 0:
        print("Cannot withdwar negative or zero amount")
        print("-------------------------------")
    elif amount > balance:
        print("Cannot withdrwa. Insufficient balance...")
        print("-------------------------------")
    else:
         balance = balance - amount
         print(f"The amount {amt} withdrawn successfully....")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("Your KYC is not done")
        print("-------------------------------")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")
            print("-------------------------------")


if __name__ == "__main__": # it dont show unnecesserily code
    print("-------------------------------")
    print("Welcome to Apna Ghar ka Bank..")
    print("-------------------------------")
    print() # To enter empty line
    while True:
        print("1. Check balance")
        print("2. Deposite an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("enter your choice (1-6): ")
        print("-------------------------------")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter amount to be deposite : "))
            deposite_money(amt)
            print(f"The amount {amt} depositted successfully....")
        elif choice == '3':
            amt = float(input("Enter amount to withdraw : "))
            
            withdraw_money(amt)
            
        elif choice == '4':
            check_kyc()
            
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add : "))
            for i in range(n_documents):
                key = input("Enter the document type : ")
                value = input("Enter the document number : ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"Kyc Updated...")
        elif choice == '6':
            print("Quitting...., Have a nice day")
            break
        else:
            print("Invalid choice!! Please try again")
            print("-------------------------------")
    print()    
    print("Thankyou for banking with us...")
