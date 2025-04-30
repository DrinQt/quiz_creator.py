import random 

# Function to create a quiz with multiple-choice questions
def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()

