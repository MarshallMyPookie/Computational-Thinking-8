# Beginning:
stick_points = 0
weak_points = 0

# Middle:
answer = input ("Do you have A) A bald father, or B) a father with hair?\n")
if answer == "A":
    stick_points +=1
elif answer == "B":
    weak_points +=1
answer = input ("Are you A) happy, or B) sad?\n")
if answer == "A":
    stick_points +=1
elif answer == "B":
    weak_points +=1
answer = input ("Are you A) chill, or B) annoying?\n")
if answer == "A":
    stick_points +=1
elif answer == "B":
    weak_points +=1
answer = input ("Are you A) pure, or B) brainrotted?\n")
if answer == "A":
    stick_points +=1
elif answer == "B":
    weak_points +=1
answer = input ("Are you A) Hungry, or B) Not Hungry?\n")
if answer == "A":
    stick_points +=1
elif answer == "B":
    weak_points +=1
if stick_points > weak_points:
    print("You can wield the Serbian stick.")
elif weak_points > stick_points:
    print("You can't wield the stick.")
elif stick_points == weak_points:
    print("You're completely irrelevant.")