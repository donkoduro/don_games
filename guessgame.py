import random
randomNumber = random.randrange(1,20)
print("THIS IS A GUESS NUMBER GAME")
lie=["try bit lower","It's near","You've gone too far mate!!","Please try bit higher","Almost near dude"]
guessed = False
while guessed==False:
    userInput = int(input("Your guess please: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>50:
        print("Our guess range is between 0 and 20")
    elif userInput<0:
        print("Our guess range is between 0 and 20")
    elif userInput>randomNumber:
        print random.choice(lie)
    elif userInput < randomNumber:
        print random.choice(lie)

print("End of program")