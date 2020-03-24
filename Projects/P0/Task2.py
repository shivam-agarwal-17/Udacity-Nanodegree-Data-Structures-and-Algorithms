"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict

phone_num_to_time = defaultdict(lambda: 0)
for record in calls:
    time_spent = int(record[-1]) 
    phone_num_to_time[record[0]] += time_spent
    phone_num_to_time[record[1]] += time_spent
    
max_time = -1
max_time_ph = None
for ph, time in phone_num_to_time.items():
    if time > max_time:
        max_time = time
        max_time_ph = ph
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_time_ph, max_time))
