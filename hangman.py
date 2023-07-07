import random
# import string
def randomWord():
#3 letter word can be generated using below 2 lines
    # letter=string.ascii_lowercase
    # randomWd=''.join(random.choice(letter) for _ in range(3))
    words = ['cat', 'dog', 'sun', 'red', 'sky', 'cup', 'hat', 'pen', 'key', 'jam']
    randomWd=random.choice(words)
    return randomWd

word=randomWord()
wrong=0
win=False
stages=[" ",
        "_________       ",
        "        |       ",
        "        |       ",
        "        O       ",
        "       /|\      ",
        "       / \      "]
remChar=list(word.lower())
# print(remChar)
board=["_"]*len(word)
print("Welcome to Hangman")

def hangMan(num):
    for i in range(0,num+1):
        print(stages[i])

        
while wrong<len(stages)-1:
    choice=input("Guess a Character:").lower()
    choice=choice[0]#To get the only first Character of input 
    if choice  in remChar:
        ind=remChar.index(choice)
        board[ind]=choice
        remChar[ind]='_'
        # print(remChar)
        unCompleteword=''.join(board)
        print(f"{unCompleteword}")
        if remChar==['_']*len(word):
            win=True
            print("You won the game! Thanks For Playing\n")
            break
    # elif len(choice)>1 and choice=='':
    #     continue
    else:
        wrong+=1
        hangMan(wrong)
if not win:
    print(f"You Lose!The Correct Word Was {word}")
