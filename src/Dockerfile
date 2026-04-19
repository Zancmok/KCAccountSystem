FROM python:3.14-slim

ENV APP_VERSION="alpha-0.0.1"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["sh", "-c", "python main.py"]
