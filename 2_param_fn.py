from datetime import datetime

def year_to_month(year):
    total_months = year * 12
    print( f"{year} years is equal to {total_months} months" )

def month_to_year(month):
    total_years = month / 12
    print( f"{month} months is equal to {total_years} years" )

def age_in_months(birth_date):
    '''
    birth_date: yyyy-mm-dd
    '''
    today = datetime.now()
    age = today - birth_date
    age_in_months = age.days / 30
    print( f"Age in months: {round( age_in_months, 2 )}" )

def age_in_hours(birth_date):
    '''
    birth_date: yyyy-mm-dd
    '''
    today = datetime.now()
    age = today - birth_date
    age_in_hours = age.days * 24
    print( f"Age in hours: {age_in_hours}" )

# year_to_month(2.3)
age_in_months(datetime(2001, 2, 12))
age_in_hours(datetime(2001, 2, 12))
