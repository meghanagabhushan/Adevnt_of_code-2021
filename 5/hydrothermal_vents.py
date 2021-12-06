# /**
#  * @author Megha Nagabhushan
#  */
import pandas as pd
import numpy as np

def get_file_lines_as_list2(filename):
    """Return a list where each element is a line in the file."""
    return [line.rstrip() for line in open("5/"+filename)]

input_data = get_file_lines_as_list2("input_2.txt")

print(input_data)
points = []

def get_points(data):
    remove_arrow = data.split(" -> ")
    remove_arrow = [i.split(",") for i in remove_arrow]
    x1_y1 = [int(x) for x in remove_arrow[0]]
    x2_y2 = [int(x) for x in remove_arrow[1]]
    x1 = x1_y1[0]
    y1 = x1_y1[1]
    x2 = x2_y2[0]
    y2 = x2_y2[1]
    return x1,y1,x2,y2

def intermediates(x1, y1, x2, y2):
    if x1<=x2:
        x = [i for i in range(x1,x2+1)]
    else:
        x = [i for i in range(x2,x1+1)]
    if y1<=y2:
        y = [i for i in range(y1,y2+1)]
    else:
        y = [i for i in range(y2,y1+1)]
    points_list = []
    for i in x:
        for j in y:
            points_list.append([i,j])
    return points_list

def get_max_number():
    max = 0
    for data in input_data:
        x1, y1, x2, y2 = get_points(data)
        if(x1>max):
            max = x1
        if(x2>max):
            max = x2
        if(y1>max):
            max = y1
        if(y2>max):
            max = y2
    return max
max = get_max_number()

def get_diagonal_points(start_x, start_y, end_x, end_y):
    if start_x > end_x:
        start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y
    result = []
    slope = (end_y - start_y) // (end_x - start_x)
    for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
        result.append([i,j])
    result.append([i,j])
    result.append([start_x, start_y])
    result.append([end_x, end_y])
    res = []
    [res.append(x) for x in result if x not in res]
    return res

def get_solution1():
    df = pd.DataFrame(np.zeros((max+1, max+1)))
    count = 0
    for data in input_data:
        x1, y1, x2, y2 = get_points(data)
        if x1==x2 or y1==y2:
            points_list = intermediates(x1, y1, x2, y2)
            for point in points_list:
                x = point[0]
                y = point[1]
                df[x][y] = df[x][y]+1
                if df[x][y] == 2:
                    count = count+1
    return count

def get_solution2():
    df = pd.DataFrame(np.zeros((max+1, max+1)))
    counter_list = []
    for data in input_data:
        x1, y1, x2, y2 = get_points(data)
        if x1==x2 or y1==y2:
            points_list = intermediates(x1, y1, x2, y2)
            for point in points_list:
                x = point[0]
                y = point[1]
                df[x][y] = df[x][y]+1
                if df[x][y] >= 2:
                    counter_list.append([x,y])
        else:
            points_list = get_diagonal_points(x1, y1, x2, y2)
            for point in points_list:
                x = point[0]
                y = point[1]
                df[x][y] = df[x][y]+1
                if df[x][y] >= 2:
                    counter_list.append([x,y])

    result_list = []
    [result_list.append(x) for x in counter_list if x not in result_list]
    return len(result_list)

print("Solution 1 "+str(get_solution1()))
#input_1.txt -> 5, input_2.txt -> 6572
print("Solution 2 "+str(get_solution2()))
#input_1.txt -> 12, input_2.txt -> 21466