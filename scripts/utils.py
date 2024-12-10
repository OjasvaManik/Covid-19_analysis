def filter_by_date(data, start_date, end_date):
    return data[(data["date"] >= start_date) & (data["date"] <= end_date)]