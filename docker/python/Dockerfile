FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y libpq-dev gcc git \
    && pip install psycopg2

WORKDIR /app

# Install dependencies:
COPY ./src/api/requirements.txt .
RUN pip install -r requirements.txt

ENV DATABASE_URL="postgresql://postgres:uav@uav/uav"

# Add start script and grant execution rights
ADD ./docker/python/scripts/ /scripts/
RUN chmod +x /scripts/*.sh

CMD ["/scripts/01-init.sh"]
