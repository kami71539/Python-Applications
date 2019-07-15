import time
#name=input("What is your name ? ")
#print(f"Hello, {name}, time to play Hangman.")
print("")
time.sleep(1)
print("start Guessing.")
time.sleep(0.5)
word='oompa loompa'
guesses=""
turns=10
answer=''
while turns>0:
    failed=0
    guess=input("Guess a character:-\n")
    guesses+=guess.lower()
    answer=''
    for char in word:
        if char in guesses:
            answer=answer+char
            print(char,end="")
        else:
            print("_",end="")
            failed+=1
    if guess==word or answer==word:
        print("\nYou won")
        break
    print()
    if guesses not in word:
        turns-=1
        print("WRONG")
    print(f"You have {turns} more guesses left.")
    if turns==0:
        print("You lose")
    if guess=='stop':
        print('ok')
        break
