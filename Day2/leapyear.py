year = int(input("Year : "))
if (year % 4 == 0):
    if (year % 100 == 0 ):
        if(year % 400 == 0 ):
            print("Leap");
        else:
            print("Not a Leap!");
    else:
        print("Leap year;");

else:
    print("Not a Leap Year  !");
