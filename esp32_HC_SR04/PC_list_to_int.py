# read from file and wirte
# calculate the time passed between readings
# Manuel Lameira


def str_to_int(lst):
    for i in range(0, len(lst)):
        lst[i] = int(lst[i])
    return lst


# Read from file
rtc_readings = []

with open("test_list_to_int.txt", mode='r') as rtc_file:
    #contents = rtc_file.read()
    for line in rtc_file:
        rtc_readings.append(line.lstrip(
            'Last reading of total_discharge: ').rstrip('\n'))
    # for element in rtc_readings:
    #     print(element, end='')

# Reading the last value of the array
print(rtc_readings)

# using naive method to
# perform conversion
# for i in range(0, len(rtc_readings)):
#     rtc_readings[i] = int(rtc_readings[i])

mod = str_to_int(rtc_readings)

# Printing modified list
print("Modified list is lamu : " + str(mod))
print("sum of modified list: " + str(sum(rtc_readings)))
# test_list = [1, 4, 3, 6, 7]
for i in range(10):
    # Wirte to file
    # 'w' = write --> new file
    # 'a' = append
    # when with is used, no need to close the file
    with open("test_list_to_int.txt", mode='a') as file:
        file.write('Last reading of total_discharge: {} \n'.format(i))
