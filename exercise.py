import random

class SubtractionExerciseFactory:
    def generate(self):
        subtraction_exercise = Exercise()

        for id in range(0, 10):
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

class Exercise:
    def __init__(self):
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
