"""
@author : Nishant Sanjay kumbhar
@goal   : To implement calender i.e month class
"""
import sys
print("Blue Sky Inc.")


class Month:
    def __init__(self, january: dict) -> None:
        self.__dict__ = january

    def get_day(self, day):
        return self.__dict__.get(day)

# ---------------------------------------------------------------------------------------------


def get_month_dict(start_day: str, no_of_day: int) -> dict:
    days = []
    print(start_day)
    week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    # print(days)
    flag = 0
    for k in range(7):
        if week_days[k] == start_day:
            flag = k
            break

    print("flag : ", flag)
    for i in range(1, no_of_day + 1):
        days.append(i)
    # print(days)
    days_dict = dict.fromkeys(days)
    # print(days_dict)
    j = flag
    for i in days_dict:
        if j == 7:
            j = 0
        days_dict[i] = week_days[j]
        j = j + 1
    # print(days_dict)
    return days_dict
# ---------------------------------------------------------------------------------------------

"""
days = []
week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(days)
for i in range(1, 32):
    days.append(i)
print(days)
days_dict = dict.fromkeys(days)
print(days_dict)
j = 0
for i in days_dict:
    if j == 7:
        j = 0
    days_dict[i] = week_day[j]
    j = j + 1
    
"""
week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
"""
if
"""
mon = get_month_dict(week_day[3], 31)
print(mon)

jan = Month(mon)
k = jan.get_day(31)
print(k)
# days_dict[1] = 'Sunday'
nov_month = get_month_dict(week_day[1], 30)
nov = Month(nov_month)
today = nov.get_day(19)
print(today)
