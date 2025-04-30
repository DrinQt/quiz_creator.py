import random

def load_questions(file_name):
    """Load questions and answers from a text file."""
    questions = []
    try:
        with open(file_name, 'r') as file:
            content = file.read().split('\n\n') # Split by double newlines
            for block in content:
                lines = block.strip().split('\n')
                if len(lines) < 2: #Just to make sure we have at least a question and an answer
                    continue

                question = lines[0].strip() # First line is the question
                options = [line.strip() for line in lines[1:-1]] # All lines except the last one are options
                correct_answer_line = lines[-1] # Last line is the correct answer
                