#This is the love calculator made by Sahil in python
#Date : 7th Nov 2023
name1 = input("Enter the Name 1 : ");
name2 = input("Enter the Name 2 : ");

name1 = name1.lower();
name2 = name2.lower();

name3 = name1+name2;
print(name3);
t = name3.count("t");
r = name3.count("r");
u = name3.count("u");
e = name3.count("e");
true = (t+r+u+e);
l = name3.count("l");
o = name3.count("o");
v = name3.count("v");
e = name3.count("e");
love = (l+o+v+e);
print(f"T occur {t} times");
print(f"R occur {r} times");
print(f"U occur {u} times");
print(f"E occur {e} times");
print(f"Total Letters in True {true} ")
print(f"L occur {l} times");
print(f"O occur {o} times");
print(f"V occur {v} times");
print(f"E occur {e} times");
print(f"Total Letters in Love {love}");

lovePercentage = str(true) + str(love)
lovePercentage = int(lovePercentage);
print(f"Your Love Percentage is {lovePercentage} ");
