FROM amd64/python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8080
COPY ./app /app

# Temporary limitation -- need the main container to persist while the cron job runs
CMD ["/bin/bash", "-c", "--", "while true; do sleep 90; done;"]
