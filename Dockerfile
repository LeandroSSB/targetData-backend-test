FROM python:3.9.6

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
