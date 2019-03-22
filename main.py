from flask import Flask, render_template, request

from factories import MultiplicationEquationsFactory, SubtractionEquationsFactory, TwoDigitMultiplicationEquationsFactory, RoundedDivisionEquationsFactory
from models import Exercise

app = Flask(__name__)

@app.route('/')
def generate_exercise():
    subtraction_equations_factory = SubtractionEquationsFactory()
    multiplication_equations_factory = MultiplicationEquationsFactory()
    
    exercise = Exercise()

    subtraction_equations_factory.appendTo(exercise)
    multiplication_equations_factory.appendTo(exercise)
    
    return render_template('exercise.html', exercise=exercise)

@app.route('/multiplication')
def generate_multiplication_exercise():
    two_digit_multiplication_equations_factory = TwoDigitMultiplicationEquationsFactory()
    
    exercise = Exercise()

    two_digit_multiplication_equations_factory.appendTo(exercise)
    
    return render_template('exercise.html', exercise=exercise)

@app.route('/division')
def generate_division_exercise():
    three_digit_rounded_division_equations_factory = RoundedDivisionEquationsFactory()
    
    exercise = Exercise()

    three_digit_rounded_division_equations_factory.appendTo(exercise)
    
    return render_template('exercise.html', exercise=exercise)

@app.route('/pomodoro')
def evaluate_exercise():
    
    return render_template('pomodoro.html')