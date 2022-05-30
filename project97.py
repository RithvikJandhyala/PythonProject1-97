import random;

ans = random.randint(1,9)
chance = 0
while chance < 5:
    guess = int(input("ENTER YOUR GUESS: "))
    if guess == ans:
        print("Congratutaltions you win")
        break
    elif guess < ans:
        print("Your Guess was to low")
        
    else:
        print( "Your Guess was to high")
    chance+=1    
    

if chance > 4 :
        print("Your Chances are completed")        