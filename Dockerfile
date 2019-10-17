FROM python:2

COPY ./ /usr/src/dsmr-data-service
WORKDIR /usr/src/dsmr-data-service
RUN make all
ENTRYPOINT ["python", "dsmr-data-service.py"]