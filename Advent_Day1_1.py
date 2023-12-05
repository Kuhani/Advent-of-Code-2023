result = 0
calibration_value = []
file = open("day1_input.txt", "r")
input = file.read()
input_list = input.split('\n')
for line in input_list:
    for value in line:
        if value.isnumeric() == True:
            calibration_value.append(value)
            result_line = int(calibration_value[0])*10 + int(calibration_value[-1])
    result += result_line
    calibration_value = []
print(result)
