FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . AuthenticationMicroservice
WORKDIR /AuthenticationMicroservice

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]


