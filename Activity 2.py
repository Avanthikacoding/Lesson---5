actual_cost = float(input("Enter you actual cost of your item:"))
selling_price = float(input("Enter your selling price of your item"))
if (selling_price > actual_cost):
    amount = selling_price - actual_cost
    print("You made a profit of " , amount , " ! Well done!") 

else:
    print("You made no profit! Oh no!")

    