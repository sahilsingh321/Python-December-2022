# This is the tip calculator in python
print("Welcome to the tip calculator in python ");
totalBill = float(input("What was the total bill $ "));
tip = float(input("How much tip would you like to give 10 , 12 or 15 ? "));
toDivide = float(input("Among how many people would you like to divide the tip ? "));
bill = (((totalBill * tip / 100) + totalBill) / toDivide) ;
#bill == round(bill,2);
print(f"So each user should pay {round(bill,2)} amont of the money");
