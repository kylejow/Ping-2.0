#https://learn.sparkfun.com/tutorials/graph-sensor-data-with-python-and-matplotlib/update-a-graph-in-real-time

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pythonping import ping
import threading
import os
import time

def pingHost(host):
    return ping(host, timeout = 2000, count = 1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys, host, start):
    xs.append(str(time.time() - start) + 's')
    ys.append(pingHost(host).rtt_max*1000)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.plot(xs, ys)
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Pinging ' + host)
    plt.ylabel('Latency (ms)')

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, '8.8.8.8', time.time()), interval=100)
plt.show()