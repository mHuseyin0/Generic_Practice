import pickle
with open('Data1.pkl','rb') as f1r2:
    a2=pickle.load(f1r2)
    b2=pickle.load(f1r2)
    c2=pickle.load(f1r2)
t=1
while(t==1):
    print('Please input a name to learn their grade.Possible choices:')
    print(b2)
    name=input()
    while(name not in b2):
        print('Please input a valid name.Posibble choices:')
        print(b2)
        name=input()
    for i in range(0,a2,1):
        if(name==b2[i]):
            print(name+"'s grade is:"+str(c2[i]))
    t=int(input('If you want to learn another one, please press 1 .Otherwise, press another number: '))