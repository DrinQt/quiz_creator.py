def main():
    #open the file in write mode
    with open("quiz_questionnaires.txt", "w") as file:
        while True:
            question = input("Enter your question:")

            answers = []
            for option in ["A", "B", "C", "D"]:
                answer = input(f"Enter option {option}:")
                answers.append(answer)
                