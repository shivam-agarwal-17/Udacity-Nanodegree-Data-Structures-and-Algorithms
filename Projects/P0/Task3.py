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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

codes = set()

total_calls_from_b = 0
total_calls_to_b = 0

for record in calls:
    if not record[0].startswith('(080)'):
        continue  
    total_calls_from_b += 1
    receiving_num = record[1]
    if receiving_num.find(' ') != -1: # mobile number
        codes.add(receiving_num[:4])
    elif receiving_num.startswith('140'): # telemarketer
        codes.add('140')
    else: # check for other fixed lines
        split_num = receiving_num.split(')')
        if len(split_num) == 2:
            receiving_code = split_num[0][1:4]
            if receiving_code == '080':
                total_calls_to_b += 1
            codes.add(receiving_code)
        
# Part A
codes = sorted(codes)
print("The numbers called by people in Bangalore have codes:")
print(*codes, sep='\n')
print('\n')

# Part B
perc = 100. * (total_calls_to_b / total_calls_from_b)
print(f"{perc:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
