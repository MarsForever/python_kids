import random

secret = random.randint(1,1000)
guess = 0
tries = 0

print("I have a secret , do you want to know that ?")
print("It is  a number from 1 to 1000. I will give you 10 tries")

while (guess) != secret and tries < 10:
    guess = int ( input("What's yer guess? \n"))
    if int(guess) < (secret):
        print("More high." )
        print (9-tries)
    elif (guess) > (secret):
        print("More low ")
        print (9-tries)
    tries = tries + 1
if (guess )== secret:
    print ("You find my secret!!!")
else:
    print ("No more guesses")
    print ("The secret number was",secret)
