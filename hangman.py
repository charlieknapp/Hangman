words = ["python", "hangman", "programming", "computer", "artificial", "intelligence", "variable", "function","loop", "algorithm", "debugging", "syntax", "development", "software", "hardware", "network", "internet", "database", "encryption", "security", "binary", "hexadecimal", "compiler", "interpreter", "recursion", "iteration", "object", "class", "inheritance", "polymorphism", 
"abstraction", "encapsulation", "exception", "modularity", "testing", "automation", "framework", "library", "package", "dependency", "repository"]
import random

def check_win(ans,used):
    for i in ans:
        if i not in used:
            return False
    return True

used = []
ans = random.choice(words)
lives = 6
while True:
    if check_win(ans,used) == True:
        print("You win!")
        break
    if lives == 0:
        print("You lose!")
        break
    for letter in ans:
        if letter in used:
            print(letter, end = "")
        else:
            print("_", end="")
    guess = input("\nGuess a letter: ")
    if guess in used:
        print("You've already guessed that letter. Try again.")
    else:
        if guess not in ans:
            lives -= 1
            print(f"Incorrect. You have {lives} lives left.")
        else:
            print("Correct")
            print(f"The word was {ans}")
            used.append(guess)
            