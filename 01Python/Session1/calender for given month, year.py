import calendar

def search_calender():
    year=int(input("enter year : "))
    month=int(input("enter month : "))

    result=calendar.month(year,month)
    print(f"Calender for {calendar.month_name[month]} {year}\n")
    print(result)

search_calender()