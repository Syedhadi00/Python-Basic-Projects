# Ip Address Validator 
import ipaddress
import time

Text =("====== IP ADDRESS VALIDATOR ======\n") 
for char in Text:
    print(char,end="",flush=True) 
    time.sleep(0.1); #For Animation Like Character By Character Text At starts.

def checkip():
    ip=input("\nEnter Ip Address :")
    try: #This Function Is For Validate The Ip Address With Error Handlers.
        ipaddress.ip_address(ip)
        print("\n===> Your Ip Address :",ip," Is Valid <====\n")
    except ValueError:
        print("\n<=== Your Ip Address :",ip,"Is Not A Valid ===>\n") 
   
    
def again():
     print("====================================================")
     print("1 : Start Validator Again")    
     print("2 : Exit\n")    
     choice = input("Enter your Choice : ")  
     return choice


def manage():
 while True:
   choice=again()
   if choice=='1':
        checkip()
   elif choice=='2':
        print("\nYou Are Exit From This Validator\n")  
        exit(0) 
   else:
        print("\n<>  Try Again <.> You Are Entering Wrong Number <>\n") 
         
       


#lets call the functions
checkip()
manage()