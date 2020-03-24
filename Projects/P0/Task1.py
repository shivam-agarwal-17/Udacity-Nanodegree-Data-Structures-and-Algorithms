"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phone_num_list = []
for record in texts:
    phone_num_list += record[:2]
    
for record in calls:
    phone_num_list += record[:2]
    
distinct_phone_num_set = set(phone_num_list)
    
print("There are {} different telephone numbers in the records.".format(len(distinct_phone_num_set)))