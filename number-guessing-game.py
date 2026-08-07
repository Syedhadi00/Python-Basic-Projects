import random #import random for picking the random number from our custom range
import time

def display(): #This is menu
 print("*=*=*=*=* NUMBER GUESSING GAME *=*=*=*=*\n")
 print("1: Start Game")
 print("2: Exit Game\n")
 choice=int(input("Enter Your Choice : \n"))
 if choice==1:
   printnumber()   
 elif choice==2:
  print("=*=*= You Are Exit From From This Game =*=*= ")
 else :
  print("You Are Entering Wrong Number Please Try Again") 


def printnumber():#Full game managing function
 number=random.randint(1,20)
 attempt=0
 max_attempt=7
 game="Game Is Starting"
 game.split() #This is used for print word by word in time duration
 for word in game:
   print(word,end='',flush=True) 
   time.sleep(0.1)
 print()  


 time.sleep(3) #After 3 seconds the game will be start
 print("===== I Thought A Number From 1 to 20 =====\n") 


 while  attempt < max_attempt :
   guess=int (input("Guess The Number:== \n"))
   attempt += 1

   if guess > number:
       print("You Are Going High Please Decrease It\n")
   elif guess < number :
      print("You Are Going Low Please Increase It\n")
   else :
      print("=== Congratulations You Guessing The Right Number In =",attempt," Attempts ===")  
      return 
 print("<< You Are Lose >>\nThe Right Number Is : ",number,"\nHaHaHaHa ! Oops Sorry")

 
#finnaly call the function
display()