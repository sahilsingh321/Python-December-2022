#This is a password generator in python
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
total_letter = int(input(f"How many letters you want in the password "));
total_num = int(input(f"How many numbers you want in the password "));
total_sym = int(input(f"How many symbols you want in the password "));

generated = "";

for item in (letters[0:(total_letter)]):
    generated += random.choice(letters)  ;
#print(generated);
for item in (symbols[0:total_sym]):
    generated += random.choice(symbols)  ;
for item in (numbers[0:(total_num)]):
    generated += random.choice(numbers)  ;
#print(generated);


#
generated = random.sample(generated , len(generated)); #Shuffling the list
generated = "".join(generated);

print(f"So the total generated has length of {(len(generated))} is {(generated.lower())}");

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
