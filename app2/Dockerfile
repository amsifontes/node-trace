FROM python:3.8

RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:./app:./node_trace_client"

COPY ./app2/requirements.txt ./app/requirements.txt
RUN pip install -r ./app/requirements.txt

COPY ./app2 ./app
COPY ./node_trace_client ./node_trace_client

CMD ["python", "./app/app2.py"]