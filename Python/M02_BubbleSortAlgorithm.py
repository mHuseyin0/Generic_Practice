def grdInput(num,ary):
    print('Please enter your grades:')
    for a in range(0,num,1):
        print('Grade ',a+1,'=')
        ary.append(float(input()))
    
    return ary

def grdAvg(num,ary):
    sum=0
    for a in range(0,num,1):
        sum=sum+ary[a]
    avg=sum/num

    return avg

def grdMax(num,ary):
    if(ary[0]>=ary[1]):
        max=ary[0]
    if (ary[0]<=ary[1]):
        max=ary[1]
    for a in range(0,num-1,1):
        if(ary[a]>=ary[a+1] and ary[a]>=max):
            max=ary[a]
        if (ary[a]<=ary[a+1] and max<=ary[a+1]):
            max=ary[a+1]

    return max

def grdMin(num,ary):
    if (ary[0]<=ary[1]):
        min=ary[0]
    if (ary[0]>=ary[1]):
        min=ary[1]
    for a in range(0,num-1,1):
        if (ary[a]<=ary[a+1] and ary[a]<=min):
            min=ary[a]
        if (ary[a]>=ary[a+1] and min>=ary[a+1]):
            min=ary[a+1]
    
    return min

def grdSort(num,ary):
    for a in range(0,num-1,1):
        for a in range(0,num-1,1):
            if ary[a]>ary[a+1]:
                swp=ary[a]
                ary[a]=ary[a+1]
                ary[a+1]=swp
    
    return Grades

def prints(num1,num2,num3,ary):
    print('The average of your grades is ',num1)
    print('Your maximum grade is:',num2)
    print('Your minimum grade is:',num3)
    print('Your grades sorted from min to max:')
    for a in ary:
        print(a)

numGrade=int(input('How many grades do you have?:'))
Grades=[]

Grades=grdInput(numGrade,Grades)
avg=grdAvg(numGrade,Grades)
max=grdMax(numGrade,Grades)
min=grdMin(numGrade,Grades)
Grades=grdSort(numGrade,Grades)
prints(avg,max,min,Grades)