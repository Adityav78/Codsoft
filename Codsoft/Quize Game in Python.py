import time

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def display_welcome_message():
    print("Welcome to the Quiz Game!\n")
    print("Rules:\n")
    print("You will be asked multiple-choice questions.")
    print("Choose the correct option by entering the corresponding letter (A, B, C, or D).")
    print("Each correct answer earns you one point.")
    print("Let's begin!\n")

def take_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    for question in questions:
        print(question.prompt)
        for option in question.options:
            print(option)
        
        user_answer = input("Your choice (A/B/C/D): ").strip().upper()

        if user_answer == question.answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        print()
    
    return score

def display_result(score, total_questions):
    print("Quiz completed!")
    print(f"Your score is {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"You scored {percentage}%")

def play_again():
    choice = input("Do you want to play again? (yes/no): ").strip().lower()
    return choice == 'yes'

def main():
    while True:
        display_welcome_message()
        questions = [
            Question("What is Python's primary use?", ["A)  Scientific research", "B)  Web development", "C)  Data analysis", "D)  All of the above"], "D"),
            Question("Who is the creator of Python?", ["A)  DMark Zuckerberg", "B)  Guido van Rossum", "C)  Jeff Bezos", "D)  Tim Berners-Lee"], "B"),
            Question("Which statement is used for decision making in Python?", ["A)  if", "B) for","C) while", "D) break"], "A"),
            Question("What is an iterator in Python?", ["A)  A device to play music", "B)  An object that can be iterated (looped) over","C)  The for loop", "D)  USe in Operator"], "B"),
            Question("What is the purpose of a function in Python?", ["A)  To store data", "B)  To define variables","C)  To perform a specific task", "D)  To write comments"], "C"),
           
        ]
      
        score = take_quiz(questions)
        display_result(score, len(questions))
        
        if not play_again():
            print("Thank you for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
