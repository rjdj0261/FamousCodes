import random
print("Number guessing game")
print("What is your name:")
myName= input()
number = random.randint(1, 20)
chances = 0
print("Guess a number (between 1 and 20):")
while chances < 5:
 guess = int(input())
 if guess == number:
     print("Congratulation YOU WON!!!")
     break
 elif guess < number:
     print("Your guess was too low: Guess a number higher than", guess)
 else:
     print("Your guess was too high: Guess a number lower than", guess)
 chances += 1
if not chances < 5:
    print("YOU LOSE!!! The number is ", number)