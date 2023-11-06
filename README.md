# Meeting Availability Finder

This Python script helps you find available meeting times between two people, taking into account their schedules and daily activities. It reads input data from an 'input.txt' file and writes the results to an 'output.txt' file.

## Prerequisites

Before running this script, make sure you have Python installed on your system.

## How to Use

1. Create an 'input.txt' file with the following format:

   ```
   person1_schedule
   person1_daily_activity
   person2_schedule
   person2_daily_activity
   duration_of_meeting
   ```

   Replace `person1_schedule`, `person1_daily_activity`, `person2_schedule`, `person2_daily_activity`, and `duration_of_meeting` with your own data. Ensure that each component is a valid Python list.

2. Run the script by executing the code in your Python environment. It will read the input data from 'input.txt', process it, and write the results to 'output.txt'.

3. After execution, you can check the 'output.txt' file to see the available meeting times.

## Input Format

The script expects the following input data:

- `person1_schedule`: A list of time slots when person 1 is available, where each time slot is represented as `[start_time, end_time]`. Time format should be in HH:MM.

- `person1_daily_activity`: A list representing the daily availability of person 1, in the format `[start_time, end_time]`.

- `person2_schedule`: A list of time slots when person 2 is available, in the same format as `person1_schedule`.

- `person2_daily_activity`: A list representing the daily availability of person 2, in the same format as `person1_daily_activity`.

- `duration_of_meeting`: The duration of the desired meeting in minutes.

## Output Format

The script will generate a list of available meeting time slots between person 1 and person 2. Each available time slot is represented as `[start_time, end_time]` in the 'output.txt' file.

## Example Input

```
# Input.txt
[
  ['09:00', '11:00'],
  ['13:00', '14:30'],
  ['15:30', '17:00'],
  ['18:00', '20:00'],
  ['08:00', '22:00'],
]
['12:00', '13:00']
[
  ['09:30', '10:30'],
  ['12:30', '14:00'],
  ['14:30', '15:30'],
  ['17:00', '18:30'],
  ['08:00', '22:00'],
]
['13:30', '14:30']
45
```

## Example Output

```
# Output.txt
[['13:00', '13:45'], ['14:00', '14:30'], ['15:00', '15:30'], ['18:00', '18:30']]
```

## Note

- The script assumes that the input data is well-formed and valid.
- Make sure to provide the input in the specified format.

Feel free to modify and adapt the script as needed for your specific use case.
