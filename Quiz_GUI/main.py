from tkinter import *
import requests
from random import shuffle
from quizbrain import QuizBrain
from question_module import Question
from score_manager import fetch_score


# GETTING QUESTION FROM API
def get_question () :
        response = requests.get(url="https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=multiple")
        data = response.json()
        if data["response_code"] != 0 :
             return None
        else :
            question = data["results"][0]["question"]
            incorrect_answers = data["results"][0]["incorrect_answers"]
            correct_answer = data["results"][0]["correct_answer"]
            incorrect_answers.append(correct_answer)
            shuffle(incorrect_answers)
            return Question(question, correct_answer, incorrect_answers)





# CREATING GUI CLASS
BACKGROUND_COLOR = "#0364fa" 
RIGHT = "#30f400"
WRONG = "#f41a00"
SCORE = fetch_score()

class Quizstage:
    def __init__(self):
        self.quiz = None
        self.score = SCORE
        self.window = Tk()
        self.window.title("Quizzz...")
        self.window.config(padx=20, pady=20, bg= BACKGROUND_COLOR)

        self.score_board = Label(text=f"Score : {self.score}", bg= BACKGROUND_COLOR, fg= "white", font=("Arial", 15, "bold"), anchor="ne")
        self.score_board.grid(column=3, row=0)

        self.canvas = Canvas(height=400, width=400, bg= BACKGROUND_COLOR, highlightthickness=0)
        self.card = PhotoImage(file="card_back.png")
        self.canvas.create_image(200, 200, image=self.card)
        self.question = self.canvas.create_text(200, 200, text="Question", width=195, font=("Arial", 15, "bold"), fill="#26354d")
        self.canvas.grid(column=0, row=1, columnspan=4)

        self.tag = Label(text="Choose Your Answer:", bg= BACKGROUND_COLOR, fg= "white", font=("Arial", 15, "bold"), pady=10)
        self.tag.grid(column=0, row=2, columnspan=4)

        self.optn1 = Button(text="A", padx= 5, pady= 5, bg= "#26354d", fg= "white", font=("Arial", 15, "bold"), command=self.check_if_a)
        self.optn1.grid(column=0, row= 3)
        self.optn2 = Button(text="B", padx= 5, pady= 5, bg= "#26354d", fg= "white", font=("Arial", 15, "bold"), command= self.check_if_b)
        self.optn2.grid(column=1, row= 3)
        self.optn3 = Button(text="C", padx= 5, pady= 5, bg= "#26354d", fg= "white", font=("Arial", 15, "bold"), command= self.check_if_c)
        self.optn3.grid(column=2, row= 3)
        self.optn4 = Button(text="D", padx= 5, pady= 5, bg= "#26354d", fg= "white", font=("Arial", 15, "bold"), command= self.check_if_d)
        self.optn4.grid(column=3, row= 3)

        self.tag = Label(text=" ", bg= BACKGROUND_COLOR, fg= "white", font=("Arial", 15, "bold"), pady=10)
        self.tag.grid(column=0, row=4, columnspan=4)

        self.next_btn = Button(text="Next Question  >>>>", padx= 5, pady= 5, bg= "#2c682a", fg= "white", font=("Arial", 15, "bold"), command= self.update_ui)
        self.next_btn.grid(column=1, row=7, columnspan=4)

        self.close = Button(text="Close And Save Records", padx= 5, pady= 5, bg=WRONG, fg= "white", font=("Arial", 15, "bold"), command= self.store_score)
        self.close.grid(column=1, row=8,columnspan=4)

        self.show_question()
        self.window.mainloop()

    def show_question(self) :
        question = get_question()
        if question is None:
            self.canvas.itemconfig(self.question, text = "No Question! Jump to next question")

        else:    
            self.quiz = QuizBrain(question_module=question)
            q_txt = self.quiz.quizing()
            self.canvas.itemconfig(self.question, text = q_txt)

    def check_if_a (self) :
        self.optn2.config(state="disabled")
        self.optn3.config(state="disabled")
        self.optn4.config(state="disabled")
        check = self.quiz.checking(0)
        if check :
            self.optn1.config(bg=RIGHT)
            self.update_for_right()
        else :
            self.optn1.config(bg=WRONG)
            self.update_for_wrong()

    def check_if_b (self) :
        self.optn1.config(state="disabled")
        self.optn3.config(state="disabled")
        self.optn4.config(state="disabled")
        check = self.quiz.checking(1)
        if check :
            self.optn2.config(bg=RIGHT)
            self.update_for_right()
        else :
            self.optn2.config(bg=WRONG)
            self.update_for_wrong()

    def check_if_c (self) :
        self.optn2.config(state="disabled")
        self.optn1.config(state="disabled")
        self.optn4.config(state="disabled")
        check = self.quiz.checking(2)
        if check :
            self.optn3.config(bg=RIGHT)
            self.update_for_right()
        else :
            self.optn3.config(bg=WRONG)
            self.update_for_wrong()

    def check_if_d (self) :
        self.optn2.config(state="disabled")
        self.optn3.config(state="disabled")
        self.optn1.config(state="disabled")
        check = self.quiz.checking(3)
        if check :
            self.optn4.config(bg=RIGHT)
            self.update_for_right()
        else :
            self.optn4.config(bg=WRONG)
            self.update_for_wrong()
            print ("false")

    def update_for_wrong (self) :
        correct = 0
        for each in range(3) :
            if self.quiz.checking(each) :
                correct = each
                break
        correct_ans = self.quiz.options[correct]
        self.tag.config(text=f"You're Wrong!\nThe correct one is {correct_ans}\nTry for next one.", fg= WRONG)

    def update_for_right (self) :
        self.score += 1
        self.tag.config(text=f"You're Right!\nJump to next one.", fg= RIGHT)

    def update_ui (self) :
        self.tag.config(text="")
        self.score_board.config(text=f"Score : {self.score}")
        self.optn1.config(state="normal", bg="#26354d")
        self.optn2.config(state="normal", bg="#26354d")
        self.optn3.config(state="normal", bg="#26354d")
        self.optn4.config(state="normal", bg="#26354d")
        self.show_question()

    def store_score (self) :
        with open ("my_score.txt" , "w") as note:
            note.write(str(self.score))
        self.window.destroy()




# CREATING AN OBJECT STAGE OF Quizstage CLASS
stage = Quizstage()


    





