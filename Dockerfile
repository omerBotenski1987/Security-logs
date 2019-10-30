FROM python:2.7
ADD send_demo_data.py /
COPY log_data.py /
COPY logs_template.py /
COPY program.py /

RUN pip install pystrich
RUN pip install requests
ENTRYPOINT [ "python", "./send_demo_data.py" ]
