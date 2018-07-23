FROM python:latest

WORKDIR /math-pomodoro

COPY templates templates/
COPY *.py /math-pomodoro/

RUN pip install Flask

EXPOSE 5001

ENV FLASK_APP main.py

ENTRYPOINT ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5001"]
