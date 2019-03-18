import sys
import requests
import threading
import Queue
import string
import getopt

lock = threading.Lock()
thread_number = 20


def domain_test(site):
    global lock
    try:
        conn = requests.get(site)
        if conn.status_code == 302:
            pass
        elif conn.status_code == 200:
            return site
        else:
            pass
    except:
        pass
