def hangman(ch):
    for i in range(0,len(ch)):
        print('_',end=" ")
    print('/ 0 penalty')
    penalty = 0
    guesses=""
    while penalty<=12:
        count=0
        ch1=input("$> ")
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
hangman('apple')     
