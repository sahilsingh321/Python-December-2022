# Date : October 28th
#Topic BMI Calculator
(height) = input("Hey input your Height in Meters ");
(weight) = input("Hey input your weight in Kilograms ");
bmi = (float(weight) / (float(height)) ** 2);
print("your Bmi = " + str(round(bmi)));
