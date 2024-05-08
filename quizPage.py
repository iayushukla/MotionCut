from tkinter import *
import json


#opening json file
def loadQuestions(qQ):
    with open('qQ.json', 'r') as file:
        return json.load(file)

#Global Variable 
questionData = loadQuestions('qQ.json') 
currentQuestionIndex = 0
score = 0




#Check answer
def check_answer(selected_option):
    global currentQuestionIndex, score
    correct_answer_index = questionData[currentQuestionIndex]['answer']
    if selected_option == correct_answer_index:
        score += 1
    currentQuestionIndex += 1
    if currentQuestionIndex < len(questionData):
        display_question()
    else:
        quesLabel.config(text="Quiz Completed! Your Score: " + str(score) + "/" + str(len(questionData)))


# Start the quiz
def start_quiz(name):
    lbl.grid_forget()  # Hide name label and entry
    txt.grid_forget()
    btn.grid_forget()
    welcome_label.config(text=f"Welcome, {name}! Let the QUIZ begin...")
    display_question()


# Display question
def display_question():
    global currentQuestionIndex
    quesLabel.config(text=questionData[currentQuestionIndex]['question'])
    for i in range(4):
        option_buttons[i].config(text=questionData[currentQuestionIndex]['options'][i])


def submit_name():
    name = txt.get()  # Get the name entered by the user
    welcome_label.config(text=f"Welcome, {name}! \nLet the QUIZ begin...")   

# Display a personalized welcome message

# Create the app window
root = Tk()
root.title("MotionCut Ayush Quiz")
root.geometry('800x400')

# Label and Entry for name input
lbl = Label(root, text="Enter your name:")
lbl.grid(row=0, column=0)

txt = Entry(root, width=20)
txt.grid(row=0, column=1)

# Button to submit name
btn = Button(root, text="Done", fg="Red", command=lambda: start_quiz(txt.get()))
btn.grid(row=0, column=2)

# Label to display welcome message
welcome_label = Label(root, text="")
welcome_label.grid(row=1, columnspan=3)

#Question label
quesLabel = Label(root, text="", wraplength=600)
quesLabel.grid(row=2, column=0, columnspan=2, pady=10)  # Changed row to 2 and spanned two columns

# Option buttons
option_buttons = []
for i in range(4):
    button = Button(root, text="", width=20, command=lambda index=i: check_answer(index))
    button.grid(row=i+3, column=0, padx=10, pady=5)  # Incremented row by 3 to avoid overlapping with other widgets
    option_buttons.append(button)



display_question()

# Run the app
root.mainloop()

