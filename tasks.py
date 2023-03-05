import time
from celery import Celery

# broker - адрес redis
# backend - адрес бэкедн (база данных)

app = Celery(
    broker='redis://127.0.0.1/1',
    backend='redis://127.0.0.1/2'
)


# cpu_bound может размещаться внутри celery
@app.task
def cpu_bound(a):
    time.sleep(1)

    return a