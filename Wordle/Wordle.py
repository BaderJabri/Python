# %% [markdown]
# # Wordle
# imports

# %%
import random

# %% [markdown]
# Gets possible words from the file

# %%
File = open("FiveLetters.txt")
Words = []
for line in File:
    Words.append(line.strip())
File.close()

# %% [markdown]
# Chooses a random word from list

# %%
temp = random.choice(Words)
Chosen = list(temp.strip())


# %% [markdown]
# compares user input and the chosen word

# %%
def compare(userInput, Chosen):
    inputList = list(userInput.strip())
    existance = []
    num = 0
    for i in inputList:
        if i == Chosen[num]: existance.append("Correct")
        elif i == Chosen[0] or i == Chosen[1] or i == Chosen[2] or i == Chosen[3] or i == Chosen[4]: 
            existance.append("Exists")
        else: existance.append("Doesn't exist")
        num += 1
    num = 0
    
    return (existance)



# %% [markdown]
# Main code, give the user 6 tries to guess the word

# %%

inputs = []
counter = 0

print("Five Letter Wordle!")


while counter < 6:
    userInput = input()
    userInput = str.lower(userInput)
    if userInput in set(Words):
        if userInput not in set(inputs):
            inputs.append(userInput)
            counter += 1
            
            print (userInput)
            print (compare(userInput, Chosen))
                
            if compare(userInput, Chosen) == ['Correct', 'Correct', 'Correct', 'Correct','Correct']:
                print (f"congratulations '{userInput}' is correct")
                break
                
            if counter == 6:
                print (f"The word was '{temp}'")
        else:
            print (f"you already tried {userInput}")
    else:
        print(f"{userInput} is not in our words list")
    
    

# %%
print(inputs)



