# parent image
FROM python:3.10-slim  

# essential env variables
ENV PYHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


#copying all contents from local to app
COPY . .

#Run setup.py
RUN pip install --no-cache-dir -e .

#ports
#streamlit
EXPOSE 8501
#fastapi backend
EXPOSE 9999

#Run the app
CMD ["python", "app/main.py"]