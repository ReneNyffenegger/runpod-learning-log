FROM python:3.13-slim

ARG ENV_VAR_VAL=default
ENV ENV_VAR_FROM_DOCKERFILE=$ENV_VAR_VAL

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY handler.py .

CMD [ "python", "-u", "handler.py" ]
