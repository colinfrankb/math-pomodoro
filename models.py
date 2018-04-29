from datetime import datetime

class Exercise:
    def __init__(self):
        self.timestamp = datetime.now()
        self.questions = []

class Question:
    def __init__(self, id, expression, answer):
        self.id = id
        self.expression = expression
        self.answer = answer
