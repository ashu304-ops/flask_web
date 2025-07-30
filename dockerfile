FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Initialize the SQLite DB during build
RUN python db.py

EXPOSE 5000

CMD ["python", "app.py"]
