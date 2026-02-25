import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    {
        "question":" Which keyword is used to define a function in Python?",
        "option":["function","define","def","fun"],
        "answer":"def"
    },
    {
        "question":"Which data type is used to store multiple values in a single variable?",
        "option":["int","float","list","char"],
        "answer":"list"
    },
    {
        "question":"What is the correct file extension for Python files?",
        "option":[".Python",".pt",".py",".p"],
        "answer":".py"
    },
    {
        "question":"How do you insert comments in Python code?",
        "option":["//","#","/**/","--"],
        "answer":"#"
    },
    {
        "question":"Which loop is used to iterate over a sequence in Python?",
        "option":["repeat","do-while","for","loop"],
        "answer":"for"
    },
    {
        "question":"Which function is used to take input from the user?",
        "option":["input()","scan()","read()","get()"],
        "answer":"input()"
    },
    {
        "question":"What is the output of print(type(10))?",
        "option":["<class 'float'>","<class 'int'>","<class 'str'>","<class 'bool'>"],
        "answer":"<class 'int'>"
    },
    {
        "question":"Which operator is used for exponentiation in Python?",
        "option":["^","**","%","//"],
        "answer":"**"
    },
    {
        "question":"Which of the following is a Python keyword?",
        "option":["value","define","return","print"],
        "answer":"return"
    },
    {
        "question":"Which data structure uses key-value pairs?",
        "option":["list","tuple","dictionary","set"],
        "answer":"dictionary"
    }
]

# Root window
root = tk.Tk()
root.title("Quiz Game Proposed by Pramod Kumar")
root.geometry("1000x600")
root.config(bg="#FAB95B")

# Variables
score = 0
question_index = 0
select_option = tk.StringVar()

# Functions
def load_question():
    select_option.set("")
    q = questions[question_index]
    question_label.config(text=f"Q{question_index+1}. {q['question']}")

    for i in range(4):
        option_button[i].config(
            text=q["option"][i],
            value=q["option"][i]
        )

def show_result():
    messagebox.showinfo(
        "Quiz completed",
        f"Your Score is : {score}/{len(questions)}"
    )
    root.destroy()

def next_question():
    global score, question_index

    if select_option.get() == questions[question_index]["answer"]:
        score += 1

    question_index += 1

    if question_index < len(questions):
        load_question()
    else:
        show_result()

# UI Components
heading_label = tk.Label(
    root,
    text="Quiz Game — Brain Test",
    font=("Arial", 40, "bold"),
    bg="#DA7C7C",
    fg="#000000"
)
heading_label.pack(pady=10)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 20, "bold"),
    bg="#FAB95B",
    fg="#000000"
)
question_label.pack(pady=10)


option_button = []
for i in range(4):
    btn = tk.Radiobutton(
        root,
        text="",
        variable=select_option,
        font=("Arial", 12),
        bg="#FAB95B",
        fg="#000000",
        selectcolor="#FF0241",
        value=""
    )
    btn.pack(anchor="w", padx=110, pady=5)
    option_button.append(btn)

next_button = tk.Button(
    root,
    text="NEXT",
    font=("Arial", 15, "bold"),
    bg="#280905",
    fg="#FFFFFF",
    command=next_question
)
next_button.pack(pady=20)

load_question()
root.mainloop()