#Euler19
months = [-1,31,28,31,30,31,30,31,31,30,31,30,31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

dayindex = 0
year = 1900
month = 1
date = 1

sunday1count = 0

while year <= 2000:
    if year%4 == 0:#leap year
        if year%400 == 0 and year%100 != 0:
            months[2] = 29
    else:
        months[2] = 28

    while month <= 12:
        while date <= months[month]:
            day = days[dayindex]
            print(year, '/' , month , '/' , date, day)
            if(dayindex == 6 and date == 1):
                sunday1count += 1
                print('sunday')

            date += 1
            if dayindex == 6:
                dayindex = 0
            else:
                dayindex += 1

        date = 1
        month += 1
    month = 1
    year += 1

print(sunday1count)
