from pythonping import ping
import threading
import os
import time

def pingHost(host):
    time = ping(host, timeout = 2000, count = 1)
    return time.rtt_max*1000
# pinging the host


print(pingHost('8.8.8.8'))
time.sleep(1)
os.system('cls')

