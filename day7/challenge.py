import random
import words,art
stages = (art.stages)
print(art.logo);

word = (words.word_list)
rand_word = (random.choice(word));
rand_word = list(rand_word);
print(f"This Sollution is {''.join(rand_word)}")
#user_type = input(">> ");
#for item in (rand_word):
#    if (item.lower()==user_type):
    #    print("TRUE");
#    else:
   #     print("N");
blank_space = list("_"*(len(rand_word)));
#print(blank_space);
counted_no = len(rand_word);
#print(blank_space);
while ("_" in blank_space):

    user_type = input("Guess a Letter >> ");
    rand_word_string = ("".join(rand_word));


    for item in(range(len(rand_word))):
        to_change = rand_word[item];
        if (to_change == user_type):
            blank_space[item] = to_change;

            #print(stages[counted_no - 1])#editing right here
            print(blank_space);
        if ("_" not in blank_space):
            print("You've Won The Game");
    if (user_type not in rand_word):
        counted_no -= 1 ;
        print(f"\n\nThe Letter {user_type} which you type is not in the word!");
        print(stages[counted_no - 1]);

        if (counted_no == 1):
            print("Oh Shit You Loose");
#Challange 4
