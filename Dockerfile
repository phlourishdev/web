FROM python:latest

LABEL Maintainer="phlourishdev"

WORKDIR /

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
