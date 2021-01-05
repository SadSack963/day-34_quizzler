import tkinter as tk
import quiz_brain as qb

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz: qb.QuizBrain):
        self.quiz = quiz

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR)

        self.label_score = tk.Label(
            text="Score: 0",
            font=("Arial", 20, "bold"),
            fg="white",
            bg=THEME_COLOR)

        self.canvas = tk.Canvas(
            bg="white",
            width=300,
            height=250)

        self.text_question = self.canvas.create_text(
            (150, 125),  # Set tuple to half-width, half-height for centered text
            text="Question",
            width=280,  # Set text width for wrapping
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        image_false = tk.PhotoImage(file="./images/false.png")
        self.button_false = tk.Button(
            image=image_false,
            width=100,
            height=97,
            bd=0,
            highlightthickness=0,
            command=self.check_answer_false)

        image_true = tk.PhotoImage(file="./images/true.png")
        self.button_true = tk.Button(
            image=image_true,
            width=100,
            height=97,
            bd=0,
            highlightthickness=0,
            command=self.check_answer_true)

        # Grid Layout
        self.label_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Add Y padding around canvas
        self.button_false.grid(row=2, column=0)
        self.button_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=question)
        else:
            question = "Completed"
            self.canvas.itemconfig(self.text_question, text=question)
            self.button_false.config(state=tk.DISABLED)
            self.button_true.config(state=tk.DISABLED)

    def check_answer_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def check_answer_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.label_score.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1500, self.get_next_question)  # No parentheses in func!!
