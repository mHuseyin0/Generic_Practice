import time

def timeInput():
    year=input('Please input year(Can be negative): ')
    try:
        year=int(year)
    except:
        ValueError
    while type(year)!=int:
        year=input('Please input an integer: ')
        try:
            year=int(year)
        except:
            ValueError
    if year%4==0:
        feb=29
    else:
        feb=28
    print('If you do not want to give more details about the time and date, you can input - at any time from now on.')
    
    day=10
    hour=10
    minute=10
    second=10

    month=input('Please input month number(1-12): ')
    if month=='-':
        second=0
        minute=0
        hour=0
        day=1
        month=1
    try:
        month=int(month)
    except:
        ValueError
    while type(month)!=int or month<1 or month>12:
        month=input('Please input an integer between 1 and 12.: ')
        if month=='-':
            second=0
            minute=0
            hour=0
            day=1
            month=1
        try:
            month=int(month)
        except:
            ValueError
    if month==4 or month==6 or month==9 or month==11:
        maxDay=30
    elif month==2:
        maxDay=feb
    else:
        maxDay=31 

    if not day==1:
        day=input('Please input day number(1-'+str(maxDay)+'): ')
    if day=='-':
        second=0
        minute=0
        hour=0
        day=1
    try:
        day=int(day)
    except:
        ValueError
    while type(day)!=int or day<1 or day>maxDay:
        day=input('Please input an integer between 1 and '+maxDay+'.: ')
        if day=='-':
            second=0
            minute=0
            hour=0
            day=1
        try:
            day=int(day)
        except:
            ValueError
    
    if not hour==0:
        hour=input('Please input hour(0-23): ')
    if hour=='-':
        second=0
        minute=0
        hour=0
    try:
        hour=int(hour)
    except:
        ValueError
    while type(hour)!=int or hour<0 or hour>23:
        hour=input('Please input an integer between 0 and 23.:')
        if hour=='-':
            second=0
            minute=0
            hour=0
        try:
            hour=int(hour)
        except:
            ValueError
    
    if not minute==0:
        minute=input('Please input minute(0-59):')
    if minute=='-':
        second=0
        minute=0
    try:
        minute=int(minute)
    except:
        ValueError
    while type(minute)!=int or minute<0 or minute>59:
        minute=input('Please input an integer between 0 and 59.:')
        if minute=='-':
            second=0
            minute=0
        try:
            minute=int(minute)
        except:
            ValueError
    
    if not second==0:
        second=input('Please input second(0-59):')
    if second=='-':
        second=0
    try:
        second=int(second)
    except:
        ValueError
    while type(second)!=int or second<0 or second>59:
        second=input('Please input an integer between 0 and 59.:')
        if second=='-':
            second=0
        try:
            second=int(second)
        except:
            ValueError
    
    timeOutput=[year,month,day,hour,minute,second,maxDay]
    
    return timeOutput

def currentTimeInput():
    currentTimeTup=time.localtime()
    if currentTimeTup.tm_year%4==0:
        feb=29
    else:
        feb=28
    if currentTimeTup.tm_mon==4 or currentTimeTup.tm_mon==6 or currentTimeTup.tm_mon==9 or currentTimeTup.tm_mon==11:
        maxDay=30
    elif currentTimeTup.tm_mon==2:
        maxDay=feb
    else:
        maxDay=31
    currentTimeOutput=[currentTimeTup.tm_year ,currentTimeTup.tm_mon ,currentTimeTup.tm_mday ,currentTimeTup.tm_hour ,currentTimeTup.tm_min ,currentTimeTup.tm_sec ,maxDay] 
    return currentTimeOutput

def timeComp(time1,time2):
    latter=1
    former=0
    i=0
    while latter==1 and i<6:
        if time1[i]>time2[i]:
            latter=time1
        elif time1[i]<time2[i]:
            latter=time2
        i+=1

    if latter==time1:
        former=time2
    elif latter==time2:
        former=time1

    return former,latter

def timeCalc(time1,time2):
    yearDif=time2[0]-time1[0]
    monthDif=time2[1]-time1[1]
    dayDif=time2[2]-time1[2]
    hourDif=time2[3]-time1[3]
    minuteDif=time2[4]-time1[4]
    secondDif=time2[5]-time1[5]

    dayDiff=0

    if secondDif<0:
        minuteDif-=1
        secondDif=60+secondDif
    if minuteDif<0:
        hourDif-=1
        minuteDif=60+minuteDif
    if hourDif<0:
        dayDiff=-1
        hourDif=24+hourDif
    if dayDif<0:
        monthDif-=1
        dayDif=time2[2]+time1[6]-time1[2]+dayDiff
    if monthDif<0:
        yearDif-=1
        monthDif=12+monthDif

    yearPrint=''
    monthPrint=''
    dayPrint=''
    hourPrint=''
    minutePrint=''
    secondPrint=''

    if yearDif!=0:
        yearPrint=str(yearDif)+' years '
    if monthDif!=0:
        monthPrint=str(monthDif)+' months '
    if dayDif!=0:
        dayPrint=str(dayDif)+' days '
    if hourDif!=0:
        hourPrint=str(hourDif)+' hours '  
    if minuteDif!=0:
        minutePrint=str(minuteDif)+' minutes '
    if secondDif!=0:
        secondPrint=str(secondDif)+' seconds '

    print('There are '+yearPrint+monthPrint+dayPrint+hourPrint+minutePrint+secondPrint+'between these dates.')

choice=input('Please enter what do you want to do?:\n1: Calculate time between two inputted time.\n2: Calculate time between now and an inputted time.\n')
while choice!='1' and choice!='2':
    print('Please input a valid value.(1 or 2)')   
    choice=input('Please enter what do you want to do?:\n1: Calculate time between two inputted time.\n2: Calculate time between now and an inputted time.\n')

if choice=='1':
    timeVsTime1=timeInput()
    timeVsTime2=timeInput()
    if timeVsTime1!=timeVsTime2:
        formerTime,latterTime=timeComp(timeVsTime1,timeVsTime2)
        timeCalc(formerTime,latterTime)
    else:
        print('Your inputs are the same date.')

if choice=='2':
    timeVsCurrent=timeInput()
    currentTime=currentTimeInput()
    formerTime,latterTime=timeComp(timeVsCurrent,currentTime)
    if timeVsCurrent==formerTime:
        print('You are comparing past and now.')
    else:
        print('You are comparing future and now.')
    timeCalc(formerTime,latterTime)