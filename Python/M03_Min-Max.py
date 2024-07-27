numGrade=int(input('How many grades do you have?:'))
numGrades=numGrade
Grades=[]
print('Please enter your grades:')
for a in range(1,1+numGrade,1):
    print('Grade ',a,'=')
    Grades.append(float(input()))
GradeSort=[]
if Grades[0]>=Grades[1]:
    max=Grades[0]
else:
    max=Grades[1]
for b in range(0,numGrade,1):
    if Grades[b]>=max:
        max=Grades[b]
for c in range(0,numGrade-1,1):
    GradeSort.append(max)
    Grades.remove(max)
    numGrade=numGrade-1
    if numGrade==1:
        max=Grades[0]
        GradeSort.append(max)
    else:
        if Grades[0]>=Grades[1]:
            max=Grades[0]
        else:
            max=Grades[1]
        for b in range(0,numGrade,1):
            if Grades[b]>=max:
                max=Grades[b]
print('Your grades sorted from max to min:')
for a in GradeSort:
    print(a)
print('Your grades sorted from min to max:')
for a in range(numGrades-1,-1,-1):
    print(GradeSort[a])