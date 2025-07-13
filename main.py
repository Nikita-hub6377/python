import random
"""
  1 for stone
  2 for paper
  3 for scissor

"""
computer = random.choice([1,2,3])
youstr = input("Enter Your Choice:")
youDict = {"S":1,"P":2,"Sc":3} 
reverseDict = {1: "Stone",2:"Paper",3:"Scissor"}
you = youDict[youstr]
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
if(computer==you):
    print("It's draw match")
else:
   if(computer==1 and you==2)  :
       print("you win!")
   elif(computer==1 and you==3): 
       print("you lose!")
   elif(computer==2 and you==1):  
       print("you lose!")    
   elif(computer==2 and you==3):  
       print("you win!")
   elif(computer==3 and you==1):  
       print("you win!") 
   elif(computer==3 and you==2): 
       print("you lose!")     