FROM python:3.10-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install fastapi uvicorn openai

# Copy the app
COPY *.py /app/

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
