print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Good job!")
    score += 1
else:
    print("Nope! Sorry.")
 
answer = input("How would you like to eat your pasta? ")
if answer.lower() == "just like i want to":
    print("Wow, that's interesting.")
    score += 1
else:
    print("That isn't that interesting.")

answer = input("What's a good place to visit? (extra credit) ")
if answer.lower() == 'yo mama':
    print("A little rude, but you got the answer.")
    score += 2
else:
    print("Very cool! But no points.")

if not score > 2:
    print("You got a score of " + str((score / 2 * 100)) + "%!")
else:
    print("You got a score of " + str((score / 2 * 100)) + "%! You went overboard.")
