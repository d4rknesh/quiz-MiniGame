import os
import time

def welcome() :
    print("Hello !\nWelcome to my computer Quiz !")
    time.sleep(1)    
    user_awnser = input("Do you want to play?(y/n) ").lower()
    if user_awnser == 'n':
        quit()
    while user_awnser != 'y' :
        os.system("cls")
        user_awnser = input("Do you want to play?(y/n) ").lower()
        if user_awnser == 'n':
            quit()
        
def ask_question(question_dict):
    points = 0
    os.system("cls")
    print("here we go!")
    for i,question in enumerate(question_dict) :
        os.system("cls")
        print(f'Question {i+1}/{len(question_dict)}: ')
        user_awnser = input(list(question_dict.keys())[i])
        if user_awnser == question_dict[question] :
            print("Right !\nYou got 1 point :)")
            points += 1
        else : 
            print (f"Wrong !\n correct awnser is '{question_dict[question]}'")

        time.sleep(2)
        
    return points

def ending(points):
    os.system("cls")
    print(f'You got {points} question(s) correct!\nnice try')
