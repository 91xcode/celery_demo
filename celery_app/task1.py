# -*- coding: utf-8 -*-
import time
from celery_app import app
from celery.signals import task_postrun



@app.task
def add(x, y):
    time.sleep(20)
    return x + y




@app.task
def crontab_add(x, y):
    time.sleep(2)
    return x + y


@task_postrun.connect
def task_postrun_handler(sender=None, task_id=None, task=None, args=None, kwargs=None, retval=None, state=None, **kwds):
    """任务完成的信号处理函数"""
    print '''   Done!
    sender: %s
    task_id: %s
    task: %s
    retval: %s
    state: %s
    args:%s
    kwargs:%s
    kwds:%s''' % (sender, task_id, task, retval, state, args, kwargs, kwds,)

