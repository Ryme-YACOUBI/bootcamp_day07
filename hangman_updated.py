import time
import random
def hangman():
    print('Choose number of max penalties : ')
    max_penalty=int(input())
    while True:
        print('Choose the length of the word (between 3 and 12) : ')
        l=int(input())
        if l>=3 and l<=12:
            break
        else:
            print('Choose a length between 3 and 12')
    mots_theme=[]
    liste_mots_themes = []
    liste_mots=[]
    file=open("words.txt",'r')
    for line in file:
        line=line.strip()
        mots_theme+=line.split(';')
    for i in range(len(mots_theme)):
        if i % 2 == 0:
            if len(mots_theme[i])==l:
                liste_mots_themes.append(mots_theme[i])
                liste_mots.append(mots_theme[i])
                liste_mots_themes.append(mots_theme[i+1])
    ch = random.choice(liste_mots)
    for i in range(len(liste_mots_themes)):
        if liste_mots_themes[i] == ch:
            print(f'Theme: {liste_mots_themes[i+1]}')

    for i in range(0,l):
        print('_',end=" ")
    print('/ 0 penalty')
    penalty = 0
    guesses=""
    start = time.time()
    while penalty<max_penalty:
        count=0
        ch1=input("$> ")
        if time.time() - start >= 10:
            print("Time finished!")
            return
        guesses+=ch1
        if ch1.lower()==ch.lower():
            if penalty>=2:
                print(f"{ch}: correct guess - {penalty} penalties")
                return
            else:
                print(f"{ch}: correct guess - {penalty} penalty")
                return
        elif len(ch1)==1 and ch1.lower() in ch.lower():
            print(f"found {ch.lower().count(ch1.lower())} '{ch1}'")  
        elif len(ch1)==1 and ch1 not in ch:
            print(f"No '{ch1}' found")
            penalty+=1
        elif (len(ch1)==len(ch) and ch1!=ch) or (len(ch1)>1 and len(ch1)!=len(ch)):
            print(f'{ch1}: incorrect guess')
            penalty=penalty+5
            guesses=''
        for i in range(0,len(ch)):
            if ch[i].lower() in guesses.lower():
                print(ch[i],end=' ')
                count+=1
            else : 
                print('_',end=' ')
        if count==len(ch):
            if penalty>=2:
                print(f"{ch}: correct guess - {penalty} penalties")
                return
            else:
                print(f"{ch}: correct guess - {penalty} penalty")
                return
        if penalty>=2:
            print(f'/ {penalty} penalties')
        else:
            print(f'/ {penalty} penalty')    

hangman()     
