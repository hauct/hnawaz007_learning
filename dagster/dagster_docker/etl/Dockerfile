# Dagster libraries to run both dagster-webserver and the dagster-daemon. Does not
# need to have access to any pipeline code.

FROM python:3.10-slim

RUN pip install \
    dagster \
    dagster-graphql \
    dagster-webserver \
    dagster-postgres \
    dagster-docker

# Set $DAGSTER_HOME and copy dagster instance and workspace YAML there
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

RUN mkdir -p $DAGSTER_HOME

COPY dagster.yaml workspace.yaml $DAGSTER_HOME
COPY etl ./etl
COPY pyproject.toml .
COPY setup.cfg .
COPY setup.py .

EXPOSE 3000

CMD ["dagster-webserver", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3000"]