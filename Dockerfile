FROM python:3.9-slim
WORKDIR /app
COPY install.txt .
ARG WEATHER_API_KEY
RUN pip install --no-cache-dir -r install.txt
COPY . .
RUN python main.py