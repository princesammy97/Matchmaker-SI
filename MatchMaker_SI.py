print("*"*70)
print( "Matchmaker 2.0".center(68))
print("Helping you find luv since 2020".center(68))
print("Cupidsoft, Inc.".center(68))
print("*"*70)
print("This program figures out if you and I are meant to be.")
print("You will answer 5 questions.To each question, answer 5")
print("if you strongly agree, 4 if you agree, 3 if you neither") 
print("agree nor disagree, 2 if you disagree, and 1 if you")
print("strongly disagree")

print("Our happiness depends on you. Don't let us down...")
def validate(n):
    while True:
         try: 
            value= int(input(n))
         except ValueError:
            print("Error")
            continue
            if n < 0:
             print("Sorry, the number can't be negative")
            continue
         else:
            break
    return value

print("Question 1")
q1= int(input("Tom Brady is the greatest quarterback of all time:")) 
ans=5 
weight1=3
qcs=abs(q1-ans)#question comptability score
score1=weight1*qcs


print("Question 2")

q2= int(input("Rare steak is better than well done:"))
ans2=5
weight2=2
qcs2=abs(q2-ans)
score2=weight2*qcs2

print("Question 3")

q3= int(input("Beaches are nicer than mountains:"))
ans3=4
weight3=1
qcs3=abs(q3-ans)
score3=weight3*qcs3

print("Question 4")

q4= int(input("The pandemic will end this fall:"))
ans4=4
weight4=5
qcs4=abs(q4-ans)
score4=weight4*qcs4

print("Question 5")

q5= int(input("Biden will do better than Trump:"))
ans5=3
weight5=4
qcs5=abs(q5-ans)
score5=weight5*qcs5

totalscore=score1+score2+score3+score4+score5
finalscore=100-totalscore
if finalscore >=70:
    print("Your final score is {}%".format(finalscore))
    print("Looking like the marriage type")
elif finalscore >=50:
    print("Your final score is {}%".format(finalscore))
    print("A pass")
elif finalscore  < 50: 
    print("Your final score is {}%".format(finalscore))
    print("Definitely a pass")
elif finalscore <=30:
    print("Your final score is {}%".format(finalscore))
    print("Definitely a pass")
elif finalscore <=20:
    print("Your final score is {}%".format(finalscore))
    print("Definitely a pass")

            



