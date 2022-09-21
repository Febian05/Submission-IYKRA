FROM python:3.10

WORKDIR /google-cloud-storage

RUN pip install --upgrade google-cloud-storage

# Copy all files from local to docker
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS = 'prismatic-cider-363006-cec37421fdb6.json'

CMD ["python", "/google-cloud-storage/main.py"]