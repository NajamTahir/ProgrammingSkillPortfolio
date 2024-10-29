from tkinter import *
import random

# Function to display the menu and get user's difficulty selection
def displayMenu():
    def selectDifficulty(level):
        global difficulty
        difficulty = level
        root.destroy()

    root = Tk()
    root.geometry("500x500")
    root.title("Arithmetic Quiz")
    Label(root, text="DIFFICULTY LEVEL", font=('Helvetica', 16)).pack(pady=10)
    
    Button(root, text="1. Easy", font=('Helvetica', 14), command=lambda: selectDifficulty(1)).pack(pady=5)
    Button(root, text="2. Moderate", font=('Helvetica', 14), command=lambda: selectDifficulty(2)).pack(pady=5)
    Button(root, text="3. Advanced", font=('Helvetica', 14), command=lambda: selectDifficulty(3)).pack(pady=5)
    
    root.mainloop()

# Function to generate random integer based on difficulty level
def randomInt():
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

# Function to randomly decide the operation
def decideOperation():
    return random.choice(['+', '-', '*', '/', '%'])

# Function to display a problem and accept user answer
def displayProblem():
    global num1, num2, operation, user_answer, attempts
    num1, num2 = randomInt(), randomInt()
    operation = decideOperation()
    
    # Ensure division by zero doesn't happen
    if operation == '/' and num2 == 0:
        num2 = randomInt()
    
    question = f"{num1} {operation} {num2} = "
    user_answer.set("")
    label_question.config(text=question)
    attempts = 0

# Function to check if the user's answer is correct
def isCorrect():
    global score, attempts
    try:
        user_ans = float(user_answer.get())
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        return

    # Calculate the correct answer
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        correct_answer = round(num1 / num2, 2)  # Division is rounded to 2 decimal places
    elif operation == '%':
        correct_answer = num1 % num2

    if user_ans == correct_answer:
        if attempts == 0:
            score += 10
            result_label.config(text="Correct! +10 points")
        else:
            score += 5
            result_label.config(text="Correct! +5 points")
        root.after(1000, nextQuestion)
    else:
        if attempts == 0:
            attempts += 1
            result_label.config(text="Incorrect, try again!")
        else:
            result_label.config(text=f"Incorrect! The correct answer was {correct_answer}")
            root.after(1000, nextQuestion)

# Function to display the results after the quiz
def displayResults():
    result_window = Toplevel(root)
    result_window.geometry("500x500")
    result_window.title("Results")
    
    grade = ""
    if score > 90:
        grade = "A+"
    elif score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    else:
        grade = "F"
    
    Label(result_window, text=f"Your final score: {score}/100", font=('Helvetica', 16)).pack(pady=10)
    Label(result_window, text=f"Your grade: {grade}", font=('Helvetica', 16)).pack(pady=10)

    Button(result_window, text="Play Again", command=lambda: restartQuiz(result_window)).pack(pady=10)
    Button(result_window, text="Quit", command=root.quit).pack(pady=10)

# Function to move to the next question or finish the quiz
def nextQuestion():
    global question_count
    if question_count < 10:
        question_count += 1
        displayProblem()
    else:
        displayResults()

# Function to restart the quiz
def restartQuiz(window):
    window.destroy()
    resetGame()
    displayMenu()
    startQuiz()

# Function to reset game variables
def resetGame():
    global score, question_count
    score = 0
    question_count = 1

# Function to start the quiz
def startQuiz():
    global root, label_question, result_label, user_answer
    root = Tk()
    root.geometry("500x500")
    root.title("Arithmetic Quiz")

    label_question = Label(root, text="", font=('Helvetica', 16))
    label_question.pack(pady=20)

    user_answer = StringVar()
    Entry(root, textvariable=user_answer, font=('Helvetica', 16)).pack(pady=10)

    Button(root, text="Submit", font=('Helvetica', 14), command=isCorrect).pack(pady=10)
    result_label = Label(root, text="", font=('Helvetica', 14))
    result_label.pack(pady=10)

    displayProblem()
    root.mainloop()

# Main program flow
difficulty = 1
score = 0
question_count = 1
displayMenu()
startQuiz()
