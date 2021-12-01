import numpy as np
with open("1/input2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

data = [int(x) for x in lines]

#print(type(data[0]))

def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

a = rolling_window(np.array(data), 3)

#print(a)
count = 0
initial = a[0]
for tup in a:
    if sum(tup)>sum(initial):
        count = count+1
    initial = tup
print(count)
# count = 0
# initial = int(lines[0])
# for line in lines:
#     #print(type(line))
#     if int(line)>initial:
#         #print(line)
#         count = count+1
#         #initial = line
#     initial = int(line)

# print(count)

    
