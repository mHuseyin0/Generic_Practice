Grades=[]
numGrade=int(input('Hello! How many grades do you have?:'))
numGrades=numGrade
print('Please enter your grades:')
while(numGrade>0):
    Grades.append(float(input()))
    numGrade=numGrade-1
print('Your grades are:')
while(numGrades>0):
    print(Grades[-numGrades])
    numGrades=numGrades-1