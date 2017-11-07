from flask import Flask, render_template, request

from exercise import SubtractionExerciseFactory

app = Flask(__name__)

@app.route('/')
def generate_exercise():
    exercise_factory = SubtractionExerciseFactory()
    subtraction_exercise = exercise_factory.generate()
    
    return render_template('exercise.html', exercise=subtraction_exercise)

@app.route('/pomodoro')
def evaluate_exercise():
    
    return render_template('pomodoro.html')