FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . OrderMicroservice
WORKDIR /OrderMicroservice

# EXPOSE 3000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:3000"]


