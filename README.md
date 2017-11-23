# Python Prometheus Cient
This library is a testing library for the Prometheus Endpoint.
It is implemented with the python client api https://github.com/prometheus/client_python.
If you want to know more about the metric types you can look at https://prometheus.io/docs/concepts/metric_types/.

## Api
For simplicity this Api only contains GET methods.

| HTTP METHOD | URL              | Response                              |
| ----------- | ---------------- | ------------------------------------- |
| GET         | /                | returns api                           |
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
pip install requirements.txt
```
after installing you can run it with
```
python app.py
```

## DOCKER
The build Docker image can be found https://hub.docker.com/r/dirkjkb/python-prometheus-client/.
You can also build it with the following commands.
```
docker build -t sample:prometheus-client .
```
```
docker build -t sample:prometheus-client .
```