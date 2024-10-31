import html
from question_module import Question

class QuizBrain:
    def __init__(self, question_module : Question):
        self.question_number = 0
        self.question_module = question_module
        self.right_answer = html.unescape(self.question_module.answer)
        self.options = [html.unescape(option) for option in self.question_module.options]
        self.question_text = html.unescape(self.question_module.question)
        self.score = 0
        self.quizing()
        

    def quizing(self) :
        return f"Question : \n\t{self.question_text} \noptions : \n\t {self.options}"
        
    def checking (self, answer):
        if self.options[answer] == self.right_answer:
            return True
        else:
            return False


