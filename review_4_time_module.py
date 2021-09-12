#%%
print(dir())

print(dir(__builtin__)) # type: ignore
print()
for item in dir(__builtin__): # type: ignore
    print(item)

# help(dir)


# %%
import shelve
import random
# print(dir())
print()

# Show all objects in module shelve
# print(dir(shelve))

# Show only METHODS in  Shelf object in shelve module
# print(dir(shelve.Shelf))
# print()

for each_obj in dir(shelve.Shelf):
    if each_obj[0] != '_':
        print(each_obj)

# help(dir)

# help() to show the definition of one specific object/method
help(random.randint)


# %%
print('----------------------WEBBROWSER MODULE--------------------------')
import webbrowser

# webbrowser.open('https://www.python.org/', new=1)
url = "https://www.python.org/"
chrome = webbrowser.get(using='windows-default')
chrome.open_new(url)

# %%
print('----------------------TIME MODULE--------------------------')
import time
print(time.gmtime(0))
print(time.localtime())
print(time.time())


# %%
import time

time_here = time.localtime()
print(time_here)
print()

print("Year:" , time_here[0], time_here.tm_year)
print("Month:" , time_here[1], time_here.tm_mon)
print("Day:" , time_here[2], time_here.tm_mday)


# %%
print('----------------------TIME MODULE--------------------------')
import time

# To deal with real times rather than just measuring dureations
from time import time as my_timer

# Measure actual elapse time (BEST WAY)
# from time import perf_counter as my_timer # good to use for elasped time


# from time import monotonic as my_timer

# Want to know how much time the CPU is spent on particular task
from time import process_time as my_timer


import random

input("Press enter to start")
wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("Started at ", time.strftime("%X", time.localtime(start_time)))
print("ended at ", time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds.".format(end_time-start_time))


# %%
print('----------------------TIME MODULE--------------------------')
import time

print("TIME(): \t", time.get_clock_info('time'))
print("PERF_COUNTER(): \t", time.get_clock_info('perf_counter'))
print("MONOTONIC(): \t", time.get_clock_info('monotonic'))
print("PROCESS_TIME(): \t", time.get_clock_info('process_time'))



# %%
print('----------------------TIMEZONE MODULE--------------------------')
import time

print("The epoch on this system starts at ", time.strftime('%c', time.gmtime(0)))
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is ", time.tzname[1])

print()
print("Local time is", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))



#%%
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())



# %%
print('----------------------TIMEZONE MODULE NAIVE TIME--------------------------')
import pytz  # type: ignore
import datetime

country = ('Europe/Moscow')
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))
print()

# for x in pytz.all_timezones:
#     print(x)


# for name in sorted(pytz.country_names):
#     print(name, ": ", pytz.country_names[name])


# for name in sorted(pytz.country_names):
#     print("{}: {}: {}".format(name, pytz.country_names[name], pytz.country_timezones.get[name]))


# with open("D:\python\Python_practice\documents\Timezones.txt", 'w') as timezones_file:
#     for name in sorted(pytz.country_names):
#         print("{}: {}: {}".format(name, pytz.country_names[name], pytz.country_timezones.get(name)), file=timezones_file)

# print("Completed writing Timezones.txt") 

with open("D:\python\Python_practice\documents\Timezones_2.txt", 'w') as timezones_file:
    for name in sorted(pytz.country_names):
        print("{}: {}".format(name, pytz.country_names[name]), end=': ', file=timezones_file)
        if name in pytz.country_timezones:
            for zone in sorted(pytz.country_timezones[name]):
                tz_to_display = pytz.timezone(zone)
                local_time = datetime.datetime.now(tz=tz_to_display)
                print("\t\t{}: {}".format(zone,local_time), file=timezones_file)
        else:
            print("\t\tNo time zone defined", file=timezones_file)


# %%
print('----------------------TIMEZONE MODULE AWARE TIME--------------------------')
import pytz  # type: ignore
import datetime

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()


print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))
print()

aware_local_time = pytz.utc.localize(utc_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware utc time {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

# %%
import pytz  # type: ignore
import datetime

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())


s = 1445711400
t = s + (60*60) # current time s in seconds + 1 hours in seconds

gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
print()

dt3 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt4 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)
print("{} seconds since the epoch is {}".format(s, dt3))
print("{} seconds since the epoch is {}".format(t, dt4))
print()
# %%
