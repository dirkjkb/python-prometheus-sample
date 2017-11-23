from bottle import Bottle
from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram, Summary

application = Bottle()
COUNTER = Counter('test_counter', 'count')
GAUGE = Gauge('test_gauge', 'gauge')
HISTOGRAM = Histogram('test_histogram', 'histogram')
SUMMARY = Summary('test_summary', 'summary')


@application.get('/summary/<num>')
def histogram(num):
    SUMMARY.observe(int(num))


@application.get('/histogram/<num>')
def histogram(num):
    HISTOGRAM.observe(int(num))


@application.get('/gauge/+/<num>')
def gauge_inc(num):
    GAUGE.inc(int(num))


@application.get('/gauge/-/<num>')
def gauge_dec(num):
    GAUGE.dec(int(num))


@application.get('/gauge/=/<num>')
def gauge_set(num):
    GAUGE.set(int(num))


@application.get('/counter/<num>')
def inc(num):
    COUNTER.inc(int(num))


@application.get('/')
def index():
    with open('api.json') as f:
        return f.read()


@application.get('/metrics')
def metrics():
    return generate_latest(REGISTRY)


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, reloader=True)
