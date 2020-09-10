
from uvicorn import run
from fastapi import FastAPI

from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram, Summary

app = FastAPI()

PROMETHEUS_COUNTER: Counter = Counter('test_counter', 'count')
PROMETHEUS_GAUGE: Gauge  = Gauge('test_gauge', 'gauge')
PROMETHEUS_HISTOGRAM: Histogram = Histogram('test_histogram', 'histogram')
PROMETHEUS_SUMMARY: Summary = Summary('test_summary', 'summary')


@app.get('/summary/{num}')
def summary(num: int) -> None:
    PROMETHEUS_SUMMARY.observe(num)


@app.get('/histogram/{num}')
def histogram(num: int) -> None:
    PROMETHEUS_HISTOGRAM.observe(num)


@app.get('/gauge/+/{num}')
def gauge_inc(num: int) -> None:
    PROMETHEUS_GAUGE.inc(num)


@app.get('/gauge/-/{num}')
def gauge_dec(num: int) -> None:
    PROMETHEUS_GAUGE.dec(num)


@app.get('/gauge/=/{num}')
def gauge_set(num: int) -> None:
    PROMETHEUS_GAUGE.set(num)


@app.get('/counter/{num}')
def inc(num: int) -> None:
    PROMETHEUS_COUNTER.inc(num)


@app.get('/metrics')
def metrics():
    return generate_latest(REGISTRY)
