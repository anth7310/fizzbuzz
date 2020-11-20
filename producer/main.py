from rq import Queue
from redis import Redis
from functions import send_post_requests
import time


redis_conn = Redis()
q = Queue("low", connection=redis_conn)

"""
Generate n POST requests within 100ms, once per
second at the start of the second. Send request
to consumer
"""
while True:
    q.enqueue(send_post_requests, 10)
    time.sleep(1000)
