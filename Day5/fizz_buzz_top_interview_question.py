#this is a fizz buzz challenge;
for item in (range (1,101)):
    if (item %3 == 0):
        if (item % 5 == 0):
            print( f"{item} fizz_buzz");
        else:
            print(f"{item} fizz");
    if (item % 5 == 0):
        print(f"{item} buzz");