# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:24:14 2017

@author: trevi
"""

import pandas as pd

birddata = pd.read_csv("bird_tracking.csv")

birddata.info()

import matplotlib.pyplot as plt

import numpy as np

ix = birddata.bird_name == "Eric"
x, y = birddata.longitude[ix], birddata.latitude[ix]

plt.figure(figsize=(7,7))
plt.plot(x, y, ".")

bird_names = pd.unique(birddata.bird_name)


plt.figure(figsize=(7,7))

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x, y, ".", label=bird_name)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3traj.pdf")


ix = birddata.bird_name == "Eric"
speed = birddata.speed_2d[ix]
ind = np.isnan(speed)
plt.hist(speed[~ind])
plt.savefig("hist.pdf")

plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0,30,20), normed=True)
plt.xlabel("2D Speed (m/s)")
plt.ylabel("Frequency")
plt.savefig("hist.pdf")


birddata.speed_2d.plot(kind="hist", range=[0,30])
plt.xlabel("2D Speed (m/s)"); 
plt.savefig("pd_hist.pdf")

import datetime

date_str = birddata.date_time[0]

datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []

for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index=birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time - times[0] for time in times]

plt.plot(np.array(elapsed_time) / datetime.timedelta(days=1))
plt.xlabel("Observation")
plt.ylabel("Elapsed Time (days)")
plt.savefig("timeplot.pdf")

#Calculating Daily Mean Speed

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []

for (i,t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds =[]

plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean Speed (m/s)")
plt.savefig("dms.pdf")

### Using the Cartopy Library

import cartopy.crs as ccrs
import cartopy.feature as cfeature






































