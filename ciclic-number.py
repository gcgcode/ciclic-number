# Check if input is a number
def isValidInput():
    validGuess = False
    guess = input("Enter number: ")


    while not validGuess:
        validGuess = guess.isdigit()
        if not validGuess:
            guess = input("Invalid characters. Please enter valid number: ")
    
    return guess

# Check if the input number is a ciclic number
def checkCiclicNumber(guess):
    contains = False 
    
    for i in range(len(guess)):
        if(i>=1):
            product = int(guess)*(i+1)
            print(str(guess) + " x " + str(i+1) + " = " + str(product))
            for j in range(len(str(product))):
                if(guess[j] in str(product)):
                    contains = True
                else:
                    contains = False
                    break
            
            if(not contains):
                break
        
    return contains


inputN = isValidInput()

if(checkCiclicNumber(inputN)):
    print("El número " + str(inputN) + " SÍ es cíclico.")
else:
    print("El número " + str(inputN) + " NO es cíclico.")
