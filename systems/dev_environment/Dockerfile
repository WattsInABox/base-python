FROM python:3.7.6-alpine3.11

MAINTAINER Billy Watson

# pull in arguments from docker-compose or docker command line
ARG PROJECT_DEPLOY_ROOT
ARG PROJECT_NAME

LABEL description="Dev container for ${PROJECT_NAME}"

ENV PYTHONUNBUFFERED=1

COPY ./python-requirements/* ./
# do all the pip installs in a clean fashion so we don't bloat the container
RUN pip install --no-cache-dir -r test_requirements.txt -r project_requirements.txt

WORKDIR ${PROJECT_DEPLOY_ROOT}
