import random
print("******** Passwrod Generator ********")
print("           **** Signup ****         ")
UserName=input("Enter user Name")
Capital_Char=[]
Number=[1,2,3,4,5,6,7,8,9]
Symbol=['@','#','*','$']
Small_Char=[]
for i in range(ord("A"),ord("Z")+1):
    Capital_Char.append(chr(i))
for i in range(ord("a"),ord("z")+1):
   Small_Char.append(chr(i))
Random_password=[]
for i in range(2):
    C=random.choice(Capital_Char)
    Random_password.append(C)
for i in range(1,4):
    S=random.choice(Small_Char)
    Random_password.append(S)
for i in range(1,4):
    Ss=random.choice(Symbol)
    Random_password.append(Ss)
for i in range(2):
    N=random.choice(Number)
    Random_password.append(N)
random.shuffle(Random_password)
print("".join([str(Random_password)for Random_password in Random_password]))

---------------------------------------------
#second code
import string
import random
print('********Password Generator********')
print('       ****Signup Form****        ')
Number=string.digits
Charcter=string.ascii_letters
Symbol=string.punctuation
R_Password=[]
#print(Number,Charcter,Symbol)
Word=Number+Charcter+Symbol
#print(Word)

Password_length=int(input("How many character you want for password:  "))
for i in range(Password_length):
    Random_password=random.choice(Word)
    R_Password.append(Random_password)
# SignUp Form:-
User_Name= input("Enter User Name")
print("User Name: ",User_Name)
print("Password:" + "".join([str(R_Pwd) for R_Pwd in R_Password]))


