import time
import random
List_Word=['python','java','ruby','cpp','django','react']
random_word=random.choice(List_Word)
List=list('_'*len(random_word))
print(List)
number=len(random_word)
Life_Time=2
print('*******************')
while True:
    if  '_' not in List:
        break
    user_input=input("Enter a char")
    if len(user_input)==1:
        index=0
        if user_input in random_word:
            for char in random_word:
                if char == user_input:
                    List[index]=char
                    
                    print(" ".join(List))
                index+=1
    
        else:
            print("up's your guess wrong")
            
            if Life_Time<1:
                break
            Life_Time -= 1
            print("Your remaining Life_time:",Life_Time)
    else:
        print("you entered more than 1 character .")
if '_' not in List:
    print("Congratulation ! you are winnier...........by LifeTime",Life_Time)
else:
    print("ups! You are loss")
                
        
       
