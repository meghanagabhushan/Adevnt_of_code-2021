# /**
#  * @author Megha Nagabhushan
#  */
import pandas as pd

def get_file_lines_as_list(filename):
    """Return a list where each element is a line in the file."""
    with open("Advent_of_code-2021/4/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
input_data = get_file_lines_as_list("input_2.txt")

numbers = input_data[0]
random_numbers = numbers.replace(" ","").split(",")
input_data = input_data[1:]

def list_split(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for y in range(n-len(every_chunk))]
        yield every_chunk

input_list = list(list_split(input_data,6))

input_list_matrix = []
for set in input_list:
    while "" in set:
        set.remove("")
    for i,value in enumerate(set):
        values = value.split(" ")
        while "" in values:
            values.remove("")
        set[i] = values
    input_list_matrix.append(set)

matrix_dict = {}
for i,data in enumerate(input_list_matrix):
    matrix_dict[i] = pd.DataFrame(data, columns = ['C1', 'C2','C3','C4','C5'])

def check_rows_for_match(df):
    for index, row in df.iterrows():
        if row['C1'] == row['C2'] == row['C3'] == row['C4'] == row['C5'] == 'X':
            return True

def check_columns_for_match(df):
    for column in df:
        column_values = df[column].tolist()
        #print(column_values)
        count = 0
        for value in column_values:
            if value == 'X':
                count = count +1
        if(count==5):
            return True

def get_solution_1():
    break_out_flag = False
    resultant_dataframe_index = 0
    last_number = 0
    for number in random_numbers:
        last_number = number
        for key,df in matrix_dict.items():
            df = df.replace(number,'X')
            matrix_dict[key] = df
        for key,df in matrix_dict.items():
            rows_match = check_rows_for_match(df)
            columns_match = check_columns_for_match(df)
            if rows_match or columns_match:
                break_out_flag = True
                resultant_dataframe_index = key
                break
        if break_out_flag:
            break
    return resultant_dataframe_index,last_number

def get_solution_2():
    break_out_flag = False
    resultant_dataframe_index = 0
    last_number = 0
    all_keys = list(matrix_dict.keys())
    for number in random_numbers:
        last_number = number
        for key,df in matrix_dict.items():
            df = df.replace(number,'X')
            matrix_dict[key] = df
        for key,df in matrix_dict.items():
            if key in all_keys:
                rows_match = check_rows_for_match(df)
                columns_match = check_columns_for_match(df)
                if rows_match or columns_match:
                    if len(all_keys)>1:
                        if key in all_keys:
                            all_keys.remove(key)
                    else:
                        resultant_dataframe_index = key
                        last_number = number
                        break_out_flag = True
                        break
        if break_out_flag:
            break
    return resultant_dataframe_index,last_number

def get_result(resultant_dataframe_index,last_number):
    resultant_dataframe = matrix_dict[resultant_dataframe_index]
    resultant_dataframe = resultant_dataframe.replace('X','0')
    b = resultant_dataframe.astype(int)
    sum_values = b.values.sum()
    return sum_values*int(last_number)

resultant_dataframe_index_1,last_number_1 = get_solution_1()
solution_1 = get_result(resultant_dataframe_index_1,last_number_1)
print(solution_1)
#input_1.txt -> 4512, input_2.txt -> 44088
resultant_dataframe_index_2,last_number_2 = get_solution_2()
solution_2 = get_result(resultant_dataframe_index_2,last_number_2)
print(solution_2)
#input_1.txt -> 1924, input_2.txt ->23670

