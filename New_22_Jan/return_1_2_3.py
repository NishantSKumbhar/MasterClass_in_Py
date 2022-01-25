"""
@author : Nishant Sanjay Kumbhar
@goal : a, b, c = fun_name() because it returns three values.
"""


def converter(num):
    """
    this is converter method to convert the seconds into hr / min / second format
    :param num: seconds
    :return: format
    """
    hr = num // 3600
    hr_remain = num % 3600
    min = hr_remain // 60
    sec_remain = hr_remain % 60
    return hr, min, sec_remain


def main():
    sec = int(input("Enter the Seconds : "))
    hr, min, seconds = converter(sec)
    print(f"{hr} hr  {min} minutes  {seconds} seconds")


main()
