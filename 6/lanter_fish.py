# /**
#  * @author Megha Nagabhushan
#  */
from collections import defaultdict
from typing import Counter
import pandas as pd
import numpy as np

def get_file_lines_as_list2(filename):
    """Return a list where each element is a line in the file."""
    return [line.rstrip() for line in open("6/"+filename)]

input_data = get_file_lines_as_list2("input_2.txt")[0]
input_state = [int(x) for x in input_data.split(",")]
states = {}
days=256
states_count = {x:input_state.count(x) for x in input_state}
for i in range(0,9):
    if not i in states_count.keys():
        states_count[i]=0

print(states_count)

def get_state(previous_count):
    current_count = {}
    current_count[7] = previous_count[8]
    current_count[6] = previous_count[7] + previous_count[0]
    current_count[5] = previous_count[6]
    current_count[4] = previous_count[5]
    current_count[3] = previous_count[4]
    current_count[2] = previous_count[3]
    current_count[1] = previous_count[2]
    current_count[0] = previous_count[1]
    current_count[8] = previous_count[0]
    return current_count

current_state = states_count
for i in range(0,days):
    current_state = get_state(current_state)
print(sum(current_state.values()))
#input_2.txt -> 351092 solution 1
#input_2.txt -> 1595330616005 solution 2
