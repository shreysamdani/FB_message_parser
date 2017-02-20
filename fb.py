import time as Time
import calendar

person1 = ""
person2 = ""
filename = "messages.htm"
cal = {m: n for n,m in enumerate(calendar.month_name)}


# takes a time in string format in the htm file and converts to epoch
def epoch(time):
    time = time.split()
    month = time[1]
    day = time[2]
    year = time[3]
    hours = time[5].split(':')

    if hours[1][-2:] == 'pm':
        if hours[0] == '12':
            hours[0] = '0'
        else:
            hours[0] = str(int(hours[0]) + 12)

    date_and_time = str(cal[month]) + "." + day[:-1] + "." + year + " " + hours[0] + ":" + hours[1][:-2]

    pattern = '%m.%d.%Y %H:%M'
    return [int(Time.mktime(Time.strptime(date_and_time, pattern))), date_and_time]


# parses the file
def parser(file):

    # splits up the file into lines
    fblines = open(file).read()
    fblines = fblines.split("><")

    # sorts the fblines into a nested list with person, time, and message
    ordered = []
    current = -1 # current conversation

    for i in range(len(fblines)):
        if fblines[i][-20:] == '<div class="message"':
            ordered.append([fblines[i][19:-20],[]])
            current += 1

        if fblines[i][-6:] == '</span' and fblines[i][-7] != "T":
            name = fblines[i][18:-6]
            time = epoch(fblines[i + 1][18:-6])
            message = fblines[i + 4][2: -3]
            complete = [name, time, message]
            ordered[current][1].append(complete)


    return ordered

for line in parser(filename):
    if line[0] == person1 + ", " + person2 or line[0] == person2 + ", " + person1:
        for line1 in line[1]:
            print(str(line1[0]) + ':')
            print(line1[1][1])
            print(line1[2])
            print()


# print(max(parser(filename), key = lambda x: len(x[2]))[2])

