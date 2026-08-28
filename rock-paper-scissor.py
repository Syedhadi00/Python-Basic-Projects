#This Is A Mini Project Of Stone, Paper or Scissor

import random
import time
# Little Animation Of Startin The Game
text="===== Game Is Starting... =====\n1\n2\n3\nLet's Go ...\n\n"
for char in text:
    print(char,end="",flush=True)
    time.sleep(0.1)

def game():
    my_choice=input("Choose = Rock, Paper Or Scissor : ").lower()
    Cpu_choice=random.choice(["rock","paper","scissor"])
# For Print The Cpu Random Choice
    cpu=print("=== Cpu : ",Cpu_choice," ===\n") 
    
    if my_choice == Cpu_choice:
     print("The Game Is Tie")

    elif my_choice == "rock" and Cpu_choice == "scissor":
     print("=== The Winner Is Rock ===\nBecause The Rock Is Break The Scissor Easily\n")

    elif my_choice == "rock" and Cpu_choice == "paper":
     print("=== The Winner Is Paper ===\nBecause The Paper Is Cover The Rock Easily\n")

    elif my_choice == "paper" and Cpu_choice == "scissor":
     print("=== The Winner Is Scissor ===\nBecause The Scissor Is Cut The Paper Easily\n")

    elif my_choice == "paper" and Cpu_choice == "rock":
     print("=== The Winner Is Paper ===\nBecause The Paper Is Cover The Rock Easily\n")

    elif my_choice == "scissor" and Cpu_choice == "rock":
     print("=== The Winner Is Rock ===\nBecause The Rock Is Break The Scissor Easily\n")
 
    elif my_choice == "scissor" and Cpu_choice == "paper":
     print("=== The Winner Is Scissor ===\nBecause The Scissor Is Cut The Paper Easily\n")
    else: 
         print("You Are Entering Wrong Number")
  
def manage():
  while True:
    print("== 1 : Game Again Start ==")
    print("== 2 : Exit game ==")
    choice=input("Enter Your Choice : ")
    if choice=="1":
      game()
    elif choice=="2":
      print("\nThanks For Playing The Game ")
      break
    else:
      print("You Are Entering Wrong Number Try Again !\n")  
      

#Lets Call The Function
game()        
manage()