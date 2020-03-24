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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_callers = set()
call_receivers = set()
texters = set()

for record in texts:
    texters.add(record[0])
    texters.add(record[1])
    
for record in calls:
    outgoing_callers.add(record[0])
    call_receivers.add(record[1])

outgoing_callers.difference_update(call_receivers)
outgoing_callers.difference_update(texters)
telemarketers = sorted(outgoing_callers)

print("These numbers could be telemarketers: ")
for tm in telemarketers:
    print(tm)
