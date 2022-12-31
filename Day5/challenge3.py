#You got a list of number.. Write  a program to find the highest number in the
#list of the numbers
numbers = input("Enter The Numbers Seperated by a comma{,}").split(",");
var1 = [0];
for converto_floats in (numbers):
    var1.append(float(converto_floats));
#print(type(var1[len(var1)-1]));
var2 = 0;
for data in (var1):
    if( var2 < data):
        var2 = data;
print(f"The Highest Number of the list is {round(var2,3)}");