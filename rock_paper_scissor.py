from random import randint as rint

'''
    Rock = 1
    Paper = 2
    Scissor = 3
        Rock beats Scissor
        Paper beats Rock
        Scissor beats Paper
'''


computer_choice = rint(1,3)
player_choice = int(input("Please enter one of the following: 1 (For Rock), 2 (For Paper), 3 (For Scissors)"))
temp_comp_var = None
temp_player_var = None

if computer_choice == 1:
    temp_comp_var = "Rock"
elif computer_choice == 2:
    temp_comp_var = "Paper"
elif computer_choice == 3:
    temp_comp_var = "Scissors"

if player_choice == 1:
    temp_player_var = "Rock"
elif player_choice == 2:
    temp_player_var = "Paper"
elif player_choice == 3:
    temp_player_var = "Scissors"

print(f"You Picked {temp_player_var}\nThe Computer picked {temp_comp_var}")
if computer_choice == 1 and player_choice == 3:
    print("The Computer is the Winner")
elif computer_choice == 2 and player_choice == 1:
    print("The Computer is the Winner")
elif computer_choice == 3 and player_choice == 2:
    print("The Computer is the Winner")
else:
    print("You TIED")


'''
    24-Hour Clock Program
'''
time = input("Please enter the 24-hour clock time: ")
minutes = int(time) % 100
hours = int(time) // 100
if minutes >= 0 and minutes <= 9:
    minutes = str(minutes)
    minutes = "0"+minutes
Meridiem = "AM"
if hours == 0:
    hours = "12"
elif hours >= 1 and hours <= 9:
    hours = str(hours)
    hours = "0"+hours
elif hours > 12:
    Meridiem = "PM"
    if hours == 13:
        hours = "01"
    elif hours == 14:
        hours == "02"
    elif hours == 15:
        hours = "03"
    elif hours == 16:
        hours = "04"
    elif hours == 17:
        hours = "05"
    elif hours == 18:
        hours = "06"
    elif hours == 19:
        hours = "07"
    elif hours == 20:
        hours = "08"
    elif hours == 21:
        hours = "09"
    elif hours == 22:
        hours = "10"
    elif hours == 23:
        hours = "11"
print(f"The time is {hours}:{minutes} {Meridiem}")