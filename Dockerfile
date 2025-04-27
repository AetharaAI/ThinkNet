# Start from official Python base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system-level build tools
RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev wget unzip

# Upgrade pip
RUN pip install --upgrade pip

# Copy project
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Expose API port
EXPOSE 8000

# Run the Hive Mind
CMD ["uvicorn", "run_brain_collective:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
