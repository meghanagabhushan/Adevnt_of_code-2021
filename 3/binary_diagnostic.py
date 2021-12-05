# /**
#  * @author Megha Nagabhushan
#  */
from collections import Counter
from os import replace
def get_file_lines_as_list(filename):
    """Return a list where each element is a line in the file."""
    with open("3/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

input_data = get_file_lines_as_list("input_2.txt")

def get_counts(n):
    ones =  n.count('1')
    zeros = n.count('0')
    if ones<zeros:
        return '0',zeros,'1',ones
    elif ones==zeros:
        return 'X',zeros,'X',ones
    else:
        return '1',ones,'0',zeros

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def get_epsilon_gamma(input_data):
    re_grouped_data = []
    for i in range(len(input_data[0])):
        regroup=""
        for data in input_data:
            regroup = regroup + data[i]
        re_grouped_data.append(regroup)
    min_bin = ""
    max_bin = ""
    for x in re_grouped_data:
        char_1,max,char_2,min = get_counts(x)
        min_bin = min_bin + char_2
        max_bin = max_bin + char_1
    epsilon = int(min_bin, 2)
    gamma = int(max_bin, 2)

    return epsilon,gamma

def get_final_bytes(input_data,type):
    input_filter = input_data
    for i in range(len(input_data[0])):
        bit_list = ""
        if len(input_filter)!=1:
            for data in input_filter:
                bit_list = bit_list+data[i]
            max_char,max_count,min_char,min_count = get_counts(bit_list)

            #for oxygen_generator
            if type == "max":
                max_char = max_char.replace('X','1')
                for data in input_filter:
                    filter_list = [x for x in input_filter if x[i]!=max_char]
            
            #for CO2_scrubber
            if type == "min":
                min_char = min_char.replace('X','0')
                for data in input_filter:
                    filter_list = [x for x in input_filter if x[i]!=min_char]
        
            input_filter = Diff(input_filter,filter_list)
            print(input_filter)
    return input_filter

oxygen_generator_byte = get_final_bytes(input_data,"max")
CO2_scrubber_byte = get_final_bytes(input_data,"min")
oxygen_generator = int(oxygen_generator_byte[0],2)
CO2_scrubber = int(CO2_scrubber_byte[0],2)

epsilon,gamma = get_epsilon_gamma(input_data)

#Part 1 solution
print(epsilon*gamma)
#input_1.txt -> 198
#input_2.txt -> 2035764

#Part 2 solution
print(oxygen_generator*CO2_scrubber)
#input_1.txt -> 230
#input_2.txt -> 2817661


    



    
    

