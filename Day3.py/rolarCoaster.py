print(''' Welcome To Sahil's Rolar Coaster ''');
height = int(input("Hey Enter Your Height\n : "));
if (height > 120):
    print(f"Ok Your height is {height} which is more then 120 ");
    age = int(input("Hey Enter Your Age Brother\n : "))
    if ( age <= 12):
        bill = 6;
    elif (age > 12 and age < 18):
        bill = 7;
    elif ( age > 18 and age < 44):
        bill = 12
    elif( age>=45 and age <= 55):
        bill = 0;
    else:
        print(f"You didn't write your age")


    pic = input("Do you want Picture Y or N : ")

    if (pic == "Y"):
        bill += 3;
        print(f"Your Total Bill {bill}");
    else:
        bill += 0;
        print(f"Your total bill {bill}")
else:
    print(f"Sorry Bro, You need to grow taller to ride the rolar coaster");
