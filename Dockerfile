FROM python:3.9.18
ENV PYTHONBUFFERED 1

ENV DOCKER=True

RUN ["mkdir", "/data"]
RUN ["mkdir", "/donarsangre"]

WORKDIR /donarsangre

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python donarsangre/manage.py makemigrations ; \
    python donarsangre/manage.py migrate ; \
    python donarsangre/manage.py loaddata testData.json ; \
    python donarsangre/manage.py rebuild_index --noinput ; \
    python donarsangre/manage.py runserver 0.0.0.0:8000
