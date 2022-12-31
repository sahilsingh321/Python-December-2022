#Average Height Calculator
heights = (input("Enter The Height Seperated by ','  > " )).split(",");
var1 = 0;
for single_values in (heights):
    
    var1 += int(single_values);
    #Calculating the Average Height:
    average = round(var1/len(heights));
print("there you go ");
print(f"Sum is equal to {var1}");
print(f"Total Length is equal to {len(heights)}");
print(f"Average is equal to {average}");
    
