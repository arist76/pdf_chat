
FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend

WORKDIR /backend

ADD ./pdf_chat/ /backend

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./pdf_chat/manage.py", "runserver", "0.0.0.0:8000"]
