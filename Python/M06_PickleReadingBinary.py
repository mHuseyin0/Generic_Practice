import pickle
with open('Data1.pkl','rb') as f1r1:
    a1=pickle.load(f1r1)
    b1=pickle.load(f1r1)
    c1=pickle.load(f1r1)
for i in range(1,a1+1,1):
    print('Student',i,':')
    print('')
    print('Name:',b1[i-1])
    print('Grade:',c1[i-1])
    print('')
    print('')