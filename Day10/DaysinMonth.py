def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True #is_leap = True also another method but the method used here is faster as it     skippes the most of the code
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(check_year, check_month):
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(check_year):
        month_days[1] += 1

    return month_days[check_month - 1]
     
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
