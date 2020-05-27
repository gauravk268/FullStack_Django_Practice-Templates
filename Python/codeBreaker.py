import random

def generateRandom():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    solution = digits[:3]
    print(solution)
    return solution

def getUserGuess():
    userValue = input("What's your guess: ")
    return userValue

def checkUserGuess(userGuess, gameCode):
    if( userGuess == gameCode ):
        return "Game Won"
    
    results = []
    for index, number in enumerate(userGuess):
        if number == gameCode[:index]:
            results.append("Match")
        elif number in gameCode:
            results.append("Close")
    
    if results == []:
        return "Nope"
    else: 
        return results

print("Game Begins!")
code = generateRandom()
result = []

while result != "Game Won":
    user_guess = getUserGuess()
    result = checkUserGuess(user_guess, code)
    print(code)

    print("Here is the result of your guess:")
    if result == "Game Won":
        print("Game Won!!")
    else:
        for clue in result:
            print(clue)