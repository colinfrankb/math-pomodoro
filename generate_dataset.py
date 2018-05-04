from factories import MultiplicationEquationsFactory, SubtractionEquationsFactory
from models import Exercise

subtraction_equations_factory = SubtractionEquationsFactory()
exercise = Exercise()
subtraction_equations_factory.appendTo(exercise)

def is_desired_question(question):
  return question.answer > 10

with (open('dataset.csv', mode='wb')) as file:
  for question in exercise.questions:
    line = '{0},{1},{2},{3}\n'.format(
      question.expression.first_term,
      question.expression.second_term,
      question.answer,
      is_desired_question(question)
    )
    file.write(line.encode())
