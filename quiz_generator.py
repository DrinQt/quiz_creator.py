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

                # Getting the correct answer
                if "Correct Answer :" in correct_answer_line:
                    correct_answer = correct_answer_line.split(':')[-1].strip()
                    questions.append((question, options, correct_answer))
                else:
                    print(f"Skipping Invalid block: {block}")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return questions

def ask_question(question, options, correct_answer):
    """Ask the user a question and check if the answer is correct."""
    print(question)
    for option in options:
        print(option)

    user_answer = input("Your answer (a/b/c/d): ").strip().lower()

    if user_answer == correct_answer:
        print("Galing ah! You got it right!")
    else:
        print(f"Mali! Wrong answer! The correct answer is: {correct_answer}")

def main():
    """Main Function to run the quiz."""
    file_name = 'quiz_questionnaires.txt'

    while True:
        questions = load_questions(file_name)
        
        if not questions:
            print("No questions available.")
            return

        questions, options,correct_answer = random.choice(questions) # Randomly select a question
        ask_question(question, options, correct_answer)

        
    