# /**
#  * @author Megha Nagabhushan
#  */
from typing import Counter
import pandas as pd
import numpy as np

def get_file_lines_as_list2(filename):
    """Return a list where each element is a line in the file."""
    return [line.rstrip() for line in open("6/"+filename)]

input_data = get_file_lines_as_list2("input_1.txt")[0]
states = {}
#days=80
days = 256
states[0] = [int(x) for x in input_data.split(",")]
for i in range(0,days+1):
    states[i] = states[0]

for i,v in states.items():
    if i-1 in states.keys():
        print(i)
        counter = 0
        previous_state=states[i-1]
        d = Counter(previous_state)
        counter = d[0]
        current_state = [6 if x==0 else x-1 for x in previous_state]
        current_state = current_state + [8] * counter
        states[i] = current_state
print(len(states[days]))

#         d = Counter(previous_state)
#         counter = d[0]
#     print(i)
#     current_state = []
#     if i-1 in states.keys():
#         day=i
#         counter = 0
#         previous_state=states[i-1]
#         d = Counter(previous_state)
#         counter = d[0]
#         #current_state = [x-1 for x in previous_state]
#         current_state = [6 if x==0 else x-1 for x in previous_state]      
#         current_state = current_state + [8] * counter
#         #print(current_state,counter)
#         #print(i)
#         states[i] = current_state
# print(len(states[days]))
#input_2.txt -> 351092