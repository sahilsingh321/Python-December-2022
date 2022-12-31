list1 = ["x","x","x"]
list2 = ["x","x","x"]
list3 = ["x","x","x"];
list4 = [list1,list2,list3];
print(f"{list1}\n{list2}\n{list3}\n")
print(f"Where do you want to put your treasure");
co_ordinates = input(">> ")
hori =(co_ordinates[0]);
ver = (co_ordinates[1]);
ver = int(ver);
hori = int(hori);
ver = ver-1
hori = hori-1
print(type(hori));
list4[ver][hori] = "o"
print(f"{list1}\n{list2}\n{list3}\n");
