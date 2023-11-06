def find_available_times(schedule_1, schedule_2, daily_activity_1, daily_activity_2, meeting_duration):
    available_times = []
    for i in range(len(schedule_1)):
        end_time1 = schedule_1[i][1]
        end_min1 = end_time1.split(':')[1]
        end_min_m1 = int(end_min1) + meeting_duration
        end_hour_m1 = int(end_min_m1 / 60)
        end_hour_m1 += int(end_time1.split(':')[0])
        end_hour_m1 = str(end_hour_m1)
        if end_min_m1 >= 10 and end_min_m1 < 60:
            end_min_m1 = str(end_min_m1)
        elif end_min_m1 > 60:
            end_min_m1 -= 60
            end_min_m1 = str(end_min_m1)
        elif end_min_m1 == 60:
            end_min_m1 = '00'
        else:
            end_min_m1 = f'0{end_min_m1}'
        end_time_m1 = end_hour_m1 + ':' + end_min_m1
        if i == len(schedule_1) - 1:
            compare_time1 = daily_activity_1[1]
        else:
            compare_time1 = schedule_1[i+1][0]
        end_time_float1 = float(end_time1.replace(':', '.'))
        end_time_float_m1 = float(end_time_m1.replace(':', '.'))
        compare_time_float1 = float(compare_time1.replace(':', '.'))
        for j in range(len(schedule_2)):
            end_time2 = schedule_2[j][1]
            end_min2 = end_time2.split(':')[1]
            end_min_m2 = int(end_min2) + meeting_duration
            end_hour_m2 = int(end_min_m2 / 60)
            end_hour_m2 += int(end_time2.split(':')[0])
            end_hour_m2 = str(end_hour_m2)
            if end_min_m2 >= 10 and end_min_m2 < 60:
                end_min_m2 = str(end_min_m2)
            elif end_min_m2 > 60:
                end_min_m2 -= 60
                end_min_m2 = str(end_min_m2)
            elif end_min_m2 == 60:
                end_min_m2 = '00'
            else:
                end_min_m2 = f'0{end_min_m2}'
            end_time_m2 = end_hour_m2 + ':' + end_min_m2
            if j == len(schedule_2) - 1:
                compare_time2 = daily_activity_2[1]
            else:
                compare_time2 = schedule_2[j+1][0]
            end_time_float2 = float(end_time2.replace(':', '.'))
            end_time_float_m2 = float(end_time_m2.replace(':', '.'))
            compare_time_float2 = float(compare_time2.replace(':', '.'))
            # ------- Start algorithm -------
            if end_time_float_m1 <= compare_time_float1 and end_time_float1 >= end_time_float2 and end_time_float_m1 <= compare_time_float2:
                if compare_time_float1 <= compare_time_float2:
                    available_times.append([end_time1, compare_time1])
                else:
                    available_times.append([end_time1, compare_time2])
            if end_time_float_m2 <= compare_time_float2 and end_time_float2 >= end_time_float1 and end_time_float_m2 <= compare_time_float1:
                if compare_time_float2 <= compare_time_float1:
                    available_times.append([end_time2, compare_time2])
                else:
                    available_times.append([end_time2, compare_time1])
    return available_times


# Read input from 'input.txt' file
result = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

for i in range(0, len(lines), 5):
    # person1_schedule = eval(file.readline())
    # person1_daily_activity = eval(file.readline())
    # person2_schedule = eval(file.readline())
    # person2_daily_activity = eval(file.readline())
    # duration_of_meeting = eval(file.readline())
    person1_schedule = eval(lines[i])
    person1_daily_activity = eval(lines[i + 1])
    person2_schedule = eval(lines[i + 2])
    person2_daily_activity = eval(lines[i + 3])
    duration_of_meeting = eval(lines[i+4])
    # Find available meeting times
    available_meeting_times = find_available_times(person1_schedule, person2_schedule, person1_daily_activity, person2_daily_activity, duration_of_meeting)
    result.append(available_meeting_times)
    print(available_meeting_times)

with open("output.txt", "w") as outfile:
    for result in result:
        outfile.write(str(result))
