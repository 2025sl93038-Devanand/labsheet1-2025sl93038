FROM python:3.14
 
WORKDIR /app
 
COPY . /app
 
CMD ["python", "calculator.py"]