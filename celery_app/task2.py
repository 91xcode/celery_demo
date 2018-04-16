# -*- coding: utf-8 -*-
import time
from celery_app import app


@app.task
def multiply(x, y):
    time.sleep(2000)
    return x * y



@app.task
def crontab_multiply(x, y):
    time.sleep(2)
    return x * y
