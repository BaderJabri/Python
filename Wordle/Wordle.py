import random
import gradio as gr

# Get possible words from the file
File = open("FiveLetters.txt")
Words = []
for line in File:
    Words.append(line.strip())
File.close()

# Choose a random word from the list
temp = random.choice(Words)
Chosen = list(temp.strip())

# Define variables for tracking turns and guesses
counter = 0
inputs = []
correct_guesses = []

# Compare user input and the chosen word
def compare(userInput, Chosen):
    inputList = list(userInput.strip())
    existence = []
    num = 0
    for i in inputList:
        if i == Chosen[num]:
            existence.append("Correct")
        elif i in Chosen:
            existence.append("Exists")
        else:
            existence.append("Doesn't exist")
        num += 1
    return existence


# Define the function for the Gradio interface
def play_wordle(user_input):
    global counter, inputs, correct_guesses
    if counter < 6:
        user_input = user_input.lower()
        if user_input in Words:
            if user_input not in inputs:
                inputs.append(user_input)
                counter += 1
                result = compare(user_input, Chosen)
                if result == ['Correct', 'Correct', 'Correct', 'Correct', 'Correct']:
                    return f"Congratulations! '{user_input}' is correct."
                else:
                    correct_guesses.append(f"{user_input}: {', '.join(result)}")
                    return "\n".join(correct_guesses)
            else:
                
                return "You already tried '{}'.\n".format(user_input) + "\n".join(correct_guesses)
        else:
            return f"'{user_input}' is not a valid word.\n".format(user_input) + "\n".join(correct_guesses)
    else:
        return f"You have reached the maximum number of turns. The word was '{temp}'."


# Create the Gradio interface
iface = gr.Interface(
    fn=play_wordle,
    inputs="text",
    outputs="text",
    title="Wordle Game",
    description="Guess the word!",
    examples=[["apple"], ["black"], ["lemon"]],
)

# Start the Gradio interface
iface.launch()
