print("Welcome to the rolar coster ride\n");
height = int(input("Hey Bro Enter your height"));
if (height > 180):
    print("You Can Ride");
    age = int(input("Hey Please tell me you age"));
    if (age < 12):
        bill = 7;
    elif (age <=18):
        bill = 12;
    else:
        bill = 18;
    want_pic = input("Hey Do you want a picture? Y or N " );
    if (want_pic == "Y"):
        bill += 2;
else:
    print(f"No you can't ride");
print(f"So bro your total bill is {bill}");
