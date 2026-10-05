FROM python:3.12
 
WORKDIR /app
 
COPY . .
 
RUN pip install pandas requests
 
CMD ["python","scripts/fetch.py"]