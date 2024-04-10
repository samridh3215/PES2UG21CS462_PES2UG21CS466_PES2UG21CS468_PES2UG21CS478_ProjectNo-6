FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . Item_ManagementMicroservice
WORKDIR /Item_ManagementMicroservice

# EXPOSE 8000
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]


