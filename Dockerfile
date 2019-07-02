FROM python:3.7.3-stretch

WORKDIR /math-pomodoro

COPY templates templates/
COPY *.py /math-pomodoro/

RUN pip install Flask

EXPOSE 5001

ENV FLASK_APP main.py

ENTRYPOINT ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5001"]

# docker build -t math-pomodoro:latest .
# docker run -d -p 5001:5001 math-pomodoro:latest