class Students:
    def __init__(self,fn,num,):
        self.firstn=fn
        self.nGrades=num
    def grades(self):
        self.rGrades=[]
        print('For '+self.firstn+',')
        for a in range(0,self.nGrades,1):
            self.rGrades.append(float(input('Please enter grade '+str(a+1)+':')))
        print('')
        return self.rGrades
    def average(self):
        sum=0
        for a in range(0,self.nGrades,1):
            sum=sum+self.rGrades[a]
        self.avg=sum/self.nGrades
        return self.avg
    def minimum(self):
        if self.rGrades[0]>=self.rGrades[1]:
            self.min=self.rGrades[1]
        else:
            self.min=self.rGrades[0]
        for a in range(0,self.nGrades,1):
            if self.rGrades[a]<self.min:
                self.min=self.rGrades[a]
        return self.min
    def maximum(self):
        if self.rGrades[0]<=self.rGrades[1]:
            self.max=self.rGrades[1]
        else:
            self.max=self.rGrades[0]
        for a in range(0,self.nGrades,1):
            if self.rGrades[a]>self.max:
                self.max=self.rGrades[a]
        return self.max
numStudent=int(input('How many students do you have?:'))
print('')
StudentNum=[]
for a in range(0,numStudent,1):
    StudentNum.append('S'+str(a+1))
    StudentNum[a]=Students('Student'+str(a+1),int(input('How many grades '+'Student'+str(a+1)+' has?:')))
    StudentNum[a].grades()
for a in range(0,numStudent,1):
    print(StudentNum[a].firstn)
    print('Average of grades:',StudentNum[a].average())
    print('Maximum grade:',StudentNum[a].maximum())
    print('Minimum grade:',StudentNum[a].minimum())
    print('')