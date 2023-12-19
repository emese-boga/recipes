FROM python:3.11 as base

RUN apt update && apt install --yes --no-install-recommends \
    entr \
    netcat-traditional \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/src \
    && mkdir -p /app/coverage \
    && mkdir -p /app/htmlcov

WORKDIR /app
COPY entrypoint .coveragerc .version pyproject.toml requirements.txt /app/
COPY ./src /app/src

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

ARG CONTEXT=local
ENV CONTEXT=${CONTEXT}

ENTRYPOINT ["/app/entrypoint"]
VOLUME [ "/app/coverage" ]
VOLUME [ "/app/htmlcov" ]

EXPOSE 80
CMD [ "start" ]