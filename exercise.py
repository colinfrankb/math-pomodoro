from datetime import datetime
import random

class SubtractionExerciseFactory:
    def generate(self):
        subtraction_exercise = Exercise()

        for id in range(10, 40):
            expression = self._generate_two_digit_expression()
            question = Question(
                id=id,
                expression=expression,
                answer=eval(expression)
            )
            subtraction_exercise.questions.append(question)

        # for id in range(0, 10):
        #     expression = self._generate_expression()
        #     question = Question(
        #         id=id,
        #         expression=expression,
        #         answer=eval(expression)
        #     )
        #     subtraction_exercise.questions.append(question)

        return subtraction_exercise

    def _generate_expression(self):
        subtractor = random.randrange(200, 1000)
        low_hundred = random.randrange(subtractor)
        subtractee = random.randrange(1,10) * 1000 + low_hundred

        return '{0} - {1}'.format(subtractee, subtractor)

    def _generate_two_digit_expression(self):
        subtractor_unit = random.randrange(2, 10)
        subtractee_unit = random.randrange(1, subtractor_unit)

        subtractee_tens = random.randrange(2, 9)
        subtractor_tens = random.randrange(1, subtractee_tens)
        
        subtractee = subtractee_tens * 10 + subtractee_unit
        subtractor = subtractor_tens * 10 + subtractor_unit

        return '{0} - {1}'.format(subtractee, subtractor)

class Exercise:
    def __init__(self):
        self.timestamp = datetime.now()
        self.questions = []

class Question:
    def __init__(self, id, expression, answer):
        self.id = id
        self.expression = expression
        self.answer = answer

# thousandth = random.randrange(1, 10) * 1000
# high_hundredth = random.randrange(2, 10)
# high_hundred = high_hundredth * 100
# low_hundred = random.randrange(1, high_hundredth) * 100
# complete_low_hundred = random.randrange(low_hundred, low_hundred + 100)
# subtractee = thousandth + complete_low_hundred
# subtractor = random.randrange(high_hundred, 1000)

# print('Algorithm A', subtractee, '-', subtractor)
