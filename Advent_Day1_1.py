result = 0
calibration_value = []
values = ["0","1","2","3","4","5","6","7","8","9"]
file = open("day1_input.txt", "r")
input = file.read()
input_list = input.split('\n')
for line in input_list:
    for value in line:
        if value in values:
            calibration_value.append(value)
            result_line = int(calibration_value[0])*10 + int(calibration_value[-1])
    result += result_line
    calibration_value=[]
print(result)