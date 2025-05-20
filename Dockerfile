FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application and archive
COPY app.py ./

# Install dependencies
RUN pip install --no-cache-dir flask
RUN mkdir -p /app/data

# Expose port
EXPOSE 8080

# Run the app
CMD ["python", "app.py"]