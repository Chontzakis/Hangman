s = []

s.append(''' __________
|       |
|       O     
|      /|\ 
|       |
|      / \
|
|_________
          |_
'''









)

s.append(''' __________
|       |
|       O     
|      /|\ 
|       |
|      / 
|
|_________
          |_
'''








)

s.append(''' __________
|       |
|       O  
|      /|\ 
|       |
|      
|
|_________
          |_
'''








)

s.append(''' __________
|       |
|       O  
|      /| 
|       |
|
|_________
          |_
'''








)

s.append(''' __________
|       |
|       O  
|       | 
|       |
|
|_________
          |_'''
          
          
          
          
          
          
          
          
          )

s.append(''' __________
|       |
|       O  
|       | 
|       
|
|_________
          |_'''
          
          
          
          
          
          
          
          
          
          
          )

s.append(''' __________
|       |
|       O  
|        
|       
|
|_________
          |_
'''









)

s.append('''__________
|       |
|        
|        
|       
|
|_________
          |_
'''









)

s.reverse()

import random

def kremala() :
    score = 1
    highscore = 1
    lap = 0
    r = 1
    symbols = '''!@#$%^&*()_-+={}[]\|'";:?/>.<,~`§±'''
    while r == 1 :
        lap += 1
        l = ['conjugate', 'denominator', 'imag', 'numerator', 'real','append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort','count', 'index','count', 'index','capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill','add', 'clear', 'copy', 'difference','discard', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'union', 'update', 'conjugate', 'fromhex', 'hex', 'imag', 'real']
        l = list(set(l)) 
        faults = 0
        guessed = []
        d = random.randint(0,len(l))
        word = l[d]
        print(s[faults],'\n','Word: ' + '_ '*len(word))
        secret = list('_'*len(word))
        while faults < 7 :
            print(' High Score: ',highscore,'\n','Score: ',score,'\n','Word#:',lap)
            char = input(' Guess: ',)
            if (char.isdigit()) or char in symbols : #checking if the character is symbol or number 
                print("That's not a valid guess,give me a letter",'\n\n\n\n',s[faults],'\n','Guessed: ',' '.join(guessed),'\n','Word: ',' '.join(secret))
            else :    
                if len(char) > 1 : #checking if the character has given us 2 or more letters
                    print('Enter a single character','\n\n\n\n',s[faults],'\n','Guessed: ',' '.join(guessed))
                else :    
                    if char in guessed : #checking if the player has already guessed this letter
                        print('You have already guessed that character','\n\n\n\n',s[faults],'\n','Guessed: ',' '.join(guessed),'\n','Word: ',' '.join(secret))
                    else :    
                        print('\n\n\n')
                        guessed += char
                        guessed.sort()
                        if char in word :
                            for spot in range(0,len(word)) :
                                if word[spot] == char : #checking the spot of the correct character
                                    secret[spot] = char #showing the correct character to the player
                            print(s[faults],'\n' , 'Guessed: ',' '.join(guessed))
                            print(' Word: ',' '.join(secret))
                        else :                          
                            faults += 1
                            if faults == 7 : #the whole body is shown
                                for q in [ int , float , list , tuple , dict , str , set] :
                                    if word in dir(q) :
                                        group = str(q)
                                print(s[7],'You lost','\n','The word was',word,'from',group[8:len(group)-2],'\n\n\n','High Score: ',highscore,'\n','Score: ',score,'\n','Word#: ',lap,'\n')
                                score = 1 
                                r = int(input("Press '1' if you want to play again or '0' if you don't: ")) 
                            else :
                                print(s[faults],'\n' , 'Guessed: ',' '.join(guessed))
                                print(' Word: ',' '.join(secret))
                        if not '_' in secret : #all characters have been found 
                            score +=1
                            faults = 7
                            highscore += 1
                            print(' High Score: ',highscore,'\n','Score: ',score,'\n','Word#:',lap,'\n')
                            print ('~~~You won~~~','\n')
                            r = int(input("Press '1' if you want to play again or '0' if you don't: "))
                            if r == 0 :
                                break
        

kremala()
