from question_modules import questions

class Question:
    def __init__(self, question, answer):
        self.question= question
        self.answer= answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        

    def quizing(self) :
        q = self.question_list[self.question_number].question
        answer = input (f"Q.{(self.question_number) + 1} {q} (True/False)\n[Your answer should be 'True' or 'False']: ").lower()
        right = self.question_list[self.question_number].answer
        self.question_number += 1
        self.checking(answer, right)
        
    def checking (self, answer, right):
        if answer == right:
            self.score += 1
            print("You're Right!!")
        else:
            print("You're Wrong!!")
        print(f"Correct answer was: {right}")
        print(f"Your score is {self.score} / {self.question_number}")

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            print(f"Congratulations! You've Completed The Quiz And Your Final Score Is {self.score} / {len(self.question_list)}")
            return False
        else:
            return True
        


def play_quiz(question_bank):
    quiz = QuizBrain(question_bank)
    while quiz.still_has_question():
        quiz.quizing()       
    



question_bank=[]
for each in questions:
    question = each["question"]
    answer = each["correct_answer"].lower()
    new_question = Question(question, answer)
    question_bank.append(new_question)



retry = 'y'
while retry == 'y':
    print("\n" * 50)
    play_quiz(question_bank)
    retry= input("Retry? 'y' for yes 'n' for no: ")

