
def switch_day(argument):
    switcher = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return switcher.get(argument, "Invalid month")


date_list = [2020, 1, 9, 4, 3, 0, 20, 0]
print(date_list)

date_list_now = [2020, 2, 17, 2, 14, 55, 0, 0]
print(date_list_now)

start_year, start_month, start_day, start_weekday, start_hour, start_minute, start_second, * other = [
    2020, 1, 9, 4, 3, 0, 20, 0]
year_now, month_now, day_now, weekday_now, hour_now, minute_now, second_now, * \
    other_now = date_list_now
print(day_now)

time = date_list[4:7]
print("")
print("Time: ", str(time))

weekday = date_list[3]
day = switch_day(weekday)
print("Day: ", str(day))

date1 = date_list[0:3]
print("Date: ", str(date1))

date2 = str(date_list[2]) + ', ' + str(date_list[1]) + ', ' + str(date_list[0])
print("Date: ", str(date2))
