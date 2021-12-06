# /**
#  * @author Megha Nagabhushan
#  * @create date 2021-12-01 23:28:51
#  */
import numpy as np

def get_file_lines_as_list(filename):
    """Return a list where each element is a line in the file."""
    with open("1/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def get_file_lines_as_list2(filename):
    """Return a list where each element is a line in the file."""
    return [line.rstrip() for line in open("5/"+filename)]


def rolling_window(input_list, window):
    """Return a list containing arrays grouped according to a rolling window"""
    a = np.array(input_list)
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

