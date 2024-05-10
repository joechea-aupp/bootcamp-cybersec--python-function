from datetime import datetime

def print_time():
    # get current time
    current_time = datetime.now()

    # format current date to dd/mm/yyyy - hh:mm:ss AM/PM
    formatted_date = current_time.strftime('%d/%m/%Y - %I:%M:%S %p')

    # display current time when function is called
    print('Current time: ', formatted_date)


print_time()
