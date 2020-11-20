import os
import requests
import time


"""
Generate 10 POST requests within 100ms, once per
second at the start of the second. Send request
to consumer
"""

# url of redis server
url = os.getenv('HTTP')
count = 0 
def send_post_requests(n):
    """
    Generate n POST requests within 100ms. 
    Send request to consumer
    """
    for i in range(n):
        # (message number, time send)
        response = requests.post(url, data={str(count): time.time()})
