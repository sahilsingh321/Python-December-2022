alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
test_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("input the text > ").lower()
text = list(text);
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
    main_engine = 0;
    temp_engine = 0 ;
    new_list = [];
    while main_engine < len(text):
        
        if( text[temp_engine] in alphabet) == True:
            index_of_list = alphabet.index(text[temp_engine]);
            index_of_list += shift;
           
            new_list.append(alphabet[index_of_list]);
            main_engine+=1;
            temp_engine+=1;
            
    print(f"The encoded text is " + "".join(new_list));
    
                            
        
    
def decrypt():
    main_engine = 0;
    temp_engine = 0 ;
    new_list = [];
    decrypt_2 = input("text to decrypt > ")
    while main_engine < len(text):
        
        if( decrypt_2[temp_engine] in alphabet) == True:
            
            index_of_list = alphabet.index(decrypt_2[temp_engine]);
            index_of_list -= shift;
           
            new_list.append(alphabet[index_of_list]);
            main_engine+=1;
            temp_engine+=1;
            
    print(f"The encoded text is " + "".join(new_list));
                            
    
    
def userinput():
    if direction == "encode":
        encrypt(text,shift);
    elif direction == "decode":
        decrypt();
        
        
userinput()