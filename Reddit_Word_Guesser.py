import praw
import config
import time
import random

def bot_login():
    login = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "Word_Finder Version 1.0")
    return login

def getWord(login):
    for comment in login.subreddit("all").comments(limit=100):
        if len(comment.body) > 50:
            words = comment.body.split(" ")
            for word in words:
                if len(word) >= 5 and len(word) <= 7:
                    return word.lower().strip(".").strip(",").strip("'").strip('"')

def main():
    
    login = bot_login()
    word = getWord(login)

    print("\nWord acquired, time to guess!")
    print("Hint: the word is of length",len(word),"and the first letter is '"+word[0]+"'.")
    print("Type 'quit' to terminate the game, 'hint' for one extra hint.")
    print("Type 'reveal' to see your word if you just want to know, (this will reset the game).\n")
    print("***Guesses and commands are not case sensitive!***\n")
    
    hintUsed = False
    guess = ""    
    wordHash = {}
    for char in word:
        wordHash[char] = wordHash.get(char, 0) + 1
        
    while guess != word:
        guess = input().lower()
        if guess == word:
            win(word)
        elif guess == "quit":
            print("Game terminated.")
            return
        elif guess == "hint":
            if hintUsed == True:
                print("Hint was already used!")
            else:
                randomIndex = random.randint(1,len(word)-1)
                print("\nThe "+str(randomIndex+1)+"th/[rd] letter of the word is: '"+word[randomIndex]+"'.")
                hintUsed = True
                print("In other words, this is the word so far: ")
                toPrint = [word[0]]
                for i in range(1,randomIndex):
                    toPrint.append("_")
                toPrint.append(word[randomIndex])
                for j in range(randomIndex+1,len(word)):
                    toPrint.append("_")
                print("".join(toPrint)+"\n")
        elif guess == "reveal":
            print("The word was: "+word+".")
            print("Restarting game...")
            main()
        else:
            guessHash = {}
            score = 0            
            for char in guess:
                guessHash[char] = guessHash.get(char, 0) + 1
            for index in wordHash:
                if index in guessHash:
                    if guessHash[index] > wordHash[index]:
                        score+= wordHash[index]
                    else:
                        score += guessHash[index]
            print("Score currently is: "+str(score)+".")
            print("Guess again!")

def win(word):
    print("\nCongratulations! '"+word+"' was the word!")
    print("Play again? Y/N (not case sensitive)")
    key = input()
    while key != "y" and key.lower() != "n":
        print("Not 'Y' or 'N'. Try again")
        key = input().lower()
    if key == "y":
        main()
    else:
        print("\n*****************************************")
        print("Game terminated, congratulations on winning!")
        print("*****************************************")

def intro():
    print("*****************************************")
    print("Welcome to the Reddit Word Guessing Game!")
    print("*****************************************")
    print("For instructions, press i.\n")
    print("Otherwise, press any other key to begin.")
    key = input()
    if key.lower() == "i":
        instructions()
    else:
        main()

def instructions():
    print("*****************************************")
    print("INSTRUCTIONS:")
    print("A random word will be found in any subreddit, and you will")
    print("be given hints to guess what that word is and also be awarded")
    print("a point for every correct letter of the word.\n")
    print("Good luck!")
    print("*****************************************")
    main()
      
intro()
