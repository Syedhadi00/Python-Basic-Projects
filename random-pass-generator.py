#Syed Abdul Hadi
# This is my second program of Random Password Generator in Python
import string
import secrets #import secrets for picking Random numbers with high security level

print("===== Random Password Generator =====")

pool ="123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
password=""
print(" Enter The Length Of Your Password ")

try:
 length=int(input())

 
except ValueError:
   print("You Are Entering Wrong Number!!") 
   exit(0)

if length <= 0 :
  print ("*****! Please Enter Positive Numbers !*****")
  exit(0)

for i in range(length): #loop for lenth of password for the input from the user.
 password +=  secrets.choice(pool)
 
print(password)  
print("=== Thanks For Using The Random Pass Generator ===") 