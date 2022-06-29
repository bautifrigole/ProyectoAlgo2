def get_day_month(date):
    day_month = ["", "", ""]
    index = 0
    for i in range(len(date)):
        if date[i] != "-" and date[i] != "/" and date[i] != "_":
            day_month[index] += date[i]
        else:
            index += 1
            if index == 3:
                break

    day_month[0] = int(day_month[0])
    day_month[1] = int(day_month[1])
    day_month[2] = int(day_month[2])
    if is_valid_date(day_month):
        return day_month
    else:
        print("Error: Invalid date")


def get_last_day(month):
    max_day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return max_day_per_month[month-1]


def is_valid_date(day_month):
    max_day_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 0 < day_month[0] <= max_day_per_month[day_month[1] + 1]:
        return True
    else:
        return False
