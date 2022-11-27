#Enter Character is Uppercase,Lowecase,digit or special character
choice = 'Y'
while choice == 'Y'  or choice == 'y':
 ch = input("Enter any Character from the keyboard:-")
 if ch >= 'A' and ch <= 'Z':
    print("You have entered Capital Letter")
 elif ch >= 'a' and ch <='z':
    print("You have entered lowercase alphabate")
 elif ch >= '0' and ch <= '9':
    print("You have entered a number")
 else:
    print("You have entered a special character")

 choice = input("Do you want to continue Y/N....?")
 if choice == 'Y' or choice == 'y':
     continue





    



