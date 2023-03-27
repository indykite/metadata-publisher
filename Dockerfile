FROM python:3.11-slim

# Do not generate .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Do not buffer python output
ENV PYTHONUNBUFFERED 1

COPY . /

RUN pip install pipenv

RUN pipenv install --deploy --system

ENTRYPOINT python /send-analytics-data.py \
  $GITHUB_EVENT_NAME $GITHUB_REPOSITORY $GITHUB_SHA \
  $INPUT_ENV $INPUT_VERSION $INPUT_STATUS $INPUT_BIGQUERY_TABLE
