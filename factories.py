import random

from models import *

class SubtractionEquationsFactory:
    def generate(self):
        subtraction_exercise = Exercise()

        for id in range(10, 30):
            expression = self._generate_two_digit_expression()
            question = Question(
                id=id,
                expression=expression,
                answer=eval(expression)
            )
            subtraction_exercise.questions.append(question)

        for id in range(31, 41):
            expression = self._generate_expression()
            question = Question(
                id=id,
                expression=expression,
                answer=eval(expression)
            )
            subtraction_exercise.questions.append(question)

        return subtraction_exercise

    def _generate_expression(self):
        subtractor = random.randrange(200, 1000)
        low_hundred = random.randrange(subtractor)
        subtractee = random.randrange(1,10) * 1000 + low_hundred

        return '{0} - {1}'.format(subtractee, subtractor)

    def _generate_two_digit_expression(self):
        subtractor_unit = random.randrange(3, 10)
        subtractee_unit = random.randrange(1, subtractor_unit - 1)

        subtractee_tens = random.randrange(2, 9)
        subtractor_tens = random.randrange(1, subtractee_tens)
        
        subtractee = subtractee_tens * 10 + subtractee_unit
        subtractor = subtractor_tens * 10 + subtractor_unit

        return '{0} - {1}'.format(subtractee, subtractor)

class MultiplicationExerciseFactory:
    def generate(self):
        multiplication_exercise = Exercise()

        for id in range(10, 30):
            expression = self._generate_two_digit_expression()
            question = Question(
                id=id,
                expression=expression,
                answer=eval(expression)
            )
            multiplication_exercise.questions.append(question)

        return multiplication_exercise

    def _generate_two_digit_expression(self):
        first_number = random.randrange(10, 100)
        second_number = random.randrange(2, 10)

        return '{0} * {1}'.format(first_number, second_number)
