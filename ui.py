import tkinter as tk

THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self):
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

        # Set tuple to half-width, half-height for centered text
        self.text_question = self.canvas.create_text(
            (150, 125),
            text="Question",
            fill="black",
            font=("Arial", 20, "italic"))

        image_false = tk.PhotoImage(file="./images/false.png")
        self.button_false = tk.Button(
            image=image_false,
            width=100,
            height=97,
            bd=0,
            highlightthickness=0)

        image_true = tk.PhotoImage(file="./images/true.png")
        self.button_true = tk.Button(
            image=image_true,
            width=100,
            height=97,
            bd=0,
            highlightthickness=0)

        # Grid Layout
        self.label_score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # Add Y padding around canvas
        self.button_false.grid(row=2, column=0)
        self.button_true.grid(row=2, column=1)

        self.window.mainloop()

    def next_question(self):
        pass

        # self.canvas.itemconfig(self.text_question, text=question)

    def check_answer(self):
        pass

        # self.score = 0
        # self.score_text = str(self.score)
