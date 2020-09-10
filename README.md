# Python Prometheus Cient
This library is a testing library for the Prometheus Endpoint.
It is implemented with the python client api https://github.com/prometheus/client_python.
If you want to know more about the metric types you can look at https://prometheus.io/docs/concepts/metric_types/.

## Api
For simplicity this Api only contains GET methods.

| HTTP METHOD | URL              | Response                              |
| ----------- | ---------------- | ------------------------------------- |
| GET         | /docs            | returns the open api definition       |
| GET         | /metrics         | returns prometheus metrics            |
| GET         | /histogram/{num} | Sets histogram values                 |
| GET         | /summary/{num}   | Sets summary values                   |
| GET         | /counter/{num}   | adds value to total counter sum       |
| GET         | /gauge/+/{num}   | adds value to total gauge sum         |
| GET         | /gauge/-/{num}   | subtracts value from total gauge sum  |
| GET         | /gauge/=/{num}   | setts gauge value                     |

## RUN

First off all you have to install all dependencies listed in the requirements.txt
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
after installing you can run it with
```
uvicorn app:app --host 0.0.0.0 --port 8000
```

## DOCKER
The build Docker image can be found https://hub.docker.com/r/dirkjkb/python-prometheus-sample/.
You can also build it with the following commands.
```
docker build -t sample:prometheus-client .
```
```
docker build -t sample:prometheus-client .
```
