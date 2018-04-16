# -*- coding: utf-8 -*-

from datetime import timedelta
from celery.schedules import crontab

from kombu import Queue


BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'  # 指定 Backend

####################################
# 一般配置 #
####################################
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json','msgpack']
#指定消息代理和执行结果都使用Redis，任务（消息）使用msgpack序列化，结果使用json序列化，任务结果保存时间24小时等
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'                             
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2'
)


# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app.task1.crontab_add',
         'schedule': timedelta(seconds=30),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.crontab_multiply',
        'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}



#默认队列
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_DEFAULT_ROUTING_KEY = 'celery'
#CELERYD_LOG_FILE="./logs/celery.log"
CELERY_QUEUEs = (
    Queue("queue_add", routing_key='queue_add'),
    Queue('queue_mult', routing_key='queue_mult'),
    Queue('celery', routing_key='celery'),
    )
CELERY_ROUTES = {
    'celery_app.task1.add':{'queue':'queue_add', 'routing_key':'queue_add'},
    'celery_app.task2.multiply':{'queue':'queue_mult', 'routing_key':'queue_mult'},
}


