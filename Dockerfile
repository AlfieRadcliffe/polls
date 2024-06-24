# build environment
FROM python:3.10

COPY . code
WORKDIR /code

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
