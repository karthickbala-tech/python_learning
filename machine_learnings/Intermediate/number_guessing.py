#Implement a number guessing game (computer chooses random number)
import random
Random= random.randint(1,100)
attempt=0
print("Enter a number between  1 to 100")

find=False
while find==False:
    guess=int(input("guess number:"))
    attempt+=1
    if guess==Random:
        print(f"Your find that number with in {attempt} attempt")
        find=True
    elif Random>guess:
        print("Too low try again")
        
    elif Random<guess:
        print("Too high,try again")
