def get_file_lines_as_list(filename):
    """Return a list where each element is a line in the file."""
    with open("1/"+filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
input_list = get_file_lines_as_list("2/input1.txt")

def get_horizontal_vertical_depth(input_list):
    horizontal = 0
    vertical = 0
    depth = 0
    for x in input_list:
        direction = x.split(" ")[0]
        pos = int(x.split(" ")[1])
        print(direction,pos)
        if direction=='forward':
            horizontal = horizontal + pos
            depth = depth + (pos * vertical)
        elif direction=='down':
            vertical = vertical + pos
        else:
            vertical = vertical - pos
    return horizontal,vertical,depth

horizontal,vertical,depth = get_horizontal_vertical_depth(input_list)
print("output 1 : "+str(horizontal*vertical))
#Input1 -> 150
#Input2 -> 2150351
print("output 2 : "+str(horizontal*depth))
#Input1 -> 900
#Input2 -> 1842742223