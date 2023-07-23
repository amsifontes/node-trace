FROM python:3.8

RUN pip install --upgrade pip

ENV PYTHONPATH "${PYTHONPATH}:./app:./node_trace_client"

COPY ./app3/requirements.txt ./app/requirements.txt
RUN pip install -r ./app/requirements.txt

COPY ./app3 ./app
COPY ./node_trace_client ./node_trace_client

CMD ["python", "./app/app3.py"]