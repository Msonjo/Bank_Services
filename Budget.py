import sys
import datetime
now = datetime.datetime.now()

class budget():
	def __init__(self,total_balance):
		self.total_balance = total_balance

food = budget(500)
clothing = budget(0)
entertainment = budget(0)

print("________Welcome________")
print( "Today is: ", now)
print("These are the available options: ")
print("1. Withdrawal")
print("2. Cash Deposit")
print("3. Transfer")
print("4. Complaint")

selectedOption = int(input("Please select an option: "))

if(selectedOption == 1):
	print("You selected %s" % selectedOption)
	print("This are the available accounts to withdraw from")
	print("1. Food Account")
	print("2. Clothing Account")
	print("3. Entertainment Account")

	selectOption = int(input("Please select an option: "))
    
	if(selectOption == 1):
		print("You selected %s" % selectOption)
		withdraw = int(input("How much would you like to withdraw? "))

		if(withdraw < food.total_balance):
			print("Take your cash ", withdraw)
			print("--------------------------")
			print("Your available balance is", food.total_balance -  withdraw)

		else:
			print("You do not have enough credit please recharge!")
            
	elif(selectOption == 2):
		print("You selected %s" % selectOption)
		withdraw = int(input("How much would you like to withdraw? "))

		if(withdraw < clothing.total_balance):
			print("Take your cash ", withdraw)
			print("--------------------------")
			print("Your available balance is", clothing.total_balance -  withdraw)

		else:
			print("You do not have enough credit please recharge!")
            
	elif(selectOption == 3):
		print("You selected %s" % selectOption)
		withdraw = int(input("How much would you like to withdraw? "))

		if(withdraw < entertainment.total_balance):
			print("Take your cash ", withdraw)
			print("--------------------------")
			print("Your available balance is", entertainment.total_balance -  withdraw)

		else:
			print("You do not have enough credit please recharge!")
            
elif(selectedOption == 2):
    print("You selected %s" % selectedOption)
    print("This are the avaible options to deposit to")
    print("1. Food Account")
    print("2. Clothing Account")
    print("3. Entertainment Account")
    
    selectOption = int(input("Please select an option: "))
    
    if(selectOption == 1):
        print("You selected %s" % selectOption)
        deposit = int(input("How much would you like to deposit? "))
        food.total_balance += deposit
        print("-------------------------")
        print("Your available balance is", food.total_balance)
        
    elif(selectOption == 2):
        print("You selected %s" % selectOption)
        deposit = int(input("How much would you like to deposit? "))
        clothing.total_balance += deposit
        print("-------------------------")
        print("Your available balance is", clothing.total_balance)
        
    elif(selectOption == 3):
        print("You selected %s" % selectOption)
        deposit = int(input("How much would you like to deposit? "))
        entertainment.total_balance += deposit
        print("-------------------------")
        print("Your available balance is", clothing.total_balance)
        
elif(selectedOption == 3):
    print("You selected %s" % selectedOption)
    print("This are the avaible options to transfer to")
    print("1. Food Account")
    print("2. Clothing Account")
    print("3. Entertainment Account")
    
    selectOption = int(input("Please select an option: "))
    
    if(selectOption == 1):
        print("You selected %s" % selectOption)
        print("This are the avaible options to transfer from")
        print("1. Clothing Account")
        print("2. Entertainment Account")
        
        selectOption = int(input("Please select an option: "))
        
        if(selectOption == 1):
            print("You are transfering from Clothing Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < clothing.total_balance):
                print("You have transferred", transfer)
                print("Your Food Account has been replenished. Total available credit is", food.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
                
        elif(selectOption == 2):
            print("You are transfering from Entertainment Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < entertainment.total_balance):
                print("You have transferred", transfer)
                print("Your Food Account has been replenished. Total available credit is", food.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
                
    elif(selectOption == 2):
        print("You selected %s" % selectOption)
        print("This are the avaible options to transfer from")
        print("1. Food Account")
        print("2. Entertainment Account")
        
        selectOption = int(input("Please select an option: "))
        
        if(selectOption == 1):
            print("You are transfering from Food Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < food.total_balance):
                print("You have transferred", transfer)
                print("Your Clothing Account has been replenished. Total available credit is", clothing.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
                
        elif(selectOption == 2):
            print("You are transfering from Entertainment Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < entertainment.total_balance):
                print("You have transferred", transfer)
                print("Your Food Account has been replenished. Total available credit is", clothing.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
            
    if(selectOption == 3):
        print("You selected %s" % selectOption)
        print("This are the avaible options to transfer from")
        print("1. Food Account")
        print("2. Clothing Account")
        
        selectOption = int(input("Please select an option: "))
        
        if(selectOption == 1):
            print("You are transfering from Food Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < food.total_balance):
                print("You have transferred", transfer)
                print("Your Entertainment Account has been replenished. Total available credit is", entertainment.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
                
        elif(selectOption == 2):
            print("You are transfering from Clothing Account")
            transfer = int(input("How much would you like to transfer: "))
            
            if(transfer < clothing.total_balance):
                print("You have transferred", transfer)
                print("Your Entertainment Account has been replenished. Total available credit is", entertainment.total_balance + transfer)
                
            else:
                print("There is no enough credit for the transfer to be initiated")
        
elif(selectedOption == 4):
    print("Your Complaint has been recorded we will get to you soon")
    print("Thank you for your humility")
    
