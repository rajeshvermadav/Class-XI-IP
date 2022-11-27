#Simple if statement to calculate the discount

amount = float(input("Enter Price of the item"))
qty = int(input("Enter total quantity of item"))

amt = amount*qty
disc  = amt*.10
if amt>1000:
    print("Discount is given")
    print("Discounted Amount", disc)
    pass

