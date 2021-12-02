# /**
#  * @author Megha Nagabhushan
#  */
import numpy as np

input_file = "input2.txt"

def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def get_sonar_sweep_output(input_data,window):
    count = 0
    rolled_data = rolling_window(np.array(input_data), window)
    initial = rolled_data[0]
    for tup in rolled_data:
        if sum(tup)>sum(initial):
            count = count+1
        initial = tup
    return count

def get_file_lines_as_list(filename):
    with open("1/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def main():
    data = get_file_lines_as_list(input_file)
    print(data)
    input_data = [int(x) for x in data]
    part1_output = get_sonar_sweep_output(input_data,1)
    part2_output = get_sonar_sweep_output(input_data,3)
    print(part1_output)
    print(part2_output)
    #input.txt -> output -> 7,5
    #input2.txt -> output -> 1301, 1346

if __name__ == "__main__":
    main()