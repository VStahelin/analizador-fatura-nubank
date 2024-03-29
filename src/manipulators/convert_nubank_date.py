from datetime import datetime, timedelta


def convert_date(date_str):
    days_mapping = {
        "Segunda": 0,
        "Terça": 1,
        "Quarta": 2,
        "Quinta": 3,
        "Sexta": 4,
        "Sábado": 5,
        "Domingo": 6,
    }

    today = datetime.today()

    if len(date_str.split()) == 2:
        day, month = map(str.strip, date_str.split())
        month_number = {
            "JAN": 1,
            "FEV": 2,
            "MAR": 3,
            "ABR": 4,
            "MAI": 5,
            "JUN": 6,
            "JUL": 7,
            "AGO": 8,
            "SET": 9,
            "OUT": 10,
            "NOV": 11,
            "DEZ": 12,
        }[month.upper()]
        return datetime(today.year, month_number, int(day))

    if date_str in days_mapping:
        target_day = days_mapping[date_str]
        today = datetime.today()
        today_weekday = today.weekday()
        if today_weekday > target_day:
            return today - timedelta(days=today_weekday - target_day)
        else:
            return today - timedelta(days=today_weekday + 7 - target_day)
    return today
