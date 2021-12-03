# /**
#  * @author Megha Nagabhushan
#  */
from collections import Counter
def get_file_lines_as_list(filename):
    """Return a list where each element is a line in the file."""
    with open("1/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

input_data = get_file_lines_as_list("input_2.txt")

re_grouped_data = []
for i in range(len(input_data[0])):
    regroup=""
    for data in input_data:
        regroup = regroup + data[i]
    re_grouped_data.append(regroup)


def get_counts(n):
    ones =  n.count('1')
    zeros = n.count('0')
    if ones<zeros:
        return '0',zeros,'1',ones
    else:
        return '1',ones,'0',zeros

min_bin = ""
max_bin = ""
for x in re_grouped_data:
    char_1,max,char_2,min = get_counts(x)
    min_bin = min_bin + char_2
    max_bin = max_bin + char_1

epsilon = int(min_bin, 2)
gamma = int(max_bin, 2)

print(epsilon*gamma)



