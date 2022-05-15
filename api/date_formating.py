from datetime import datetime

def format_date_time():
    current_time = datetime.now()
    formated_time = current_time.strftime('%Y%m%d%H%M%S')

    return formated_time