NumStud = int(input("How many students are there?"))

SumScore = 0

for i in range(NumStud):
    score = int(input("What did this student get?"))
    SumScore = SumScore + score

print("The average score of all the students is " + str(SumScore/NumStud))
