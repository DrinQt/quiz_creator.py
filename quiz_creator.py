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