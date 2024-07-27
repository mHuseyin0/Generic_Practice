import random

playerChoice=1
draw=0
PCWon=0
playerWon=0

def mainGame(playerChoice):
    global playerWon, PCWon, draw
    print('')
    if playerChoice=='1':
        print('You have chosen ROCK.')
    if playerChoice=='2':
        print('You have chosen PAPER.')
    if playerChoice=='3':
        print('You have chosen SCISSORS.')
    print('')
    if playerChoice=='1' or playerChoice=='2' or playerChoice=='3':
        PCChoice=str(random.randint(1,3))
        if PCChoice=='1':
            print('PC has chosen ROCK.')
        if PCChoice=='2':
            print('PC has chosen PAPER.')
        if PCChoice=='3':
            print('PC has chosen SCISSORS.')
        print('')
        if PCChoice==playerChoice:
            print("It's draw.")
            draw+=1
        if (PCChoice=='1' and playerChoice=='3') or (PCChoice=='2' and playerChoice=='1') or (PCChoice=='3' and playerChoice=='2'):
            print('PC has won.')
            PCWon+=1 
        if (PCChoice=='1' and playerChoice=='2') or (PCChoice=='2' and playerChoice=='3') or (PCChoice=='3' and playerChoice=='1'):
            print('You have won.')
            playerWon+=1
        print('')
    return playerWon, PCWon, draw

print('Welcome to "Rock-Paper-Scissors".')
print('You can make your choices by inputting 1,2,3. \n1:ROCK\n2:PAPER\n3:SCISSORS\nIf you want to quit,you can enter 0.')
while playerChoice!='0':
    playerChoice=input('Please input your choice.: ')
    if playerChoice=='1' or playerChoice=='2' or playerChoice=='3':
        mainGame(playerChoice)
    elif playerChoice=='0':
        pass
    else:
        print('Please input a valid value.(Possible values:1,2,3 OR 0 to quit.)')
if playerChoice=='0':
    if draw==0 and playerWon==0 and PCWon==0:
        print('')
        print('Understandable.Have a nice day.')
        print('')
    else:
        gamePlayed=draw+playerWon+PCWon
        print('')
        print('You have played', str(gamePlayed) ,'games.')
        print('')
        print('You have won', str(playerWon) ,'rounds.')
        print('')
        print('You have lost', str(PCWon) ,'rounds.')
        print('')
        print(str(draw),'rounds were draw.')
        print('')
        if playerWon>PCWon:
            print('Congratulations!')
            print('')
        if playerWon<PCWon:
            print('I wish you could have a better chance next time.')
            print('')
        lastChance='1'
        while playerWon==PCWon and lastChance=='1':
            print('It is a absolute draw.You may consider playing one more round.')
            print('')
            lastChance=input('Please press 1 to play one more or press any button to quit: ')
            if lastChance!='1':
                print('Come on! What have you done?!')
            if lastChance=='1':
                print('')
                playerChoice=input('Please input your choice.You have only one chance,think hard.\n1:ROCK\n2:PAPER\n3:SCISSORS\n')
                mainGame(playerChoice)
                print('')
                if playerWon==PCWon:
                    print("You have one more chance again,if you want...")
                    print('')
                if playerWon>PCWon:
                    print('GREAT!!! YOU WON!!! :)')
                    print('')
                if playerWon<PCWon:
                    print('HAHAHAHAHAHAHAH I WON!')
                    print('')
