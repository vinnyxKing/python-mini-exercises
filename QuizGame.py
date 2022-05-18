print("Welcome to my Practice quizz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay let's play :D")

score = 0;

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer1 =  input("What does GPU stand for? ")
if answer1.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 =  input("What does RAM stand for? ")
if answer2.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 =  input("What does PSU stand for? ")
if answer3.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4)*100) + "%")