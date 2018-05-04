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

class Expression:
  def __init__(self, first_term, second_term, symbol):
    self.first_term = first_term
    self.second_term = second_term
    self.symbol = symbol

  def __str__(self):
    return '{0} {2} {1}'.format(
      self.first_term, 
      self.second_term,
      self.symbol
    )
