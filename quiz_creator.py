import random 

# Function to create a quiz with multiple-choice questions
def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            # Each question block has 5 lines + 1 for the correct answer
            for i in range(0, len(lines), 6):
                if i + 5 < len(lines):  # Ensure there are enough lines for a question block
                    question_line = lines[i].strip()
                    options = [lines[i + j].strip() for j in range(1, 5)]  # For the 4 options
                    correct_answer_line = lines[i + 5].strip()

                    # Extract the correct answer from the options
                    if ':' in correct_answer_line:
                        correct_answer = correct_answer_line.split(":")[1].strip() # Get the lette (A, B, C, D) from the line
                    else:
                        print(f"Invalid format for correct answer in line: {correct_answer_line}")
                        continue # Skip this question if format is invalid

                    # Store the question, options, and correct answer in a tuple
                    questions.append((question_line, options, correct_answer))
    except FileNotFoundError:
        print(f"File {filename} not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return questions

def quiz(questions):
    random.shuffle(questions)  # Shuffle the questions
    for question, options, correct_answer in questions:
        print(question)  # Prints the question
        for index, option in enumerate(options):
            print(f"{chr(65 + index)}. {option}")  # Prints the options with letters (A, B, C, D)

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()  # Get the user's answer

        if user_answer == correct_answer:
            print("Wow! You got it right!")
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

        # If the user wants to continue or quit
        play_again = input("Do you want to continue? (yes/no): ")
        if play_again.lower() != 'yes':
            break

# Main function to run the quiz
def main():
    filename = 'quiz_questionnaires.txt'  # The file containing the questions
    questions = load_questions(filename)  # Load the questions from the file

    if not questions:
        print("No questions found in the file.")
        return
    
    while True:
        quiz(questions)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

if __name__ == "__main__":
    main()  # Run the main function to start the quiz
