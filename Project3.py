Summer_points = 0
Spring_points = 0
Winter_points = 0


answer1 = input ("Do you prefer A short sleeves, B long sleeves, or C tank top?")
if answer1 == "A":
    Summer_points += 1 
elif answer1 == "B":
    Winter_points += 1
elif answer1 == "C": 
    Spring_points += 1

answer2 = input ("Is your favorite weather A rainy, B snowy, or C sunny?")
if answer2 == "A":
    Spring_points += 1
    Winter_points += 1
elif answer2 == "B":
     Winter_points += 2
elif answer2 == "C":
    Summer_points += 2

answer3 = input ("Would you rather A Snowboard, B ski, or C swim?")
if answer3 == "A" or answer3 == "B":
    Winter_points += 2
elif answer3 == "C":
    Summer_points += 1
    Spring_points += 1

answer4 = input ("Do you like A golf, B Baseball, C Basektball")
if answer4 == "A":
    Summer_points += 1
elif answer4 =="B":
    Spring_points += 1
elif answer4 == "C":
    Winter_points += 1 


answer5 = input ("Overall do you think you like A summer, B winter, or C spring?")
if answer5 == "A":
    Summer_points += 1
elif answer5 == "B": 
    Winter_points += 1
elif answer5 == "C":
    Spring_points += 1


if Winter_points > Summer_points and Winter_points > Spring_points:
    print ("You are a Winter Person")
elif Summer_points > Winter_points and Summer_points > Spring_points:
    print ("You are a Summer person")
elif Spring_points > Summer_points and Spring_points > Winter_points:
    print ("You are a Spring person")
