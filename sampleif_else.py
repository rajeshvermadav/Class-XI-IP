# Sample program if-else conditional statement

price = float(input("Enter a price"))
qty = float(input("Enter Quantity"))
amt = price*qty
if amt>1000:
    disc = amt*0.10
    print("Discount", disc)
else:
    disc= amt * 0.05
    print("Discount", disc)
