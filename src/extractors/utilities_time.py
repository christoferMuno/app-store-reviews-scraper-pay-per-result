thonfrom datetime import datetime

def convert_timestamp_to_date(timestamp):
    try:
        return datetime.fromisoformat(timestamp)
    except ValueError:
        return None