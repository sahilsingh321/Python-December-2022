#In this module we are going to add all the even numbers from 1 to 100;
number = 0;
for items in (range(1,101)):
    if (items % 2 == 0):
        number += items;
print(number);