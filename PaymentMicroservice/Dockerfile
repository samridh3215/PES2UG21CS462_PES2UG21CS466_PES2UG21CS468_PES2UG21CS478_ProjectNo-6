FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . PayementMicroservice
WORKDIR /PayementMicroservice

# EXPOSE 8080
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8080"]


