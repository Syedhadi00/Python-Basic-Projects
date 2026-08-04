#This Is My First Python Programme Of Calculator 
#Syed Abdul Hadi
def calc():
    print("===== CALCULATOR =====\n")
    print("Enter Your First Number")
    try:
     num1=float(input())
    except ValueError:
     print("This is Not A Valid Number ! Try Again ")
     return
    
    print("Enter Your Operator : + , - , / , * ")
    special=input()

    print("Enter Your second Number")
    try: #try and except is used because if someone used characters not number then it will execute.
     num2=float(input())
    except ValueError:
      print("This is Not A Valid Number ! Try Again ")
      return

    if special=="+": 
     print("Your Answers is >>> ",num1 + num2)

    elif special=="-":
     print("Your Answers is >>> ",num1 - num2)  

    elif special=="*":
     print("Your Answers is >>> ",num1*num2) 

    elif special=="/":
       if num2== 0:
         print("Divison By Zero Is Not Valid !!!")
       else:  
        print("Your Answers is >>> ",num1/num2)

    else :
      print(" ***** You Are Entering Wrong Operator !!! ***** ") 

    print ("===== You Want To Calculate More : y / n =====")  
    more=str(input()) 
    print()


    if more=="y":
     calc()
    elif more=="n":
     print("Thanks For Using The Calculator")   
    
#lets call the function
calc()