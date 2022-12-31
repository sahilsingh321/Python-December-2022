scissors = '''
  ####
 #
  ####
      #
 #    #
  ####
'''
rock = '''
######
#     #
#     #
######
#   #
#    #
#     #
'''
paper = '''
 #####
 #    #
 #    #
 #####
 #
 #
'''
draw = '''
######
#     #
#     #
#     #
#     #
#     #
######
'''
#Algorithm:
import random
number_got = random.randint(0,2);

rock_list = [rock , str(number_got)];

paper_list = [paper , str(number_got)];

scissors_list = [scissors , str(number_got)];

player_guess = int(input("What You Choose ? 0 for Rock , 1 for Paper 2 for Scissors >>    "));
rock_list_player = [rock , str(player_guess)];

paper_list_player = [paper , str(player_guess)];

scissors_list_player = [scissors , str(player_guess)];
if(player_guess == number_got):
    if(number_got == 0):
        print(f"You Choosed {player_guess} \n\nwhich is \n{rock} \nComputer Choosed {number_got} which is {rock}\nSo its a draw \n{draw}");
    if (number_got ==  1):
        print(f"You Choosed {player_guess} \n\nwhich is \n{paper} \nComputer Choosed {number_got} which is {paper}\nSo its a draw \n{draw}");
    if (number_got == 2 ):
        print(f"You Choosed {player_guess} \n\nwhich is \n{scissors}\nComputer Choosed {number_got} which is {scissors}\nSo its a draw \n{draw}");

if (number_got == 0):
    if(player_guess == 1):
        print(f"Computer Got {rock_list[1]}\n{rock_list[0]}\nYou Got {paper_list_player[1]} \n{paper_list_player[0]}\n");
        print("Paper Beats Rock \nYou Won ");
    if(player_guess == 2):
        print(f"Computer Got {rock_list[1]}\n{rock_list[0]}\nYou Got {scissors_list_player[1]} \n{scissors_list_player[0]}\n");
        print("Rock Beats Scissor \nYou Loose ");
if (number_got == 1 ):
    if(player_guess == 0):
        print(f"Computer Got {paper_list[1]}\n{paper_list[0]}\n You Got {rock_list_player[1]} \n{rock_list_player[1]}\n");
        print("Paper Beats Rock \nYou Loose");
    if (player_guess == 2):
        print(f"Computer Got {paper_list[1]}\n{paper_list[0]}\n You Got {scissors_list_player[1]} \n{scissors_list_player[0]}\n");

        print("Scissor Cuts Paper \nYou Won ");
if (number_got == 2 ):
    if(player_guess == 0):
        print(f"Computer Got {scissors_list[1]}\n{scissors_list[0]}\n You Got {rock_list_player[1]} \n{rock_list_player[0]}\n");
        print("Rock Beats Scissors \nYou Won");
    if (player_guess == 1):
        print(f"Computer Got {scissors_list[1]}\n{scissors_list[0]}\n You Got {paper_list_player[1]} \n{paper_list_player[0]}\n");
        print("Scissors Cus Paper \nYou Loose Bro");
