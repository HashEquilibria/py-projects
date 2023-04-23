"""lives = 6
chosen_word = "banana"
guesses = {"G","Y","A"}
word = ["_","A","_","_","_","_"]

- word is chosen
- write dashes "_" in place of the letters in the chosen word
- start guessing letters
- if letter isn not in chosen wod lose a life
- if letter is in the chosen word replace the dashes where the letters apear
- game finishes when there is no "_" or run out of lives"""

lives = 6
chosen_word = "banana"
len_word = len(chosen_word)
word = ["_"]*len_word



while True: 
    print(word)
    letter = input("Guess a letter: ")
    if letter.isalpha() and len(letter)==1:
        if letter in chosen_word:
            for x in range(len_word):
                if letter==chosen_word[x]:
                    word[x] = letter
          # replace the "_" with the letter
        else:
            lives = lives - 1
            print("lives:", lives)
        # lose a life
    else: 
        lives = lives - 1
        print("lives:", lives)
    # lose a life
    if lives==0:
        print("Game over pleb")
        break
    if not "_" in word:
        print("You've won champ:", chosen_word)
        break


