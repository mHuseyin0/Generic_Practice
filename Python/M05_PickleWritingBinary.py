import pickle
Students=[]
Grades=[]
numStudents=int(input('How many students do you have?:'))
for i in range(1,numStudents+1,1):
    print('')
    print('Student',i,':')
    Students.append(str(input("What is student's name?:")))
    print('')
    Grades.append(float(input("What is their grade?:")))
    print('')
with open('Data1.pkl','wb') as f1w:
    pickle.dump(numStudents,f1w)
    pickle.dump(Students,f1w)
    pickle.dump(Grades,f1w)