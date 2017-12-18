# Reddit-Word-Guessing-Bot
Word guessing game that takes random words off of Reddit and lets you guess what it is!

To play the game, you must setup your own config.py file using your Reddit account information (just make a new one) and go to:
https://www.reddit.com/prefs/apps/

If you do not have "PRAW"(Python Reddit API Wrapper) installed, you can install it via pip by typing:

<i>pip install praw</i>

1) Click "are you a developer? create an app..." or "create another app..."
2) Click the "script" button and fill in any information
3) Edit my config.py file, put it in the same directory as the game file.
     Format it like this:
        username = "your Reddit username here"
        password = "your Reddit password here"
        client_id = "code under the title of your script"
        client_secret =	"code next to the word 'secret'"
4) Run the Reddit_Word_Guesser.py file
5) Have fun!

Devpost link:
https://devpost.com/software/reddit-random-word-guessing-game
