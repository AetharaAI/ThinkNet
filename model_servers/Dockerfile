FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn pyyaml
CMD ["uvicorn", "mood_controller:app", "--host", "0.0.0.0", "--port", "8001"]
y