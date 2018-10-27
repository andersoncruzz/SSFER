import os
import time
import datetime

def make_dirs(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def get_date_string():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H_%M_%S+%Y-%m-%d')
    return st
