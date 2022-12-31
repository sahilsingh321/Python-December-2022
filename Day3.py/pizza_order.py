print("Welcome to Sahil's Pizza");
print(''' For Small { $15 }
          For Medium { $20}
          For Large { $25 }''')
small = 15;
medium = 20;
large = 25;
size = input("Which size do you want to order?  S , M , L : ");
if (size == "S"):
    print(f"You Choose Small The Price is ${small}");
    price = small;
elif (size == "M"):
    print(f"You Choose Medium the Price s ${medium}");
    price = medium;
elif ( size == "L"):
    print(f"You Choose Large the price is ${large}");
    price = large;
else:
    print(f"You Didn't Choose Anything")
print('''Pepper for Small : $2
         Pepper for Medium or Large : $3''')
pepper_ment = input("Do You want pepper ? S or L : ");
if (pepper_ment == "S"):
    print(f"You Choose Pepper for Small , price : $2");
    price += 2;
elif (pepper_ment == "L"):
    print(f"You Choose Pepper for Large , price : $3");
    price += 3;
else :
    print(f"Pease Choose The Correct Option");
cheese = input("Do you want cheese , price {$1} , Y or N");
if (cheese == 'Y'):
    print(f"You Choose Cheeze , price : $1");
    price += 1;
print(f"So the total price if ${price}");
