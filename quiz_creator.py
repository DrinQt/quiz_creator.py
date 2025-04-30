import random 

# Function to create a quiz with multiple-choice questions
def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()

# Each questions block has 5 lines + 1 for the correct answer
        for i in range(0, len(lines), 6):
            if i + 5 < len(lines): # Ensure there are enough lines for a question block
                question_line = lines[i].strip()
                options = [lines [i + j].strip() for j in range(1, 5)] # For the 4 options
                correct_answer_line = lines[i + 5].strip()

                #Get the correct answer from the options
                correct_answer = correct_answer_line.split(': ')[1].strip().upper() #For the letters (A, B, C, D)

                # Store the question, options, and correct answer
                questions.append((question_line, options, correct_answer))
    
    return questions
def quiz(questions):
    ransom.shuffle(questions) # Shuffle the questions
    for question, options, correct_answer in questions:
        print(question) # Prints the question
        for option in options:
            print(option) # Prints the options

        user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Get the user's answer

        if user_answer == correct_answer:
            print("Wow! You got it right!")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

            
