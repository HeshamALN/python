from datetime import datetime

date_format = "%d/%m/%Y"


def check_birthdate(year,month,day):
    try:
        birth_date = str(day) + "/" + str(month) + "/" + str(year)
        end_date = datetime.strptime("04/09/2019", date_format)
        birth_date = datetime.strptime(birth_date, date_format)
        if birth_date < end_date:
            return True
        else:
            return False
    except:
        return  False

def calculate_age(year,month,day):
    today = datetime.today()
    birth_date = str(day) + "/" + str(month) + "/" + str(year)
    birth_date = datetime.strptime(birth_date, date_format)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

year = input("Enter birth year: ")
month = input("Enter birth month: ")
day = input("Enter birth day: ")

if check_birthdate(year,month,day):
    print(calculate_age(year,month,day), " Years")
else:
    print("Brithdate is invalid")