# Krish Dhansinghani

word = input("Enter a word or phrase:")
newword=""
for i in range(0,len(word)):
    newword= newword+word[i]+"_"
print("The word to guess:",newword[1::2])
wrong_guess_counter=0;
while "_" in newword and wrong_guess_counter<6:
    letter = input("Guess a letter: ")
    if letter in newword:
        newword=newword.replace(letter+"_",letter+letter)
    else:
        wrong_guess_counter+=1
    print("The word to guess:",newword[1::2])

if "_" in newword:
    print("You Lose!")
    print("You guessd: ",newword[1::2])
    print("The answer was", word)

else:
    print("You win! The answer was: ",word)


