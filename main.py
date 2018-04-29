from flask import Flask, render_template, request

from factories import MultiplicationExerciseFactory, SubtractionEquationsFactory

app = Flask(__name__)

@app.route('/')
def generate_exercise():
    subtraction_exercise_factory = SubtractionEquationsFactory()
    multiplication_exercise_factory = MultiplicationExerciseFactory()
    
    subtraction_exercise = subtraction_exercise_factory.generate()
    multiplication_exercise = multiplication_exercise_factory.generate()
    
    return render_template('exercise.html', exercise=multiplication_exercise)

@app.route('/pomodoro')
def evaluate_exercise():
    
    return render_template('pomodoro.html')