FROM python:3.8.5
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP todo
ENV FLASK_ENV development
CMD ["flask", "run", "--host=0.0.0.0"]
